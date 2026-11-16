from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import EmpresaConsulta
from .services import CNPJIntelligenceService

def dashboard_view(request):
    query = request.GET.get('q', '').strip()
    empresas = EmpresaConsulta.objects.all().order_by('-criado_em')

    if query:
        empresas = empresas.filter(
            models_q_cnpj_or_name(query)
        ) if hasattr(empresas, 'filter') else empresas

    # Estatísticas
    total_consultas = EmpresaConsulta.objects.count()
    risco_alto = EmpresaConsulta.objects.filter(risk_level='ALTO').count()
    risco_medio = EmpresaConsulta.objects.filter(risk_level='MÉDIO').count()
    risco_baixo = EmpresaConsulta.objects.filter(risk_level='BAIXO').count()

    context = {
        'empresas': empresas[:20], # Últimas 20
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
        try:
            empresa = CNPJIntelligenceService.consultar_cnpj(cnpj_input)
            messages.success(request, f"CNPJ {empresa.cnpj} consultado e analisado com sucesso!")
            return redirect('detalhes_empresa', pk=empresa.pk)
        except ValidationError as e:
            messages.error(request, str(e))
        except Exception as e:
            messages.error(request, f"Erro inesperado na consulta: {str(e)}")

    return redirect('dashboard')

def detalhes_empresa_view(request, pk):
    empresa = get_object_or_404(EmpresaConsulta, pk=pk)
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
