#from django.shortcuts import render
#from django.http import HttpResponse
#from functions import importar_dados
#from .models import companhias_abertas
# Create your views here.

#def visu(request):
 #   companhias = companhias_abertas.objects.all()  
  #  return render(request, 'companhias.html',{'companhias abertas': companhias})
#HttpResponse('Ola mundo')

from django.shortcuts import render
from django.http import HttpResponse
#from functions import importar_dados
from .models import companhias_abertas
from django_tables2 import RequestConfig
from .tables import companhias_abertasTable

def visu(request):
    queryset = companhias_abertas.objects.all()
    table = companhias_abertasTable(queryset)
    RequestConfig(request).configure(table)  # Configura paginação e ordenação
    return render(request, 'tabela.html', {'table': table})
# Create your views here.

#def visualizacao(request):
 #   companhias = companhias_abertas.objects.all()  
  #  return render(request, 'companhias_abertas.html',{'companhias abertas': companhias})
#HttpResponse('Ola mundo')

