from django.db import models

# Create your models here.
class companhias_abertas(models.Model):
    id = models.IntegerField(primary_key=True)
    ROWID = models.IntegerField()  # Se for uma chave primária única
    CNPJ_CIA = models.CharField(max_length=14)
    DENOM_SOCIAL = models.CharField(max_length=255)
    DENOM_COMERC = models.CharField(max_length=255)
    DT_REG = models.DateField()
    DT_CONST = models.DateField()
    DT_CANCEL = models.DateField(null=True, blank=True)  # Assuming cancellation is optional
    MOTIVO_CANCEL = models.CharField(max_length=255, null=True, blank=True)
    SIT = models.CharField(max_length=255)
    DT_INI_SIT = models.DateField()
    CD_CVM = models.CharField(max_length=255)
    SETOR_ATIV = models.CharField(max_length=255)
    TP_MERC = models.CharField(max_length=255)
    CATEG_REG = models.CharField(max_length=255)
    DT_INI_CATEG = models.DateField()
    SIT_EMISSOR = models.CharField(max_length=255)
    DT_INI_SIT_EMISSOR = models.DateField()
    CONTROLE_ACIONARIO = models.CharField(max_length=255)
    TP_ENDER = models.CharField(max_length=255)
    LOGRADOURO = models.CharField(max_length=255)
    COMPL = models.CharField(max_length=255)
    BAIRRO = models.CharField(max_length=255)
    MUN = models.CharField(max_length=255)
    UF = models.CharField(max_length=2)
    PAIS = models.CharField(max_length=255)
    CEP = models.CharField(max_length=8)
    DDD_TEL = models.CharField(max_length=2)
    TEL = models.CharField(max_length=10)
    DDD_FAX = models.CharField(max_length=2)
    FAX = models.CharField(max_length=10)
    EMAIL = models.EmailField()
    TP_RESP = models.CharField(max_length=255)
    RESP = models.CharField(max_length=255)
    DT_INI_RESP = models.DateField()
    LOGRADOURO_RESP = models.CharField(max_length=255)
    COMPL_RESP = models.CharField(max_length=255)
    BAIRRO_RESP = models.CharField(max_length=255)
    MUN_RESP = models.CharField(max_length=255)
    UF_RESP = models.CharField(max_length=2)
    PAIS_RESP = models.CharField(max_length=255)
    CEP_RESP = models.CharField(max_length=8)
    DDD_TEL_RESP = models.CharField(max_length=2)
    TEL_RESP = models.CharField(max_length=10)
    DDD_FAX_RESP = models.CharField(max_length=2)
    FAX_RESP = models.CharField(max_length=10)
    EMAIL_RESP = models.EmailField()
    CNPJ_AUDITOR = models.CharField(max_length=14)
    AUDITOR = models.CharField(max_length=255)

    class Meta:
        db_table = 'companhias_abertas'

    def __str__(self):
        return self.CNPJ_CIA

class declaracao_genero_2024(models.Model):
    id = models.IntegerField(primary_key=True)
    cnpj_companhia = models.TextField(db_column='CNPJ_Companhia', blank=True, null=True)  # Field name made lowercase.
    data_referencia = models.TextField(db_column='Data_Referencia', blank=True, null=True)  # Field name made lowercase.
    versao = models.IntegerField(db_column='Versao', blank=True, null=True)  # Field name made lowercase.
    id_documento = models.IntegerField(db_column='ID_Documento', blank=True, null=True)  # Field name made lowercase.
    nome_companhia = models.TextField(db_column='Nome_Companhia', blank=True, null=True)  # Field name made lowercase.
    local = models.TextField(db_column='Local', blank=True, null=True)  # Field name made lowercase.
    quantidade_feminino = models.IntegerField(db_column='Quantidade_Feminino', blank=True, null=True)  # Field name made lowercase.
    quantidade_masculino = models.IntegerField(db_column='Quantidade_Masculino', blank=True, null=True)  # Field name made lowercase.
    quantidade_nao_binario = models.IntegerField(db_column='Quantidade_Nao_Binario', blank=True, null=True)  # Field name made lowercase.
    quantidade_outros = models.IntegerField(db_column='Quantidade_Outros', blank=True, null=True)  # Field name made lowercase.
    quantidade_sem_resposta = models.IntegerField(db_column='Quantidade_Sem_Resposta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'declaracao_genero_2024'

    def __str__(self):
        return self.cnpj_companhia

class declaracao_raca_2024(models.Model):
    id = models.IntegerField(primary_key=True)
    cnpj_companhia = models.TextField(db_column='CNPJ_Companhia', blank=True, null=True)  # Field name made lowercase.
    data_referencia = models.TextField(db_column='Data_Referencia', blank=True, null=True)  # Field name made lowercase.
    versao = models.IntegerField(db_column='Versao', blank=True, null=True)  # Field name made lowercase.
    id_documento = models.IntegerField(db_column='ID_Documento', blank=True, null=True)  # Field name made lowercase.
    nome_companhia = models.TextField(db_column='Nome_Companhia', blank=True, null=True)  # Field name made lowercase.
    local = models.TextField(db_column='Local', blank=True, null=True)  # Field name made lowercase.
    quantidade_amarelo = models.IntegerField(db_column='Quantidade_Amarelo', blank=True, null=True)  # Field name made lowercase.
    quantidade_branco = models.IntegerField(db_column='Quantidade_Branco', blank=True, null=True)  # Field name made lowercase.
    quantidade_preto = models.IntegerField(db_column='Quantidade_Preto', blank=True, null=True)  # Field name made lowercase.
    quantidade_pardo = models.IntegerField(db_column='Quantidade_Pardo', blank=True, null=True)  # Field name made lowercase.
    quantidade_indigena = models.IntegerField(db_column='Quantidade_Indigena', blank=True, null=True)  # Field name made lowercase.
    quantidade_outros = models.IntegerField(db_column='Quantidade_Outros', blank=True, null=True)  # Field name made lowercase.
    quantidade_sem_resposta = models.IntegerField(db_column='Quantidade_Sem_Resposta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'declaracao_raca_2024'

    def __str__(self):
        return self.cnpj_companhia

class faixa_etaria_2024(models.Model):
    id = models.IntegerField(primary_key=True)
    cnpj_companhia = models.TextField(db_column='CNPJ_Companhia', blank=True, null=True)  # Field name made lowercase.
    data_referencia = models.TextField(db_column='Data_Referencia', blank=True, null=True)  # Field name made lowercase.
    versao = models.IntegerField(db_column='Versao', blank=True, null=True)  # Field name made lowercase.
    id_documento = models.IntegerField(db_column='ID_Documento', blank=True, null=True)  # Field name made lowercase.
    nome_companhia = models.TextField(db_column='Nome_Companhia', blank=True, null=True)  # Field name made lowercase.
    local = models.TextField(db_column='Local', blank=True, null=True)  # Field name made lowercase.
    quantidade_ate30anos = models.IntegerField(db_column='Quantidade_Ate30Anos', blank=True, null=True)  # Field name made lowercase.
    quantidade_30a50anos = models.IntegerField(db_column='Quantidade_30a50Anos', blank=True, null=True)  # Field name made lowercase.
    quantidade_acima50anos = models.IntegerField(db_column='Quantidade_Acima50Anos', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'faixa_etaria_2024'

    def __str__(self):
        return self.cnpj_companhia