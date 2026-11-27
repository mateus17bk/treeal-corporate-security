from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from .models import EmpresaConsulta
from .services import CNPJIntelligenceService

def dashboard_view(request):
    query = request.GET.get('q', '').strip()
    empresas = EmpresaConsulta.objects.all().order_by('-criado_em')

    if query:
        empresas = empresas.filter(models_q_cnpj_or_name(query))

    total_consultas = EmpresaConsulta.objects.count()
    risco_alto = EmpresaConsulta.objects.filter(risk_level='ALTO').count()
    risco_medio = EmpresaConsulta.objects.filter(risk_level='MÉDIO').count()
    risco_baixo = EmpresaConsulta.objects.filter(risk_level='BAIXO').count()

    context = {
        'empresas': empresas[:20],
        'total_consultas': total_consultas,
        'risco_alto': risco_alto,
        'risco_medio': risco_medio,
        'risco_baixo': risco_baixo,
        'query': query
    }
    return render(request, 'corporate_intel/dashboard.html', context)

def models_q_cnpj_or_name(query):
    from django.db.models import Q
    return Q(cnpj__icontains=query) | Q(razao_social__icontains=query) | Q(nome_fantasia__icontains=query) | Q(municipio__icontains=query)

def consultar_cnpj_view(request):
    if request.method == 'POST':
        cnpj_input = request.POST.get('cnpj', '').strip()
        forcar = request.POST.get('forcar', 'false') == 'true'
        try:
            empresa = CNPJIntelligenceService.consultar_cnpj(cnpj_input, forcar_atualizacao=forcar)
            messages.success(request, f"CNPJ {empresa.cnpj} consultado e analisado com sucesso!")
            return redirect('detalhes_empresa', pk=empresa.pk)
        except ValidationError as e:
            messages.error(request, str(e))
        except Exception as e:
            messages.error(request, f"Erro inesperado na consulta: {str(e)}")

    return redirect('dashboard')

def detalhes_empresa_view(request, pk):
    try:
        empresa = EmpresaConsulta.objects.get(pk=pk)
    except EmpresaConsulta.DoesNotExist:
        empresa = EmpresaConsulta.objects.first()
        if not empresa:
            messages.error(request, "Nenhuma empresa cadastrada no sistema.")
            return redirect('dashboard')
        return redirect('detalhes_empresa', pk=empresa.pk)

    if request.GET.get('atualizar') == '1':
        try:
            empresa = CNPJIntelligenceService.consultar_cnpj(empresa.cnpj, forcar_atualizacao=True)
            messages.success(request, "Dados atualizados com sucesso via APIs externas!")
            return redirect('detalhes_empresa', pk=empresa.pk)
        except Exception as e:
            messages.error(request, f"Não foi possível atualizar agora: {e}")

    context = {
        'empresa': empresa
    }
    return render(request, 'corporate_intel/detalhes.html', context)

def historico_view(request):
    empresas = EmpresaConsulta.objects.all().order_by('-criado_em')
    context = {
        'empresas': empresas
    }
    return render(request, 'corporate_intel/historico.html', context)

def registrar_usuario_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Conta criada com sucesso! Bem-vindo à plataforma.")
            return redirect('dashboard')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'corporate_intel/register.html', context)

class CustomLoginView(LoginView):
    template_name = 'corporate_intel/login.html'
    redirect_authenticated_user = True

def custom_page_not_found_view(request, exception):
    return render(request, 'corporate_intel/404.html', status=404)
