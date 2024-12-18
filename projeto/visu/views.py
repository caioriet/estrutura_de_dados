from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.apps import apps
from django.forms import modelform_factory
from django_tables2 import RequestConfig
from .tables import companhias_abertasTable, declaracao_genero_2024Table, declaracao_raca_2024Table, faixa_etaria_2024Table
from .models import companhias_abertas, declaracao_genero_2024, declaracao_raca_2024, faixa_etaria_2024  # Importe os modelos também

def index(request):
    """
    Exibe a página inicial com opções para visualizar as tabelas.
    """
    tables = {
        'companhias_abertas': 'Companhias Abertas',
        'declaracao_genero_2024': 'Declaração de Gênero 2024',
        'declaracao_raca_2024': 'Declaração de Raça 2024',
        'faixa_etaria_2024': 'Faixa Etária 2024',
    }
    return render(request, 'index.html', {'tables': tables})

def index2(request):
    tables = {
        'companhias_abertas': 'Companhias Abertas',
        'declaracao_genero_2024': 'Declaração de Gênero 2024',
        'declaracao_raca_2024': 'Declaração de Raça 2024',
        'faixa_etaria_2024': 'Faixa Etária 2024',
    }
    models = {
        'companhias_abertas': 'Companhias Abertas',
        'declaracao_genero_2024': 'Declaração de Gênero 2024',
        'declaracao_raca_2024': 'Declaração de Raça 2024',
        'faixa_etaria_2024': 'Faixa Etária 2024',
    }
    return render(request, 'index2.html', {'tables': tables, 'models': models})

def visu(request):
    """
    Exibe a tabela selecionada pelo usuário.
    """
    table_name = request.GET.get('table', 'companhias_abertas')  # Pega o nome da tabela da URL, padrão é 'companhias_abertas'

    if table_name == 'companhias_abertas':
        queryset = companhias_abertas.objects.all()
        table = companhias_abertasTable(queryset)
    elif table_name == 'declaracao_genero_2024':
        queryset = declaracao_genero_2024.objects.all()
        table = declaracao_genero_2024Table(queryset)
    elif table_name == 'declaracao_raca_2024':
        queryset = declaracao_raca_2024.objects.all()
        table = declaracao_raca_2024Table(queryset)
    elif table_name == 'faixa_etaria_2024':
        queryset = faixa_etaria_2024.objects.all()
        table = faixa_etaria_2024Table(queryset)
    else:
        return HttpResponse("Tabela inválida")

    RequestConfig(request).configure(table)
    return render(request, 'tabela.html', {'table': table, 'table_name': table_name})

def get_model_and_table(model_name):
    model_names = {
        'companhias_abertas': (companhias_abertas, companhias_abertasTable),
        'declaracao_genero_2024': (declaracao_genero_2024, declaracao_genero_2024Table),
        'declaracao_raca_2024': (declaracao_raca_2024, declaracao_raca_2024Table),
        'faixa_etaria_2024': (faixa_etaria_2024, faixa_etaria_2024Table),
    }
    if model_name not in model_names:
        raise Http404("Modelo inválido")
    return model_names[model_name]

def list_view(request, model_name):
    model, table_class = get_model_and_table(model_name)
    queryset = model.objects.all()
    table = table_class(queryset)
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'list.html', {'table': table, 'model_name': model_name})

def create_view(request, model_name):
    model, _ = get_model_and_table(model_name)
    form_class = modelform_factory(model, fields='__all__')
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list', model_name=model_name)
    else:
        form = form_class()
    return render(request, 'form.html', {'form': form, 'model_name': model_name})

def detail_view(request, model_name, pk):
    model, _ = get_model_and_table(model_name)
    instance = get_object_or_404(model, pk=pk)
    fields = [(field.name, field.value_to_string(instance)) for field in model._meta.fields]
    return render(request, 'detail.html', {'instance': instance, 'model_name': model_name, 'fields': fields})

def update_view(request, model_name, pk):
    model, _ = get_model_and_table(model_name)
    instance = get_object_or_404(model, pk=pk)
    form_class = modelform_factory(model, fields='__all__')
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('list', model_name=model_name)
    else:
        form = form_class(instance=instance)
    return render(request, 'form.html', {'form': form, 'model_name': model_name})

def delete_view(request, model_name, pk):
    model, _ = get_model_and_table(model_name)
    instance = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        instance.delete()
        return redirect('list', model_name=model_name)
    return render(request, 'confirm_delete.html', {'instance': instance, 'model_name': model_name})

""" def visu(request):
    queryset = companhias_abertas.objects.all()
    table = companhias_abertasTable(queryset)
    RequestConfig(request).configure(table)  # Configura paginação e ordenação
    return render(request, 'tabela.html', {'table': table}) """
# Create your views here.

#def visualizacao(request):
 #   companhias = companhias_abertas.objects.all()  
  #  return render(request, 'companhias_abertas.html',{'companhias abertas': companhias})
#HttpResponse('Ola mundo')

