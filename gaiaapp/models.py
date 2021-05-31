# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import os
from django.contrib.gis.db import models
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from datetime import datetime
from jinja2 import Template
import webbrowser


class AlertasFlorestas(models.Model):
    id = models.IntegerField(blank=True, null=True, primary_key=True),
    geom = models.PointField(blank=True, null=True)
    datahora = models.CharField(max_length=80, blank=True, null=True)
    satelite = models.CharField(max_length=80, blank=True, null=True)
    pais = models.CharField(max_length=80, blank=True, null=True)
    estado = models.CharField(max_length=80, blank=True, null=True)
    municipio = models.CharField(max_length=80, blank=True, null=True)
    bioma = models.CharField(max_length=50, blank=True, null=True)
    diasemchuv = models.IntegerField(blank=True, null=True)
    precipitac = models.DecimalField(max_digits=20, decimal_places=8, blank=True, null=True)
    riscofogo = models.DecimalField(max_digits=20, decimal_places=8, blank=True, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=8, blank=True, null=True)
    frp = models.DecimalField(max_digits=20, decimal_places=8, blank=True, null=True)
    cnfp_id = models.IntegerField(blank=True, null=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    nome = models.CharField(max_length=200, blank=True, null=True, verbose_name='Nome')
    orgao = models.CharField(max_length=100, blank=True, null=True)
    classe = models.CharField(max_length=30, blank=True, null=True)
    estagio = models.CharField(max_length=30, blank=True, null=True)
    governo = models.CharField(max_length=20, blank=True, null=True)
    codigo = models.CharField(max_length=30, blank=True, null=True)
    ano = models.BigIntegerField(blank=True, null=True)
    uf = models.CharField(max_length=4, blank=True, null=True)
    protecao = models.CharField(max_length=30, blank=True, null=True)
    tipo = models.CharField(max_length=40, blank=True, null=True)
    comunitari = models.CharField(max_length=6, blank=True, null=True)
    atolegal = models.CharField(max_length=100, blank=True, null=True)
    anocriacao = models.BigIntegerField(blank=True, null=True)
    categoria = models.CharField(max_length=40, blank=True, null=True)
    observacao = models.CharField(max_length=200, blank=True, null=True)
    sobreposic = models.CharField(max_length=3, blank=True, null=True)
    area_ha = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return "{0} {1} {2}/{3} ".format(self.nome, self.datahora, self.municipio, self.uf)

    class Meta:
        managed = True
        db_table = 'alertas_florestas'
        verbose_name = "Alerta Floresta"
        verbose_name_plural = "Alertas Florestas"


class EmailsMP(models.Model):
    uf = models.CharField(max_length=200, blank=True, null=True, verbose_name='UF')
    email = models.EmailField(verbose_name="E-mail")

    def __str__(self):
        return self.uf + " " + self.email

    class Meta:
        managed = True
        db_table = 'email_mp'
        verbose_name = "E-mail Ministério Público"
        verbose_name_plural = "E-mails Ministério Público"


class TiposPenais(models.Model):
    tipo_penal = models.CharField(max_length=50, verbose_name="Tipo Penal")
    lei = models.CharField(max_length=50, verbose_name="Lei")
    descricao = models.TextField(verbose_name="Descrição")

    def __str__(self):
        return "{0} {1}".format(self.tipo_penal, self.lei)

    class Meta:
        managed = True
        db_table = 'tipo_penal'
        verbose_name = "Tipo Penais"
        verbose_name_plural = "Tipos Penais"


class NoticiaCrime(models.Model):
    alerta_florestal = models.ForeignKey(AlertasFlorestas,on_delete=models.CASCADE)
    tipo_penal = models.ForeignKey(TiposPenais, on_delete=models.CASCADE)
    email_mp = models.ForeignKey(EmailsMP, verbose_name="E-mail do Ministério Público",on_delete=models.CASCADE)
    user_email = models.EmailField(blank=True, verbose_name="E-mail do Usuario")
    url_doc = models.URLField(max_length=256, verbose_name="Endereço Documento Complementar", blank=True)
    data_documento = models.DateTimeField(verbose_name="Data/Hora documento", default=datetime.now)
    documento = models.FileField(verbose_name="Noticia Crime", blank=True)

    def __str__(self):
        return "{0} {1}".format(self.alerta_florestal.datahora,self.alerta_florestal.nome)

    class Meta:
        managed = True
        db_table = 'noticia_crime'
        verbose_name = "Notícia Crime"
        verbose_name_plural = "Notícias-Crime"

def openInBrowser():
    url = "file:/home/mauro/gaia/templates/template_noticia_crime_out.html"
    webbrowser.open(url)

def convertData(di):
    return (di[8:10] + "/" + di[5:7] + '/'  + di[0:4],
            di[11:13] + ":" + di[14:16] + ":" + di[17:19])

def likeJinja(template,replaces):
    for key,value in replaces.items():
        template = template.replace("{{ "+key + " }}",value)
    return template

def on_NoticiaCrime_save(sender, instance, **kwargs):
    data, hora = convertData(instance.alerta_florestal.datahora)

    replaces = {
        'alertas_florestas.datahora.data': data,
        'alertas_florestas.datahora.hora': hora,
        'alertas_florestas.municipio':instance.alerta_florestal.municipio,
        'alertas_florestas.uf':instance.alerta_florestal.uf,
        'alertas_florestas.geom':"{:.2f}".format(instance.alerta_florestal.area_ha),
        'alertas_florestas.latitude':"{:.4f}".format(instance.alerta_florestal.latitude),
        'alertas_florestas.longitude':"{:.4f}".format(instance.alerta_florestal.longitude),
        'alertas_florestas.bioma':instance.alerta_florestal.bioma,
        'alertas_florestas.orgao':instance.alerta_florestal.orgao,
        'alerta_florestas.datahora.data':datetime.now().strftime("%d/%m/%Y"),
        'link_earth': "https://maps.google.com/?q={0},{1}&basemap=satellite".format(instance.alerta_florestal.latitude,
                                                                  instance.alerta_florestal.longitude)
    }
    with open("/home/mauro/gaia/templates/template_noticia_crime.html") as f:
        template = f.read()
    replaced = likeJinja(template,replaces)
    with open("/home/mauro/gaia/templates/template_noticia_crime_out.html",mode='w') as f:
        f.write(replaced)
    openInBrowser()
    #instance.documento = replaced

pre_save.connect(on_NoticiaCrime_save, sender=NoticiaCrime)

class Cnfp(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    nome = models.CharField(max_length=200, blank=True, null=True)
    orgao = models.CharField(max_length=100, blank=True, null=True)
    classe = models.CharField(max_length=30, blank=True, null=True)
    estagio = models.CharField(max_length=30, blank=True, null=True)
    governo = models.CharField(max_length=20, blank=True, null=True)
    codigo = models.CharField(max_length=30, blank=True, null=True)
    ano = models.BigIntegerField(blank=True, null=True)
    uf = models.CharField(max_length=4, blank=True, null=True)
    protecao = models.CharField(max_length=30, blank=True, null=True)
    tipo = models.CharField(max_length=40, blank=True, null=True)
    comunitari = models.CharField(max_length=6, blank=True, null=True)
    atolegal = models.CharField(max_length=100, blank=True, null=True)
    anocriacao = models.BigIntegerField(blank=True, null=True)
    categoria = models.CharField(max_length=40, blank=True, null=True)
    observacao = models.CharField(max_length=200, blank=True, null=True)
    sobreposic = models.CharField(max_length=3, blank=True, null=True)
    bioma = models.CharField(max_length=50, blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    area_ha = models.BigIntegerField(blank=True, null=True)
    layer = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome + "//" + self.uf

    class Meta:
        managed = True
        db_table = 'cnfp'
        verbose_name = "Cadastro Nacional de Florestas Públicas"


class FocosIncendioInpe(models.Model):
    geom = models.PointField(blank=True, null=True)
    datahora = models.CharField(max_length=80, blank=True, null=True)
    satelite = models.CharField(max_length=80, blank=True, null=True)
    pais = models.CharField(max_length=80, blank=True, null=True)
    estado = models.CharField(max_length=80, blank=True, null=True)
    municipio = models.CharField(max_length=80, blank=True, null=True)
    bioma = models.CharField(max_length=80, blank=True, null=True)
    diasemchuv = models.IntegerField(blank=True, null=True)
    precipitac = models.DecimalField(max_digits=20, decimal_places=8, blank=True, null=True)
    riscofogo = models.DecimalField(max_digits=20, decimal_places=8, blank=True, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=8, blank=True, null=True)
    frp = models.DecimalField(max_digits=20, decimal_places=8, blank=True, null=True)
    cnfp_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.municipio + '/' + self.estado

    class Meta:
        managed = True
        db_table = 'focos_incendio_inpe'

'''
class Municipios(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    cd_mun = models.CharField(max_length=7, blank=True, null=True)
    nm_mun = models.CharField(max_length=60, blank=True, null=True)
    sigla_uf = models.CharField(max_length=2, blank=True, null=True)
    area_km2 = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.nm_mun + '/' + self.sigla_uf

    class Meta:
        managed = False
        db_table = 'municipios'


class Uf(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    cd_uf = models.CharField(max_length=2, blank=True, null=True)
    nm_uf = models.CharField(max_length=50, blank=True, null=True)
    sigla_uf = models.CharField(max_length=2, blank=True, null=True)
    nm_regiao = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nm_uf + '/' + self.sigla_uf

    class Meta:
        managed = False
        db_table = 'uf'
'''