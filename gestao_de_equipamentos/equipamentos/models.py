from django.db import models
import uuid

from helpers.slug import gerar_slug_dinamica
from helpers.model import get_object


from django.db import models
from laboratorios.models import Laboratorio
from tags.models import Tag
from usuarios.models import User


class Equipamento(models.Model):
    capa = models.ImageField(upload_to='equipamentos/capas')
    titulo = models.CharField(max_length=200, verbose_name='Nome')
    slug = models.SlugField(max_length=220, unique=True)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.PROTECT, related_name='lab')
    tags = models.ManyToManyField(Tag, related_name='equipamentos')
    total_eq = models.PositiveIntegerField(blank=True, null=True, verbose_name='Total de Equipamentos')
    equ_func = models.PositiveIntegerField(blank=True, null=True, verbose_name='Equipamentos Funcionados')
    equ_queb = models.PositiveIntegerField(blank=True, null=True, verbose_name='Equipamentos Quebrados')
    equ_em_manut = models.PositiveIntegerField(blank=True, null=True, verbose_name='Equipamentos em Manutenção')
    detalhar = models.BooleanField(default=False)
    conteudo = models.TextField(max_length=5000, null=True, blank=True, verbose_name='Definição')
    detal_equ_func = models.TextField(max_length=5000, null=True, blank=True, verbose_name='Detalhar Equipamentos Funcionados')
    detal_equ_queb = models.TextField(max_length=5000, null=True, blank=True, verbose_name='Detalhar Equipamentos Quebrados')
    detal_equ_em_manut = models.TextField(max_length=5000, null=True, blank=True, verbose_name='Detalhar Equipamentos em Manutenção')
    criado_em = models.DateTimeField(auto_now_add=True, editable=False)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ['-criado_em']
        constraints = [
            models.UniqueConstraint(fields=['titulo', 'laboratorio'], name='laboratorio e equipamento unicos')
            ]
        
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gerar_slug_dinamica(self, 'titulo')
        reg = get_object(self.__class__, pk=self.pk)  # type: ignore
        if reg and self.titulo != reg.titulo:
            self.slug = gerar_slug_dinamica(self, 'titulo')
        return super().save(*args, **kwargs)
    
    

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')
    parent_post = models.ForeignKey(Equipamento, on_delete=models.CASCADE, related_name='comments')
    body = models.CharField(max_length=150)
    status = models.BooleanField(null=True, default=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key = True, editable=False)

    def __str__(self):
        try:
            return f'{self.author.username} : {self.body[:30]}' 
        except:
            return f'no author : {self.body[:30]}' 
        
    class Meta:
        ordering = ['-created']
        
        
class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="replies")
    parent_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="replies")
    body = models.CharField(max_length=150)
    status = models.BooleanField(null=True, default=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        try:
            return f'{self.author.username} : {self.body[:30]}'
        except:
            return f'no author : {self.body[:30]}'

    class Meta:
        ordering = ['created']
        