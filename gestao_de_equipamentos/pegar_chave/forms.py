from django import forms


from django.utils.translation import gettext_lazy as _

from pegar_chave import models


class ChaveForm(forms.ModelForm):
    required_css_class = 'required'
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    class Meta:
        model = models.Chave
        fields = ['bloco_num', 'laboratorio']

    bloco_num = forms.CharField(
        max_length=3,
        min_length=3,
        label='Bloco/Número: '
    )

    laboratorio = forms.ModelChoiceField(
        queryset= models.Laboratorio.objects.all(),
        label='Sala: ',
        required=False,
        empty_label="Sala Comum"
    )


class PegarChaveForm(forms.ModelForm):
    required_css_class = 'required'
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    class Meta:
        model = models.Pegar_Chave
        fields = []
    

    