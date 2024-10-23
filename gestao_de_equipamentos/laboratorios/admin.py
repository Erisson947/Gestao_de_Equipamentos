from django.contrib import admin

from laboratorios import models

@admin.register(models.Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
    
@admin.register(models.Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
    
@admin.register(models.Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ['descrição']
    search_fields = ['descrição']
    
@admin.register(models.Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
    
@admin.register(models.Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['descrição']
    search_fields = ['descrição']
    
@admin.register(models.Horario_aula)
class Horario_aulaAdmin(admin.ModelAdmin):
    list_display = ['disciplina']
    search_fields = ['disciplina']
    
@admin.register(models.Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['titulo']
    search_fields = ['titulo']
    
@admin.register(models.Agenda_lab)
class Agenda_labAdmin(admin.ModelAdmin):
    list_display = ['titulo']
    search_fields = ['titulo']
    
