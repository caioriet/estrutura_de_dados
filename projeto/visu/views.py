from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.apps import apps
from django.forms import modelform_factory
from django_tables2 import RequestConfig
from .tables import companhias_abertasTable, declaracao_genero_2024Table, declaracao_raca_2024Table, faixa_etaria_2024Table
from .models import companhias_abertas, declaracao_genero_2024, declaracao_raca_2024, faixa_etaria_2024  # Importe os modelos também
import pandas as pd

def index(request):
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
    return render(request, 'index.html', {'tables': tables, 'models': models})

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
    RequestConfig(request, paginate={'per_page': 20}).configure(table)
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

def dashboard(request):
    # Distribuição por Gênero
    genero_df = pd.DataFrame(list(declaracao_genero_2024.objects.all().values()))
    genero_data = {
        'Feminino': genero_df['quantidade_feminino'].sum(),
        'Masculino': genero_df['quantidade_masculino'].sum(),
        'Nao_Binario': genero_df['quantidade_nao_binario'].sum(),
        'Outros': genero_df['quantidade_outros'].sum(),
        'Sem_Resposta': genero_df['quantidade_sem_resposta'].sum()
    }

    # Distribuição por Raça
    raca_df = pd.DataFrame(list(declaracao_raca_2024.objects.all().values()))
    raca_data = {
        'Amarelo': raca_df['quantidade_amarelo'].sum(),
        'Branco': raca_df['quantidade_branco'].sum(),
        'Preto': raca_df['quantidade_preto'].sum(),
        'Pardo': raca_df['quantidade_pardo'].sum(),
        'Indigena': raca_df['quantidade_indigena'].sum(),
        'Outros': raca_df['quantidade_outros'].sum(),
        'Sem_Resposta': raca_df['quantidade_sem_resposta'].sum()
    }

    # Distribuição por Faixa Etária
    faixa_etaria_df = pd.DataFrame(list(faixa_etaria_2024.objects.all().values()))
    faixa_etaria_data = {
        'Ate_30': faixa_etaria_df['quantidade_ate30anos'].sum(),
        'Entre_30_50': faixa_etaria_df['quantidade_30a50anos'].sum(),
        'Acima_50': faixa_etaria_df['quantidade_acima50anos'].sum()
    }

    context = {
        'genero_data': genero_data,
        'raca_data': raca_data,
        'faixa_etaria_data': faixa_etaria_data,
    }

    return render(request, 'dashboard.html', context)