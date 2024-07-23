from django.contrib import admin

from equipamentos import models




@admin.register(models.Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Reply)
class ReplyAdmin(admin.ModelAdmin):
    pass