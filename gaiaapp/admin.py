from django.conf.urls import url
from django.contrib import admin
from gaiaapp.models import AlertasFlorestas
from gaiaapp.models import Cnfp
from gaiaapp.models import NoticiaCrime
from gaiaapp.models import EmailsMP
from gaiaapp.models import TiposPenais
from django.utils.html import format_html

admin.site.register(AlertasFlorestas)
admin.site.register(Cnfp)
admin.site.register(NoticiaCrime)
admin.site.register(TiposPenais)
admin.site.register(EmailsMP)


