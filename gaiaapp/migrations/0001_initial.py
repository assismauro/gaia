# Generated by Django 3.2.3 on 2021-05-30 19:00

import datetime
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlertasFlorestas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('datahora', models.CharField(blank=True, max_length=80, null=True)),
                ('satelite', models.CharField(blank=True, max_length=80, null=True)),
                ('pais', models.CharField(blank=True, max_length=80, null=True)),
                ('estado', models.CharField(blank=True, max_length=80, null=True)),
                ('municipio', models.CharField(blank=True, max_length=80, null=True)),
                ('bioma', models.CharField(blank=True, max_length=50, null=True)),
                ('diasemchuv', models.IntegerField(blank=True, null=True)),
                ('precipitac', models.DecimalField(blank=True, decimal_places=8, max_digits=20, null=True)),
                ('riscofogo', models.DecimalField(blank=True, decimal_places=8, max_digits=20, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=8, max_digits=20, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=8, max_digits=20, null=True)),
                ('frp', models.DecimalField(blank=True, decimal_places=8, max_digits=20, null=True)),
                ('cnfp_id', models.IntegerField(blank=True, null=True)),
                ('objectid', models.BigIntegerField(blank=True, null=True)),
                ('nome', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nome')),
                ('orgao', models.CharField(blank=True, max_length=100, null=True)),
                ('classe', models.CharField(blank=True, max_length=30, null=True)),
                ('estagio', models.CharField(blank=True, max_length=30, null=True)),
                ('governo', models.CharField(blank=True, max_length=20, null=True)),
                ('codigo', models.CharField(blank=True, max_length=30, null=True)),
                ('ano', models.BigIntegerField(blank=True, null=True)),
                ('uf', models.CharField(blank=True, max_length=4, null=True)),
                ('protecao', models.CharField(blank=True, max_length=30, null=True)),
                ('tipo', models.CharField(blank=True, max_length=40, null=True)),
                ('comunitari', models.CharField(blank=True, max_length=6, null=True)),
                ('atolegal', models.CharField(blank=True, max_length=100, null=True)),
                ('anocriacao', models.BigIntegerField(blank=True, null=True)),
                ('categoria', models.CharField(blank=True, max_length=40, null=True)),
                ('observacao', models.CharField(blank=True, max_length=200, null=True)),
                ('sobreposic', models.CharField(blank=True, max_length=3, null=True)),
                ('area_ha', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Alerta Floresta',
                'verbose_name_plural': 'Alertas Florestas',
                'db_table': 'alertas_florestas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Cnfp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
                ('objectid', models.BigIntegerField(blank=True, null=True)),
                ('nome', models.CharField(blank=True, max_length=200, null=True)),
                ('orgao', models.CharField(blank=True, max_length=100, null=True)),
                ('classe', models.CharField(blank=True, max_length=30, null=True)),
                ('estagio', models.CharField(blank=True, max_length=30, null=True)),
                ('governo', models.CharField(blank=True, max_length=20, null=True)),
                ('codigo', models.CharField(blank=True, max_length=30, null=True)),
                ('ano', models.BigIntegerField(blank=True, null=True)),
                ('uf', models.CharField(blank=True, max_length=4, null=True)),
                ('protecao', models.CharField(blank=True, max_length=30, null=True)),
                ('tipo', models.CharField(blank=True, max_length=40, null=True)),
                ('comunitari', models.CharField(blank=True, max_length=6, null=True)),
                ('atolegal', models.CharField(blank=True, max_length=100, null=True)),
                ('anocriacao', models.BigIntegerField(blank=True, null=True)),
                ('categoria', models.CharField(blank=True, max_length=40, null=True)),
                ('observacao', models.CharField(blank=True, max_length=200, null=True)),
                ('sobreposic', models.CharField(blank=True, max_length=3, null=True)),
                ('bioma', models.CharField(blank=True, max_length=50, null=True)),
                ('shape_leng', models.FloatField(blank=True, null=True)),
                ('shape_area', models.FloatField(blank=True, null=True)),
                ('area_ha', models.BigIntegerField(blank=True, null=True)),
                ('layer', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Cadastro Nacional de Florestas Públicas',
                'db_table': 'cnfp',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EmailsMP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uf', models.CharField(blank=True, max_length=200, null=True, verbose_name='UF')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'E-mail Ministério Público',
                'verbose_name_plural': 'E-mails Ministério Público',
                'db_table': 'email_mp',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='FocosIncendioInpe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('datahora', models.CharField(blank=True, max_length=80, null=True)),
                ('satelite', models.CharField(blank=True, max_length=80, null=True)),
                ('pais', models.CharField(blank=True, max_length=80, null=True)),
                ('estado', models.CharField(blank=True, max_length=80, null=True)),
                ('municipio', models.CharField(blank=True, max_length=80, null=True)),
                ('bioma', models.CharField(blank=True, max_length=80, null=True)),
                ('diasemchuv', models.IntegerField(blank=True, null=True)),
                ('precipitac', models.DecimalField(blank=True, decimal_places=8, max_digits=20, null=True)),
                ('riscofogo', models.DecimalField(blank=True, decimal_places=8, max_digits=20, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=8, max_digits=20, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=8, max_digits=20, null=True)),
                ('frp', models.DecimalField(blank=True, decimal_places=8, max_digits=20, null=True)),
                ('cnfp_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'focos_incendio_inpe',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TiposPenais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_penal', models.CharField(max_length=50, verbose_name='Tipo Penal')),
                ('lei', models.CharField(max_length=50, verbose_name='Lei')),
                ('descricao', models.TextField(verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Tipo Penais',
                'verbose_name_plural': 'Tipos Penais',
                'db_table': 'tipo_penal',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NoticiaCrime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(blank=True, max_length=254)),
                ('url_doc', models.URLField(blank=True, max_length=256, verbose_name='Endereço Documento Complementar')),
                ('data_documento', models.DateTimeField(default=datetime.datetime.now, verbose_name='Data/Hora documento')),
                ('documento', models.FileField(upload_to='', verbose_name='Noticia Crime')),
                ('alerta_florestal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gaiaapp.alertasflorestas')),
                ('email_mp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gaiaapp.emailsmp', verbose_name='E-mail do Ministério Público')),
                ('tipo_penal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gaiaapp.tipospenais')),
            ],
            options={
                'verbose_name': 'Notícia Crime',
                'verbose_name_plural': 'Notícias-Crime',
                'db_table': 'noticia_crime',
                'managed': True,
            },
        ),
    ]