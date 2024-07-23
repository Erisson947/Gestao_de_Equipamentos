from django import forms
from string import punctuation

from django.utils.translation import gettext_lazy as _

from tags import models


class TagForm(forms.ModelForm):
    required_css_class = 'required'
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    class Meta:
        model = models.Tag
        fields = ['nome', 'capa']

    capa = forms.ImageField(
        widget=forms.FileInput(),
        label='Ícone'
    )

    nome = forms.CharField(
        max_length=50,
        label='Nome',
    )

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        for p in punctuation:
            if p in nome:
                self.add_error('nome', 'O nome da categoria não pode conter pontuação.')
        return nome
