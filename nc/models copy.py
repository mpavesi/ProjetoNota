from ast import Delete
from datetime import datetime
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Lay_Out_107(models.Model):
    codigo_do_cliente = models.CharField(max_length=9)
    cnpj_cpf_cliente = models.CharField(max_length=11)
    tipo_de_cliente = models.CharField(max_length=2)
    data_do_pregao = models.DateField()
    numero_da_nota = models.CharField(max_length=9)
    assessor = models.CharField(max_length=5)
    vendas_a_vista = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    compras_a_vista = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    opcoes_de_compra = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    opcoes_de_venda = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    outras_operacoes = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    valor_liquido_das_operacoes = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    taxas = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    emolumentos = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    corretagem_liquida = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    corretagem_bruta = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    valor_liquido_da_nota = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    sinal_do_valor_liquido = models.CharField(max_length=1)
    constante = models.CharField(max_length=10)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.numero_da_nota
    
class Lay_Out_108(models.Model):
    codigo_do_cliente = models.CharField(max_length=9)
    cnpj_cpf_cliente = models.CharField(max_length=11)
    tipo_de_cliente = models.CharField(max_length=2)
    data_do_pregao = models.DateField()
    numero_da_nota = models.CharField(max_length=9)
    tipo_do_mercado = models.CharField(max_length=20, null=True)
    compra_venda = models.CharField(max_length=1, null=True)
    especificacao_do_titulo = models.CharField(max_length=30, null=True)
    obs = models.CharField(max_length=3)
    quantidade = models.IntegerField()
    preco_da_liquidacao = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    valor_da_operacao = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    numero_sequencial_da_operacao = models.PositiveIntegerField()
    codigo_da_contraparte = models.CharField(max_length=8)
    constante = models.CharField(max_length=50)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.numero_da_nota

class Titneg(models.Model):
    codneg = models.CharField(primary_key=True, max_length=12)
    codemp = models.CharField(max_length=4)
    densoc = models.CharField(max_length=60)
    nomres = models.CharField(blank=True, null=True, max_length=12)
    dtcria = models.DateTimeField(auto_now_add=True)
    dtatua = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.codneg

    
class Notcor(models.Model):
    NATOPE_CHOICES = (
        ("C", "Compra"),
        ("V", "Venda")
    )
    notcor = models.CharField(max_length=9)
    natope = models.CharField(max_length=1, null=True)
    natope = models.CharField(max_length=1, choices=NATOPE_CHOICES, blank=False, null=False)
    codneg = models.ForeignKey(Titneg, on_delete = models.CASCADE)
    dtnota = models.DateField()
    quanti = models.IntegerField()
    pcunit = models.DecimalField(max_digits=13, decimal_places=2)
    corret = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    despes = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    emolum = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    taxliq = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    valliq = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    dtcria = models.DateTimeField(auto_now_add=True)
    dtatua = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.notcor
