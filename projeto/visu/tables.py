import django_tables2 as tables
from .models import companhias_abertas, declaracao_genero_2024, declaracao_raca_2024, faixa_etaria_2024

class companhias_abertasTable(tables.Table):
    class Meta:
        model = companhias_abertas  # Baseia a tabela no modelo
        template_name = "django_tables2/bootstrap.html"  # Usar tema do Bootstrap
        primary_key = 'ROWID'

class declaracao_genero_2024Table(tables.Table):
    class Meta:
        model = declaracao_genero_2024  # Baseia a tabela no modelo
        template_name = "django_tables2/bootstrap.html"  # Usar tema do Bootstrap
        primary_key = 'id'

class declaracao_raca_2024Table(tables.Table):
    class Meta:
        model = declaracao_raca_2024  # Baseia a tabela no modelo
        template_name = "django_tables2/bootstrap.html"  # Usar tema do Bootstrap
        primary_key = 'id'

class faixa_etaria_2024Table(tables.Table):
    class Meta:
        model = faixa_etaria_2024  # Baseia a tabela no modelo
        template_name = "django_tables2/bootstrap.html"  # Usar tema do Bootstrap
        primary_key = 'id'


