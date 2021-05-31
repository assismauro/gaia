from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from django.core.serializers import serialize
from gaiaapp.models import AlertasFlorestas
from django.template.context import Context
from django.urls import reverse


def alerta_florestas_dataset(request):
    alerta_florestas = serialize('geojson', AlertasFlorestas.objects.all())
    return HttpResponse(alerta_florestas, content_type='json')


# Create your views here.

from gaiaapp.forms import docForm


def createDoc(request, pk):
    alertas_florestas = get_object_or_404(AlertasFlorestas, pk=pk)
    if request == 'POST':
        form = docForm(request.POST)
        if form.is_valid():
            print()
            return HttpResponseRedirect(reverse('/'))
    else:
        name = " Teste"
        form = docForm(initial={"name": name})
    context = {
        ' form': form,
        'alertas_florestas': alertas_florestas
    }
    return render(request, 'gaiaapp/createDoc.html', context)
