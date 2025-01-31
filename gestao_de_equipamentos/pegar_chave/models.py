from django.db import models
from datetime import date

from helpers.slug import gerar_slug_dinamica
from helpers.model import get_object

from laboratorios.models import Laboratorio

from usuarios.models import User





class Chave(models.Model):
    SITUACAO_CHAVE = [
        ('em uso', 'Em Uso'),
        ('disponivel', 'Disponível'),
        ('atrasada', 'Atrasada'),
    ]
    
    bloco_num = models.CharField(max_length=3)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE, related_name='chave', blank=True, null=True, error_messages={'unique': 'O número de chave só pode pertencer a um laboratório!'})
    situacao = models.CharField(choices=SITUACAO_CHAVE, max_length=10, default='disponivel')
    campus = models.CharField(max_length=4, null=True, default=None)
    slug = models.SlugField(max_length=75, unique=True)
    criada_em = models.DateTimeField(auto_now_add=True, editable=False)
    atualizada_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bloco_num
    
    class Meta:
        ordering = ['-criada_em']
        constraints = [
            models.UniqueConstraint(fields=['bloco_num', 'campus'], name='nome da chave de sala comum único no Campus.')
            ]
        

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gerar_slug_dinamica(self, 'bloco_num')
        reg = get_object(self.__class__, pk=self.pk)  # type: ignore
        if reg and self.bloco_num != reg.bloco_num:
            self.slug = gerar_slug_dinamica(self, 'bloco_num')
        return super().save(*args, **kwargs)
    

class Pegar_Chave(models.Model):
    SITUACAO_CHAVE_PEGADA = [
        ('usando', 'Usando'),
        ('devolvida', 'Devolvida'),
        ('atrasada', 'Atrasada'),
    ]
    
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='chave_pegada')
    chave = models.ForeignKey(Chave, on_delete=models.DO_NOTHING, related_name='chave_pegada')
    situacao = models.CharField(max_length=20, default='usando')
    pegada_em = models.DateTimeField(auto_now_add=True, editable=False)
    tempo_max_devolucao = models.DateTimeField()
    campus = models.CharField(max_length=4, null=True, default=None)
    slug = models.SlugField(max_length=75, unique=True)
    atualizada_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.chave}-{self.usuario}'
    
    class Meta:
        ordering = ['-pegada_em']

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gerar_slug_dinamica(self, 'chave')
        reg = get_object(self.__class__, pk=self.pk)  # type: ignore
        if reg and self.chave != reg.chave:
            self.slug = gerar_slug_dinamica(self, 'chave')
        self.tempo_max_devolucao = f'{date.today()} 23:59:59'
        return super().save(*args, **kwargs)