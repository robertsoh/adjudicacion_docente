from django.db import models


class Colegio(models.Model):
    codigo_modular = models.CharField('Código modular', max_length=15, blank=True, null=True)
    codigo_colegio = models.CharField('Código colegio', max_length=15, blank=True, null=True)
    anexo = models.IntegerField('Anexo', default=0, null=True)
    codigo_local = models.CharField('Código colegio', max_length=15, blank=True, null=True)
    forma = models.CharField('Forma', max_length=15, blank=True, null=True)
    nivel = models.CharField('Nivel', max_length=50, blank=True, null=True)
    nombre = models.CharField('Nombre', max_length=255, blank=True, null=True)
    telefono = models.CharField('Teléfono', max_length=50, blank=True, null=True)
    direccion = models.CharField('Dirección', max_length=255, blank=True, null=True)
    centro_poblado = models.CharField('Centro poblado', max_length=100, blank=True, null=True)
    ubigeo = models.CharField('Ubigeo', max_length=10, blank=True, null=True)
    departamento = models.CharField('Departamento', max_length=100, blank=True, null=True)
    provincia = models.CharField('Provincia', max_length=100, blank=True, null=True)
    distrito = models.CharField('Distrito', max_length=100, blank=True, null=True)
    area = models.CharField('Área', max_length=100, blank=True, null=True)
    region = models.CharField('Región', max_length=100, blank=True, null=True)
    ugel_codigo = models.CharField('Ugel código', max_length=15, blank=True, null=True)
    ugel_nombre = models.CharField('Ugel nombre', max_length=150, blank=True, null=True)
