# Generated by Django 4.0.4 on 2022-04-22 00:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoas',
            fields=[
                ('id_pessoa', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome_pessoa', models.CharField(max_length=255)),
                ('email_pessoa', models.CharField(max_length=255)),
                ('sexo_pessoa', models.CharField(max_length=25)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('situacao_ocupacional_pessoa', models.CharField(max_length=100)),
                ('data_cadastro', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
