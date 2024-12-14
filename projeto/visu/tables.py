import django_tables2 as tables
from .models import companhias_abertas

class companhias_abertasTable(tables.Table):
    class Meta:
        model = companhias_abertas  # Baseia a tabela no modelo
        template_name = "django_tables2/bootstrap.html"  # Usar tema do Bootstrap
