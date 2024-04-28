from django.shortcuts import render
from .models import Pintura
from django.db.models import Q


def index(request):
    query = request.GET.get('q', '')
    pinturas = []

    if query:
        pinturas = Pintura.objects.filter(
            Q(titulo_da_obra__icontains=query) |
            Q(autor__icontains=query) |
            Q(tecnica__icontains=query) |
            Q(suporte__icontains=query) |
            Q(obs__icontains=query) |
            Q(proprietario__icontains=query)
        )
        pinturas_amostra = []
    else:
        pinturas_amostra = Pintura.objects.all()

    context = {'pinturas': pinturas, 'query': query, 'pinturas_amostra': pinturas_amostra}

    return render(request, 'cedoc/index.html', context)


def details(request, pk):
    pintura = Pintura.objects.get(id=pk)
    context = {'pintura': pintura, 'pk': pk}

    return render(request, 'cedoc/details.html', context)