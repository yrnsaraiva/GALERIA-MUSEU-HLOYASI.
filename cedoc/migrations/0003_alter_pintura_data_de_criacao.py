# Generated by Django 5.0.3 on 2024-04-26 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cedoc', '0002_audiovisual_imagem_jornal_imagem_revista_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pintura',
            name='data_de_criacao',
            field=models.DateField(default='s.d.', null=True),
        ),
    ]
