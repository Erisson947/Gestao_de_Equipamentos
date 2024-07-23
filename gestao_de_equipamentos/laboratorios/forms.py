from django import forms

from django.utils.translation import gettext_lazy as _

from laboratorios import models


class LaboratorioForm(forms.ModelForm):
    required_css_class = 'required'
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    class Meta:
        model = models.Laboratorio
        fields = ['nome']


    nome = forms.CharField(
        max_length=75,
        label='Nome',
    )


