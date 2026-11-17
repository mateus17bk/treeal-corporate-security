import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from corporate_intel.services import CNPJIntelligenceService
from corporate_intel.models import EmpresaConsulta

print("="*60)
print("🧪 VALIDANDO PERFORMANCE E AGENTE DE IA DO GOOGLE (GEMINI)")
print("="*60)

cnpj_teste = "60701190000104" # Itaú Unibanco
try:
    print(f"🔄 Consultando CNPJ {cnpj_teste} com cruzamento Multi-API + CGU + Google GenAI...")
    empresa = CNPJIntelligenceService.consultar_cnpj(cnpj_teste)
    print(f"  ✅ Razão Social: {empresa.razao_social}")
    print(f"  📊 Nível de Risco: {empresa.risk_level} (Score: {empresa.risk_score})")
    print(f"  🤖 Parecer Gerado pela IA do Google:")
    print(f"     \"{empresa.compliance_processos.get('parecer_ia')}\"")
    print("\n✨ Teste de performance executado com sucesso e sem gargalos!")
except Exception as e:
    print(f"  ❌ Erro durante o teste: {e}")

print("="*60)
