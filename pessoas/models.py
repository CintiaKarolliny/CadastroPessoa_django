from django.db import models
from uuid import uuid4

# Create your models here.

class Pessoas(models.Model):
    id_pessoa = models.UUIDField(
        primary_key = True,
        default = uuid4,
        editable = False
    )
    nome_pessoa = models.CharField(max_length = 255)
    email_pessoa = models.CharField(max_length = 255)
    sexo_pessoa = models.CharField(max_length = 25)
    data_nascimento = models.DateField(null=True, blank=True)
    situacao_ocupacional_pessoa = models.CharField(max_length = 100)
    data_cadastro = models.DateField(auto_now_add = True)
