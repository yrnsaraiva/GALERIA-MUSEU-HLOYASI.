# Generated by Django 5.0.3 on 2024-04-18 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioVisual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('direcao', models.CharField(max_length=100)),
                ('premios', models.CharField(max_length=255)),
                ('genero', models.CharField(max_length=40)),
                ('local_de_lancamento', models.CharField(default='Mundial', max_length=200)),
                ('data_de_lancamento', models.DateField()),
                ('duracao', models.IntegerField()),
                ('idioma', models.CharField(max_length=30)),
                ('formato', models.CharField(choices=[('cassete', 'cassete'), ('fita magnética', 'fita magnética'), ('DVD', 'DVD'), ('CD', 'CD')], max_length=30)),
                ('classificacao_indicativa', models.CharField(max_length=30)),
                ('localizacao_atual', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
            ],
            options={
                'verbose_name': 'Audio Visual',
                'verbose_name_plural': 'Audio Visuais',
            },
        ),
        migrations.CreateModel(
            name='Jornal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('editora', models.CharField(max_length=100)),
                ('data_publicacao', models.DateField()),
                ('numero_edicao', models.IntegerField()),
                ('descricao', models.TextField()),
                ('localizacao_atual', models.CharField(max_length=100)),
                ('estado_de_conservacao', models.CharField(choices=[('Mau', 'Mau'), ('Razoável', 'Razoável'), ('Bom', 'Bom')], max_length=10)),
            ],
            options={
                'verbose_name': 'Jornal',
                'verbose_name_plural': 'Jornais',
            },
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('autor', models.CharField(max_length=100)),
                ('assunto', models.CharField(max_length=30)),
                ('numero_edicao', models.IntegerField()),
                ('editor', models.CharField(max_length=100)),
                ('ano_edicao', models.IntegerField()),
                ('local_edicao', models.CharField(max_length=100)),
                ('numero_paginas', models.IntegerField()),
                ('tipo_paginacao', models.CharField(choices=[('normal', 'normal'), ('múltipla', 'múltipla')], max_length=20)),
                ('encadernacao', models.CharField(choices=[('Encadernado', 'Encadernado'), ('Brochado', 'Brochado')], max_length=25)),
                ('lingua', models.CharField(max_length=20)),
                ('obs', models.TextField()),
                ('imagem', models.ImageField(default='no-photo.svg', upload_to='static/images/livros')),
                ('exemplares_disponiveis', models.IntegerField()),
                ('localizacao', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Livro',
                'verbose_name_plural': 'Livros',
            },
        ),
        migrations.CreateModel(
            name='ObjetoCultural',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_da_obra', models.CharField(max_length=255)),
                ('autor', models.CharField(max_length=100)),
                ('caracteristicas_fisicas', models.TextField()),
                ('assunto', models.CharField(max_length=100)),
                ('materiais', models.CharField(max_length=255)),
                ('dimensoes', models.CharField(max_length=50)),
                ('local_de_criacao', models.CharField(max_length=200)),
                ('localizacao_atual', models.CharField(max_length=255)),
                ('estado_de_conservacao', models.CharField(choices=[('Mau', 'Mau'), ('Razoável', 'Razoável'), ('Bom', 'Bom')], max_length=10)),
                ('proprietario', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('obs', models.TextField()),
                ('imagem', models.ImageField(default='no-photo.svg', upload_to='static/images/objetos_culturais')),
            ],
            options={
                'verbose_name': 'Objeto Cultural',
                'verbose_name_plural': 'Objetos Culturais',
            },
        ),
        migrations.CreateModel(
            name='Pintura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_da_obra', models.CharField(max_length=255)),
                ('autor', models.CharField(max_length=100)),
                ('data_de_criacao', models.DateField(default='s.d.')),
                ('assinado', models.CharField(choices=[('sim', 'sim'), ('não', 'não')], max_length=20)),
                ('dimensoes', models.CharField(max_length=50)),
                ('tecnica', models.CharField(max_length=100)),
                ('suporte', models.CharField(max_length=100)),
                ('local_de_criacao', models.CharField(max_length=200)),
                ('proprietario', models.CharField(max_length=200)),
                ('localizacao_atual', models.CharField(max_length=200)),
                ('estado_de_conservacao', models.CharField(choices=[('Mau', 'Mau'), ('Razoável', 'Razoável'), ('Bom', 'Bom')], max_length=10)),
                ('obs', models.TextField()),
                ('direitos', models.TextField(default='A publicação, total ou parcial, deste documento exige prévia autorização da entidade detentora.')),
                ('imagem', models.ImageField(default='no-photo.svg', upload_to='static/images/pinturas')),
            ],
            options={
                'verbose_name': 'Pintura',
                'verbose_name_plural': 'Pinturas',
            },
        ),
        migrations.CreateModel(
            name='Revista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('editora', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=100)),
                ('ISSN', models.CharField(max_length=20)),
                ('data_publicacao', models.DateField()),
                ('numero_edicao', models.IntegerField()),
                ('volume', models.IntegerField()),
                ('descricao', models.TextField()),
                ('estado_de_conservacao', models.CharField(choices=[('Mau', 'Mau'), ('Razoável', 'Razoável'), ('Bom', 'Bom')], max_length=10)),
                ('localizacao_atual', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Revista',
                'verbose_name_plural': 'Revistas',
            },
        ),
    ]
