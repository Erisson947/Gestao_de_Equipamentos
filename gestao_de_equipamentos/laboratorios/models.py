from django.db import models

from helpers.slug import gerar_slug_dinamica
from helpers.model import get_object

from django.db import models

class Laboratorio(models.Model):
    nome = models.CharField(max_length=100)
    campus = models.CharField(max_length=4, null=True, default=None,)
    slug = models.SlugField(max_length=220, unique=True)
    criado_em = models.DateTimeField(auto_now_add=True, editable=False)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['-criado_em']
        constraints = [
            models.UniqueConstraint(fields=['nome', 'campus'], name='nome do laboratorio e campus unicos')
            ]
        

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gerar_slug_dinamica(self, 'nome')
        reg = get_object(self.__class__, pk=self.pk)  # type: ignore
        if reg and self.nome != reg.nome:
            self.slug = gerar_slug_dinamica(self, 'nome')
        return super().save(*args, **kwargs)