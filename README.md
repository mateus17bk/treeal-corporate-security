# CorpGuard Intelligence & Anti-Fraud Platform

Plataforma corporativa em **Django (Arquitetura MVC)** para consulta avançada de CNPJs, enriquecimento de dados cadastrais, varredura forense de métodos de pagamento (Pix, cartões, gateways) e análise de compliance/risco integrada com o Portal da Transparência da CGU (CEIS/CNEP).

---

## 🚀 Funcionalidades Principais

1. **Validação Matemática e Estrutural de CNPJ**:
   - Cálculo rigoroso de Dígitos Verificadores (DV).
2. **Sistema Multi-API Fallback**:
   - Consulta em cascata (`BrasilAPI` -> `Minha Receita` -> `CNPJ.ws`) para garantir alta disponibilidade de dados cadastrais.
3. **Varredura Forense de Meios de Pagamento (OSINT)**:
   - Análise automática da infraestrutura web e scripts de checkout (Mercado Pago, Pagar.me, Stripe, Pix, VTEX).
4. **Compliance & Sanções Federais (CGU)**:
   - Consulta em tempo real aos cadastros oficiais de empresas inidôneas, suspensas e punidas (CEIS e CNEP).
5. **Índice de Risco / Fraude Automatizado**:
   - Motor de pontuação (0 a 100) com classificação de risco (`BAIXO`, `MÉDIO`, `ALTO`) e relatório detalhado de justificativas.
6. **Interface Moderna (Tailwind CSS)**:
   - Dashboard analítico, histórico completo de auditoria e relatórios de diligência prontos para impressão.

---

## 🛠️ Como Executar o Projeto

```bash
cd /root/corporate-security-app
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt # ou instalar django, requests, gunicorn
python run.py migrate
python run.py runserver 0.0.0.0:8000
```

---
Co-Authored-By: Claude Code <noreply@anthropic.com>
🤖 Generated with [Claude Code](https://claude.com/claude-code)
