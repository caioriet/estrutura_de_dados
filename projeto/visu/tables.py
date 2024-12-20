import django_tables2 as tables
from .models import companhias_abertas, declaracao_genero_2024, declaracao_raca_2024, faixa_etaria_2024

class companhias_abertasTable(tables.Table):
    acoes = tables.TemplateColumn(
        template_code='<a href="{% url \'detail\' model_name=model_name pk=record.pk %}">Detalhes</a> | <a href="{% url \'update\' model_name=model_name pk=record.pk %}">Editar</a> | <a href="{% url \'delete\' model_name=model_name pk=record.pk %}">Excluir</a>',
        verbose_name="Ações"
    )
    class Meta:
        model = companhias_abertas  # Baseia a tabela no modelo
        template_name = "django_tables2/bootstrap.html"  # Usar tema do Bootstrap
        primary_key = 'id'

class declaracao_genero_2024Table(tables.Table):
    acoes = tables.TemplateColumn(
        template_code='<a href="{% url \'detail\' model_name=model_name pk=record.pk %}">Detalhes</a> | <a href="{% url \'update\' model_name=model_name pk=record.pk %}">Editar</a> | <a href="{% url \'delete\' model_name=model_name pk=record.pk %}">Excluir</a>',
        verbose_name="Ações"
    )
    class Meta:
        model = declaracao_genero_2024  # Baseia a tabela no modelo
        template_name = "django_tables2/bootstrap.html"  # Usar tema do Bootstrap
        primary_key = 'id'

class declaracao_raca_2024Table(tables.Table):
    acoes = tables.TemplateColumn(
        template_code='<a href="{% url \'detail\' model_name=model_name pk=record.pk %}">Detalhes</a> | <a href="{% url \'update\' model_name=model_name pk=record.pk %}">Editar</a> | <a href="{% url \'delete\' model_name=model_name pk=record.pk %}">Excluir</a>',
        verbose_name="Ações"
    )
    class Meta:
        model = declaracao_raca_2024  # Baseia a tabela no modelo
        template_name = "django_tables2/bootstrap.html"  # Usar tema do Bootstrap
        primary_key = 'id'

class faixa_etaria_2024Table(tables.Table):    
    acoes = tables.TemplateColumn(
        template_code='<a href="{% url \'detail\' model_name=model_name pk=record.pk %}">Detalhes</a> | <a href="{% url \'update\' model_name=model_name pk=record.pk %}">Editar</a> | <a href="{% url \'delete\' model_name=model_name pk=record.pk %}">Excluir</a>',
        verbose_name="Ações"
    )
    class Meta:
        model = faixa_etaria_2024  # Baseia a tabela no modelo
        template_name = "django_tables2/bootstrap.html"  # Usar tema do Bootstrap
        primary_key = 'id'


