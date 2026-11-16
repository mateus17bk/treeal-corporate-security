from django.db import models

class EmpresaConsulta(models.Model):
    cnpj = models.CharField(max_length=14, unique=True, db_index=True)
    razao_social = models.CharField(max_length=255, blank=True, null=True)
    nome_fantasia = models.CharField(max_length=255, blank=True, null=True)
    situacao = models.CharField(max_length=50, blank=True, null=True)
    data_abertura = models.CharField(max_length=20, blank=True, null=True)
    capital_social = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    natureza_juridica = models.CharField(max_length=255, blank=True, null=True)
    atividade_principal = models.TextField(blank=True, null=True)

    # Endereço e Contato
    logradouro = models.CharField(max_length=255, blank=True, null=True)
    numero = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    municipio = models.CharField(max_length=100, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=50, blank=True, null=True)

    # Campos estruturados JSON
    socios = models.JSONField(default=list, blank=True)
    metodos_pagamento = models.JSONField(default=list, blank=True)
    compliance_processos = models.JSONField(default=dict, blank=True)

    # Análise de Fraude / Risco
    risk_score = models.IntegerField(default=0)  # 0 a 100
    risk_level = models.CharField(max_length=20, default='BAIXO') # BAIXO, MÉDIO, ALTO
    motivos_risco = models.TextField(blank=True, null=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.cnpj} - {self.razao_social or 'Desconhecida'}"
