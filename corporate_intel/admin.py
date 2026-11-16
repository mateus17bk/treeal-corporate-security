from django.contrib import admin
from .models import EmpresaConsulta

@admin.register(EmpresaConsulta)
class EmpresaConsultaAdmin(admin.ModelAdmin):
    list_display = ('cnpj', 'razao_social', 'municipio', 'uf', 'situacao', 'risk_level', 'criado_em')
    search_fields = ('cnpj', 'razao_social', 'nome_fantasia', 'municipio')
    list_filter = ('risk_level', 'situacao', 'uf')
