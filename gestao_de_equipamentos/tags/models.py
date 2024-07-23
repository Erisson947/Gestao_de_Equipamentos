from django.db import models


from helpers.slug import gerar_slug_dinamica
from helpers.model import get_object

from django.db import models



class Tag(models.Model):
    capa = models.ImageField(upload_to='tags/icons/')
    nome = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=75, unique=True)
    criada_em = models.DateTimeField(auto_now_add=True, editable=False)
    atualizada_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['-criada_em']

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gerar_slug_dinamica(self, 'nome')
        reg = get_object(self.__class__, pk=self.pk)  # type: ignore
        if reg and self.nome != reg.nome:
            self.slug = gerar_slug_dinamica(self, 'nome')
        return super().save(*args, **kwargs)
    

