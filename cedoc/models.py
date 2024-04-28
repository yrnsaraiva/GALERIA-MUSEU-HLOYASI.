from django.db import models


class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=100)
    assunto = models.CharField(max_length=30)
    numero_edicao = models.IntegerField()
    editor = models.CharField(max_length=100)
    ano_edicao = models.IntegerField()
    local_edicao = models.CharField(max_length=100)
    numero_paginas = models.IntegerField()
    tipo_paginacao = models.CharField(max_length=20, choices=[('normal', 'normal'), ('múltipla', 'múltipla')])
    encadernacao = models.CharField(max_length=25, choices=[('Encadernado', 'Encadernado'), ('Brochado', 'Brochado')])
    lingua = models.CharField(max_length=20)
    obs = models.TextField()
    imagem = models.ImageField(default='no-photo.svg', upload_to='livros')
    exemplares_disponiveis = models.IntegerField()
    localizacao = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Livro'  # Nome singular
        verbose_name_plural = 'Livros'  # Nome plural personalizado

    def __str__(self):
        return f'{self.titulo} - {self.autor}'


class Revista(models.Model):
    titulo = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    ISSN = models.CharField(max_length=20)
    data_publicacao = models.DateField()
    numero_edicao = models.IntegerField()
    volume = models.IntegerField()
    descricao = models.TextField()
    estado_de_conservacao = models.CharField(max_length=10, choices=[('Mau', 'Mau'), ('Razoável', 'Razoável'), ('Bom', 'Bom')])
    localizacao_atual = models.CharField(max_length=255)
    imagem = models.ImageField(default='no-photo.svg', upload_to='revistas')

    class Meta:
        verbose_name = 'Revista'  # Nome singular
        verbose_name_plural = 'Revistas'  # Nome plural personalizado

    def __str__(self):
        return self.titulo


class Jornal(models.Model):
    titulo = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    data_publicacao = models.DateField()
    numero_edicao = models.IntegerField()
    descricao = models.TextField()
    localizacao_atual = models.CharField(max_length=100)
    estado_de_conservacao = models.CharField(max_length=10, choices=[('Mau', 'Mau'), ('Razoável', 'Razoável'), ('Bom', 'Bom')])
    imagem = models.ImageField(default='no-photo.svg', upload_to='jornais')

    class Meta:
        verbose_name = 'Jornal'  # Nome singular
        verbose_name_plural = 'Jornais'  # Nome plural personalizado

    def __str__(self):
        return self.titulo


class Pintura(models.Model):
    titulo_da_obra = models.CharField(max_length=255)
    autor = models.CharField(max_length=100)
    data_de_criacao = models.CharField(max_length=20, default='s.d.', null=True)
    assinado = models.CharField(max_length=20, choices=[('sim', 'sim'), ('não', 'não')])
    dimensoes = models.CharField(max_length=50)
    tecnica = models.CharField(max_length=100, null=True)
    suporte = models.CharField(max_length=100, null=True)
    local_de_criacao = models.CharField(max_length=200, default='s.l.')
    proprietario = models.CharField(max_length=200, null=True)
    localizacao_atual = models.CharField(max_length=200)
    estado_de_conservacao = models.CharField(max_length=10, choices=[('Mau', 'Mau'), ('Razoável', 'Razoável'), ('Bom', 'Bom')])
    obs = models.TextField(null=True)
    direitos = models.TextField(default='A publicação, total ou parcial, deste documento exige prévia autorização da entidade detentora.')
    imagem = models.ImageField(default='no-photo.svg', upload_to='pinturas')

    class Meta:
        verbose_name = 'Pintura'  # Nome singular
        verbose_name_plural = 'Pinturas'  # Nome plural personalizado

    def __str__(self):
        return f'{self.titulo_da_obra} - {self.autor}'


class ObjetoCultural(models.Model):
    nome_da_obra = models.CharField(max_length=255)
    autor = models.CharField(max_length=100)
    caracteristicas_fisicas = models.TextField(null=True)
    assunto = models.CharField(max_length=100, null=True)
    materiais = models.CharField(max_length=255, null=True)
    dimensoes = models.CharField(max_length=50)
    local_de_criacao = models.CharField(max_length=200, default='s.l.')
    localizacao_atual = models.CharField(max_length=255)
    estado_de_conservacao = models.CharField(max_length=10, choices=[('Mau', 'Mau'), ('Razoável', 'Razoável'), ('Bom', 'Bom')])
    proprietario = models.CharField(max_length=100)
    descricao = models.TextField()
    obs = models.TextField()
    imagem = models.ImageField(default='no-photo.svg', upload_to='objetos_culturais')

    class Meta:
        verbose_name = 'Objeto Cultural'  # Nome singular
        verbose_name_plural = 'Objetos Culturais'  # Nome plural personalizado

    def __str__(self):
        return f'{self.nome_da_obra} - {self.autor}'


class AudioVisual(models.Model):
    titulo = models.CharField(max_length=255)
    direcao = models.CharField(max_length=100)
    premios = models.CharField(max_length=255)
    genero = models.CharField(max_length=40)
    local_de_lancamento = models.CharField(max_length=200, default='Mundial')
    data_de_lancamento = models.DateField()
    duracao = models.IntegerField()
    idioma = models.CharField(max_length=30)
    formato = models.CharField(max_length=30, choices=[('cassete', 'cassete'), ('fita magnética', 'fita magnética'),
                                                       ('DVD', 'DVD'), ('CD', 'CD')])
    classificacao_indicativa = models.CharField(max_length=30)
    localizacao_atual = models.CharField(max_length=255)
    descricao = models.TextField()
    imagem = models.ImageField(default='no-photo.svg', upload_to='audio_visuais')

    class Meta:
        verbose_name = 'Audio Visual'  # Nome singular
        verbose_name_plural = 'Audio Visuais'  # Nome plural personalizado

    def __str__(self):
        return f'{self.titulo} - {self.direcao}'
