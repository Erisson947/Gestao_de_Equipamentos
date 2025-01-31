from django.contrib import admin

from pegar_chave import models

@admin.register(models.Chave)
class ChaveAdmin(admin.ModelAdmin):
    list_display = ['bloco_num']
    search_fields = ['bloco_num']
    
@admin.register(models.Pegar_Chave)
class PegarChaveAdmin(admin.ModelAdmin):
    list_display = ['chave', 'usuario']
    search_fields = ['chave', 'usuario']