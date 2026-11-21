import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

import pytest
from corporate_intel.services import CNPJValidator, CreditRiskService, CGUComplianceService
from corporate_intel.models import EmpresaConsulta

@pytest.mark.django_db
class TestTreealQAAGENT:

    def test_cnpj_validator_valid(self):
        valid_cnpj = "00.000.000/0001-91"
        cleaned = CNPJValidator.validar(valid_cnpj)
        assert cleaned == "00000000000191"

    def test_cnpj_validator_invalid(self):
        invalid_cnpj = "11.111.111/1111-11"
        with pytest.raises(Exception):
            CNPJValidator.validar(invalid_cnpj)

    def test_credit_risk_calculation(self):
        risco = CreditRiskService.calcular(1000000.0, "BAIXO")

        assert "limite_sugerido" in risco
        assert "recomendacao_credito" in risco
        assert risco["limite_sugerido"] > 0

    def test_dashboard_access_redirect(self, client):
        response = client.get('/')
        assert response.status_code in [200, 302]

    def test_model_str(self):
        empresa = EmpresaConsulta.objects.create(
            cnpj="12345678000199",
            razao_social="Treeal Test Corp",
            situacao="ATIVA"
        )
        assert str(empresa) == "12345678000199 - Treeal Test Corp"
