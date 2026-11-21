import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

import pytest
from django.urls import reverse
from corporate_intel.views import custom_page_not_found_view

@pytest.mark.django_db
class TestCustom404View:

    def test_custom_404_template_renders(self, client):
        """Valida que a página 404 customizada carrega com o design system sem quebrar."""
        response = client.get('/pagina-que-nao-existe-12345/')
        assert response.status_code == 404
        assert b"P\xc3\xa1gina N\xc3\xa3o Encontrada" in response.content or b"Treeal" in response.content
