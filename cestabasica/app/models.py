from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Cliente(models.Model):
    cpf = models.CharField(primary_key=True, max_length=12, null=False, blank=False)
    nome = models.CharField(max_length=200, null=False, blank=False)
    telefone = models.CharField(max_length=12, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    cidade = models.CharField(max_length=100, null=False, blank=False)
    cep = models.CharField(max_length=8, null=False, blank=False)
    rua = models.CharField(max_length=100, null=False, blank=False)
    numero = models.CharField(max_length=20, null=False, blank=False)
    estado = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        db_table ='cliente'

    def __stf__(self):
        return self.nome



class Vendedor(models.Model):
    cpf = models.CharField(primary_key=True, max_length=12, null=False, blank=False)
    nome = models.CharField(max_length=100)
    email = models.EmailField(null=False, blank=False)

    class Meta:
        db_table ='vendedor'

    def __str__(self):
        return self.nome

class Produto(models.Model):
    codigo_barras = models.IntegerField(primary_key=True, null=False, blank=False)
    nome = models.TextField(null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    preco = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    quantidade = models.IntegerField(null=False, blank=False)
    class Meta:
        db_table = 'produto'

    def __str__(self):
        return self.descricao

class Cesta(models.Model):
    nome = models.TextField(null=False, blank=False);
    quantidade = models.IntegerField(null=False, blank=False)
    preco = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    produtos = models.ManyToManyField(Produto)

    class Meta:
        db_table = 'cesta'

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    TIPO_PAGAMENTO_CHOICES =(
        ("A", "A vista"),
        ("P", "A prazo"),
        ("C", "Cartao")
       )
    cpf_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    cpf_vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    quantidade = models.IntegerField(null=False, blank=False)
    precototal = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    data = models.DateTimeField(default=timezone.now)
    tipo_pagamento = models.CharField(max_length=1, choices=TIPO_PAGAMENTO_CHOICES)
    cestas = models.ManyToManyField(Cesta)


    class Meta:
        db_table ='pedido'

    def __str__(self):
        return self.id





    
    
