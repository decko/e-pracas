from django.db import models
from django.forms import ModelForm

# Create your models here.

class Tipo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Espaco(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class FaixasEtaria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Parceiro(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Publico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Abrangencia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Periodicidade(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Area(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Subarea(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Atividade(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    tipo = models.ForeignKey(Tipo)
    area = models.ForeignKey(Area)
    subarea = models.ForeignKey(Subarea)
    espacos = models.ManyToManyField(Espaco)
    parceiros = models.CharField(max_length=255)
    faixas_etarias = models.ManyToManyField(FaixasEtaria)
    publico = models.ManyToManyField(Publico)
    abrangencia = models.ForeignKey(Abrangencia)
    data_inicio = models.DateField()
    data_termino = models.DateField()
    periodicidade = models.ForeignKey(Periodicidade)
    hora_inicio = models.TimeField()
    hora_termino = models.TimeField()
    publico_esperado = models.IntegerField()

    def __str__(self):
        return self.nome
