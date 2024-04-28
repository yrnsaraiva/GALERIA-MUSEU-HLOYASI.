from django.contrib import admin
from .models import AudioVisual, Jornal, Revista, Pintura, Livro, ObjetoCultural

admin.site.site_header = 'Galeria Museu Hloyasi'
admin.site.site_title = 'Galeria Museu Hloyasi'

admin.site.register(AudioVisual)
admin.site.register(Jornal)


@admin.register(ObjetoCultural)
class ObjetoCulturalAdmin(admin.ModelAdmin):
    list_display = ('nome_da_obra', 'autor', 'descricao')


@admin.register(Revista)
class RevistaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'editora', 'data_publicacao', 'volume')


@admin.register(Pintura)
class PinturaAdmin(admin.ModelAdmin):
    list_display = ('titulo_da_obra', 'autor', 'data_de_criacao', 'tecnica', 'suporte')
    search_fields = ('titulo_da_obra', 'autor', 'data_de_criacao', 'tecnica', 'suporte')
    list_filter = ('autor', 'data_de_criacao', 'tecnica', 'suporte')


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'assunto', 'ano_edicao', 'exemplares_disponiveis')
    list_filter = ('assunto', 'ano_edicao', 'autor', 'lingua', 'local_edicao')
    search_fields = ('titulo', 'autor', 'assunto', 'ano_edicao', 'local_edicao', 'lingua')
