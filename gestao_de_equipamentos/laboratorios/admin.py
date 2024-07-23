from django.contrib import admin

from laboratorios import models

@admin.register(models.Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
    
