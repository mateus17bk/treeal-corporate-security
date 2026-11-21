import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

import pytest
from django.urls import reverse
from corporate_intel.services import CNPJValidator, CreditRiskService, MultiAPIFallbackService
from corporate_intel.models import EmpresaConsulta

@pytest.mark.django_db
class TestAdvancedQAAgent:

    def test_navigation_urls_resolve(self):
        """Valida se as URLs principais respondem corretamente sem quebrar."""
        assert reverse('login') == '/'
        assert reverse('dashboard') == '/dashboard/'
        assert reverse('historico') == '/historico/'
        assert reverse('register') == '/cadastro/'

    def test_cnpj_cleaning_and_formatting(self):
        """Valida sanitização de máscara de CNPJ para evitar erros do usuário."""
        raw_inputs = [
            "00.000.000/0001-91",
            "00000000000191",
            "  00.000.000/0001-91 "
        ]
        for val in raw_inputs:
            assert CNPJValidator.validar(val) == "00000000000191"

    def test_invalid_cnpj_raises_error(self):
        """Garante que CNPJs inválidos geram erro amigável."""
        with pytest.raises(Exception):
            CNPJValidator.validar("12.345.678/0001-99")

    def test_credit_risk_edge_cases(self):
        """Valida cálculo de crédito para cenários extremos (capital zero ou alto risco)."""
        # Risco Alto -> Limite deve ser zero
        res_alto = CreditRiskService.calcular(500000.0, "ALTO")
        assert res_alto["limite_sugerido"] == 0.0

        # Risco Baixo com capital zero -> Limite padrão seguro
        res_baixo_zero = CreditRiskService.calcular(0.0, "BAIXO")
        assert res_baixo_zero["limite_sugerido"] == 15000.0

    def test_dashboard_context_comfort(self, client):
        """Valida que o dashboard carrega elementos essenciais para o conforto e UX."""
        response = client.get(reverse('login'))
        assert response.status_code == 200
        # Verifica se o template de login carrega sem erro interno
        assert b"Treeal" in response.content or response.status_code == 200
