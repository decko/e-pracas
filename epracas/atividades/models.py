from django.db import models

from smart_selects.db_fields import ChainedForeignKey


# Create your models here.
# Modelos de dados para os CEUS '''
class SituacaoCeu(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Estado(models.Model):
    nome = models.CharField(max_length=100)
    cod_ibge = models.IntegerField()

    def __str__(self):
        return self.nome


class Municipio(models.Model):
    nome = models.CharField(max_length=255)
    cod_ibge = models.IntegerField()
    estado = models.ForeignKey(Estado)

    def __str__(self):
        return self.nome


class Responsavel(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Ceu(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    responsavel = models.ForeignKey(Responsavel)
    municipio = models.ForeignKey(Municipio)
    situacao = models.ForeignKey(SituacaoCeu)

    def __str__(self):
        return self.nome


# Modelos de dados para as Atividades '''
class Tipo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

    def natural_key(self):
        return (self.nome)


class Espaco(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

    def natural_key(self):
        return (self.nome)


class FaixasEtaria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

    def natural_key(self):
        return (self.nome)


class Parceiro(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

    def natural_key(self):
        return (self.nome)


class Publico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

    def natural_key(self):
        return (self.nome)


class Abrangencia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

    def natural_key(self):
        return (self.nome)


class Periodicidade(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

    def natural_key(self):
        return (self.nome)


class Area(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

    def natural_key(self):
        return (self.nome)


class Subarea(models.Model):
    area = models.ForeignKey(Area)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

    def natural_key(self):
        return (self.nome)


class Atividade(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    parceiros = models.CharField(max_length=255)
    data_inicio = models.DateTimeField()
    data_termino = models.DateTimeField()
    # hora_inicio = models.TimeField()
    # hora_termino = models.TimeField()
    publico_esperado = models.IntegerField()
    tipo = models.ForeignKey(Tipo)
    area = models.ForeignKey(Area)
    subarea = ChainedForeignKey(
        Subarea,
        chained_field='area',
        chained_model_field='area',
        show_all=False,
        auto_choose=True,
        blank=True,
    )
    espacos = models.ManyToManyField(Espaco)
    faixas_etarias = models.ManyToManyField(FaixasEtaria)
    publico = models.ManyToManyField(Publico)
    abrangencia = models.ForeignKey(Abrangencia)
    periodicidade = models.ForeignKey(Periodicidade)
    ceu = models.ForeignKey(Ceu)

    def __str__(self):
        return self.nome
