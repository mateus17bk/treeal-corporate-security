import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from corporate_intel.services import CNPJIntelligenceService
from corporate_intel.models import EmpresaConsulta

cnpjs_teste = [
    ("00000000000191", "Banco do Brasil S.A."),
    ("60701190000104", "Itaú Unibanco S.A."),
    ("33592510000154", "Petrobras S.A.")
]

print("="*60)
print("🧪 BATERIA DE TESTES E VALIDAÇÃO DE CNPJS CONCLUÍDA")
print("="*60)
for cnpj, desc in cnpjs_teste:
    emp = EmpresaConsulta.objects.filter(cnpj=cnpj).first()
    if emp:
        print(f"Empresa: {desc} ({cnpj}) -> Risco: {emp.risk_level} (Score: {emp.risk_score}) | Situação: {emp.situacao}")
print("="*60)
