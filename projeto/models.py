# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CompanhiasAbertas(models.Model):
    cnpj_cia = models.TextField(db_column='CNPJ_CIA', blank=True, null=True)  # Field name made lowercase.
    denom_social = models.TextField(db_column='DENOM_SOCIAL', blank=True, null=True)  # Field name made lowercase.
    denom_comerc = models.TextField(db_column='DENOM_COMERC', blank=True, null=True)  # Field name made lowercase.
    dt_reg = models.TextField(db_column='DT_REG', blank=True, null=True)  # Field name made lowercase.
    dt_const = models.TextField(db_column='DT_CONST', blank=True, null=True)  # Field name made lowercase.
    dt_cancel = models.TextField(db_column='DT_CANCEL', blank=True, null=True)  # Field name made lowercase.
    motivo_cancel = models.TextField(db_column='MOTIVO_CANCEL', blank=True, null=True)  # Field name made lowercase.
    sit = models.TextField(db_column='SIT', blank=True, null=True)  # Field name made lowercase.
    dt_ini_sit = models.TextField(db_column='DT_INI_SIT', blank=True, null=True)  # Field name made lowercase.
    cd_cvm = models.IntegerField(db_column='CD_CVM', blank=True, null=True)  # Field name made lowercase.
    setor_ativ = models.TextField(db_column='SETOR_ATIV', blank=True, null=True)  # Field name made lowercase.
    tp_merc = models.TextField(db_column='TP_MERC', blank=True, null=True)  # Field name made lowercase.
    categ_reg = models.TextField(db_column='CATEG_REG', blank=True, null=True)  # Field name made lowercase.
    dt_ini_categ = models.TextField(db_column='DT_INI_CATEG', blank=True, null=True)  # Field name made lowercase.
    sit_emissor = models.TextField(db_column='SIT_EMISSOR', blank=True, null=True)  # Field name made lowercase.
    dt_ini_sit_emissor = models.TextField(db_column='DT_INI_SIT_EMISSOR', blank=True, null=True)  # Field name made lowercase.
    controle_acionario = models.TextField(db_column='CONTROLE_ACIONARIO', blank=True, null=True)  # Field name made lowercase.
    tp_ender = models.TextField(db_column='TP_ENDER', blank=True, null=True)  # Field name made lowercase.
    logradouro = models.TextField(db_column='LOGRADOURO', blank=True, null=True)  # Field name made lowercase.
    compl = models.TextField(db_column='COMPL', blank=True, null=True)  # Field name made lowercase.
    bairro = models.TextField(db_column='BAIRRO', blank=True, null=True)  # Field name made lowercase.
    mun = models.TextField(db_column='MUN', blank=True, null=True)  # Field name made lowercase.
    uf = models.TextField(db_column='UF', blank=True, null=True)  # Field name made lowercase.
    pais = models.TextField(db_column='PAIS', blank=True, null=True)  # Field name made lowercase.
    cep = models.FloatField(db_column='CEP', blank=True, null=True)  # Field name made lowercase.
    ddd_tel = models.FloatField(db_column='DDD_TEL', blank=True, null=True)  # Field name made lowercase.
    tel = models.FloatField(db_column='TEL', blank=True, null=True)  # Field name made lowercase.
    ddd_fax = models.FloatField(db_column='DDD_FAX', blank=True, null=True)  # Field name made lowercase.
    fax = models.FloatField(db_column='FAX', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='EMAIL', blank=True, null=True)  # Field name made lowercase.
    tp_resp = models.TextField(db_column='TP_RESP', blank=True, null=True)  # Field name made lowercase.
    resp = models.TextField(db_column='RESP', blank=True, null=True)  # Field name made lowercase.
    dt_ini_resp = models.TextField(db_column='DT_INI_RESP', blank=True, null=True)  # Field name made lowercase.
    logradouro_resp = models.TextField(db_column='LOGRADOURO_RESP', blank=True, null=True)  # Field name made lowercase.
    compl_resp = models.TextField(db_column='COMPL_RESP', blank=True, null=True)  # Field name made lowercase.
    bairro_resp = models.TextField(db_column='BAIRRO_RESP', blank=True, null=True)  # Field name made lowercase.
    mun_resp = models.TextField(db_column='MUN_RESP', blank=True, null=True)  # Field name made lowercase.
    uf_resp = models.TextField(db_column='UF_RESP', blank=True, null=True)  # Field name made lowercase.
    pais_resp = models.TextField(db_column='PAIS_RESP', blank=True, null=True)  # Field name made lowercase.
    cep_resp = models.FloatField(db_column='CEP_RESP', blank=True, null=True)  # Field name made lowercase.
    ddd_tel_resp = models.TextField(db_column='DDD_TEL_RESP', blank=True, null=True)  # Field name made lowercase.
    tel_resp = models.FloatField(db_column='TEL_RESP', blank=True, null=True)  # Field name made lowercase.
    ddd_fax_resp = models.FloatField(db_column='DDD_FAX_RESP', blank=True, null=True)  # Field name made lowercase.
    fax_resp = models.FloatField(db_column='FAX_RESP', blank=True, null=True)  # Field name made lowercase.
    email_resp = models.TextField(db_column='EMAIL_RESP', blank=True, null=True)  # Field name made lowercase.
    cnpj_auditor = models.TextField(db_column='CNPJ_AUDITOR', blank=True, null=True)  # Field name made lowercase.
    auditor = models.TextField(db_column='AUDITOR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'companhias_abertas'


class DeclaracaoGenero2024(models.Model):
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
        managed = False
        db_table = 'declaracao_genero_2024'


class DeclaracaoRaca2024(models.Model):
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
        managed = False
        db_table = 'declaracao_raca_2024'


class FaixaEtaria2024(models.Model):
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
