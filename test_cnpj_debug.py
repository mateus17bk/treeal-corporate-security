import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from corporate_intel.services import CNPJIntelligenceService
from corporate_intel.models import EmpresaConsulta

cnpj_teste = "69346856000110"
print(f"🔍 Investigando CNPJ {cnpj_teste}...")

# Deleta do banco local para forçar nova consulta nas APIs
EmpresaConsulta.objects.filter(cnpj=cnpj_teste).delete()

empresa = CNPJIntelligenceService.consultar_cnpj(cnpj_teste)
print(f"🏢 Razão Social: {empresa.razao_social}")
print(f"📍 Situação: {empresa.situacao}")
print(f"📊 Risco: {empresa.risk_level} (Score: {empresa.risk_score})")
print(f"📋 Motivos: {empresa.motivos_risco}")
print(f"🤖 Parecer IA: {empresa.compliance_processos.get('parecer_ia')}")
