from django.db import models

# Create your models here.
class companhias_abertas(models.Model):
    ROWID = models.IntegerField(primary_key=True)  # Se for uma chave primária única
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

    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = 'companhias_abertas'

