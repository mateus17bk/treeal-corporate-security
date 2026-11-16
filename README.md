# Treeal Corp • Compliance & BaaS Platform

Plataforma corporativa em **Django (Arquitetura MVC)** para consulta avançada de CNPJs, enriquecimento de dados cadastrais, varredura forense de métodos de pagamento (Pix, cartões, gateways) e análise de compliance/risco integrada com o Portal da Transparência da CGU (CEIS/CNEP) e Agente de IA do Google Gemini.

---

## 🚀 Funcionalidades Principais

1. **Validação Matemática e Estrutural de CNPJ**:
   - Cálculo rigoroso de Dígitos Verificadores (DV).
2. **Sistema Multi-API Fallback (5 Provedores)**:
   - Consulta em cascata (`BrasilAPI` ➔ `Minha Receita` ➔ `CNPJ.ws` ➔ `ReceitaWS` ➔ `CNPJa`) para garantir altíssima disponibilidade.
3. **Varredura Forense de Meios de Pagamento (OSINT)**:
   - Análise automática da infraestrutura web e scripts de checkout (Mercado Pago, Pagar.me, Stripe, Pix, VTEX).
4. **Compliance & Sanções Federais (CGU)**:
   - Consulta em tempo real aos cadastros oficiais de empresas inidôneas, suspensas e punidas (CEIS e CNEP).
5. **Agente de IA do Google (Gemini 2.5 Flash)**:
   - Geração automática de pareceres de segurança executivos para aprovação de transações.
6. **Autenticação & Controle de Operadores**:
   - Telas de Login e Cadastro de usuários vinculadas ao banco de dados, com widget de monitoramento em tempo real do status das APIs na barra lateral.
7. **Design System Treeal v0.1**:
   - Interface moderna em modo escuro com cartões translúcidos (*Glassmorphism*).

---

## 🛠️ Como Executar o Projeto Localmente

```bash
cd corporate-security-app
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

---
Co-Authored-By: Claude Code <noreply@anthropic.com>
🤖 Generated with [Claude Code](https://claude.com/claude-code)
