
from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from helpers.form import set_placeholder, set_attr

from equipamentos import models


class EquipamentoForm(forms.ModelForm):
    required_css_class = 'required'
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        set_attr(self.fields['titulo'], 'class', 'form-control')
        set_placeholder(self.fields['titulo'], 'Digite o nome do equipamento...')
        set_placeholder(self.fields['conteudo'], 'Exemplo: Os equipamentos que estão quebrados em sua maioria estão com partes faltando ou não ligam ...')
        set_placeholder(self.fields['detal_equ_func'], 'Exemplos: Computador Avançado A1; Computador Avançado A2; ...')
        set_placeholder(self.fields['detal_equ_queb'], 'Exemplos: Computador Avançado B3: Não está ligando; Computador Avançado B2: Está sem a placa mãe; ...')
        set_placeholder(self.fields['detal_equ_em_manut'], 'Exemplos: Computador Avançado B3; Computador Avançado B2; ...')

    class Meta:
        model = models.Equipamento
    
        fields = '__all__'
        exclude = ['slug', 'criado_em', 'atualizado_em']

    capa = forms.ImageField(
        widget=forms.FileInput(),
        label='Capa'
    )

    titulo = forms.CharField(
        min_length=1,
        max_length=200,
        label='Nome'
    )
    

    
    laboratorio = forms.ModelChoiceField(
        label='Laboratorio',
        queryset= models.Laboratorio.objects.all()
    )
    
    detalhar = forms.BooleanField(
        label='Detalhar',
        widget= forms.CheckboxInput,
        required=False
    )
    
    total_eq = forms.IntegerField(
        max_value=300,
        min_value=0,
        label='Total de Equipamentos',
        required=False
    )
    
    equ_func = forms.IntegerField(
        max_value=300,
        min_value=0,
        label='Equipamentos Funcionando',
        required=False
    )
    
    equ_queb = forms.IntegerField(
        max_value=300,
        min_value=0,
        label='Equipamentos Quebrados',
        required=False
    )
    
    equ_em_manut = forms.IntegerField(
        max_value=300,
        min_value=0,
        label='Equipamentos em Manutenção',
        required=False
    )

    detal_equ_func = forms.CharField(
        widget=forms.Textarea,
        min_length=0,
        max_length=25000,
        required=False,
        help_text=(_('Adicione todos os equipamentos que estão funcionando em forma de lista!')),
    )
    
    detal_equ_queb = forms.CharField(
        widget=forms.Textarea,
        min_length=0,
        max_length=25000,
        required=False,
        help_text=(_('Adicione todos os equipamentos que estão quebrados em forma de lista e coloque o problema apresentado pelo equipamento a frente dele!')),
    )
    
    detal_equ_em_manut = forms.CharField(
        widget=forms.Textarea,
        min_length=0,
        max_length=25000,
        required=False,
        help_text=(_('Adicione todos os equipamentos que estão em manutenção em forma de lista; De preferência, adicione somente o nome do aparelho que aparece como quebrado e está em manutenção, e não o problema!')),
    )
    
    conteudo = forms.CharField(
        widget=forms.Textarea,
        min_length=0,
        max_length=25000,
        label='Definição',
        help_text=(_('Adicione uma definição genérica do equipamento; Se não conseguir especificar os equipamentos, defina também os problemas gerais deles aqui, sem especificar!')),
    )
    

    def clean(self):
        total_eq = self.cleaned_data['total_eq']
        equ_func = self.cleaned_data['equ_func']
        equ_queb = self.cleaned_data['equ_queb']
        equ_em_manut = self.cleaned_data['equ_em_manut']
        detalhar = self.cleaned_data['detalhar']
        detal_equ_queb = self.cleaned_data['detal_equ_queb']
        detal_equ_func = self.cleaned_data['detal_equ_func']
        detal_equ_em_manut = self.cleaned_data['detal_equ_em_manut']
        
        if equ_func == None and equ_queb == None and equ_em_manut == None:
            pass
        elif equ_queb != None and equ_queb != None and equ_em_manut != None:
            if total_eq != None:
                if equ_queb + equ_func != total_eq:
                    msg = _('A quantidade de equipamentos quebrados e funcionando deve ser igual ao total!')
                    self.add_error('total_eq', msg)
                    self.add_error('equ_func', msg)
                    self.add_error('equ_queb', msg)
                    
                elif equ_em_manut > equ_queb:
                    msg = _('A quantidade de equipamentos em manutenção deve ser menor ou igual aos equipamentos quebrados!')
                    self.add_error('equ_em_manut', msg)
            else:
                msg = _('O total de equipamentos deve ser informado!')
                self.add_error('total_eq', msg)
        else:
            raise ValidationError(_('Informe todos os campos que estão faltando!'))
        
        if detalhar == True:
            if detal_equ_func == '' and equ_func > 0:
                self.add_error('detal_equ_func', _('Você deve especificar quais equipamentos estão funcionando!'))
            elif detal_equ_func != '' and equ_func == 0 or equ_func == None:
                self.add_error('equ_func', _('Você não pode detalhar os equipamentos funcionando sem informar a quantidade de equipamentos funcionado!'))
            elif detal_equ_queb == '' and equ_queb > 0:
                self.add_error('detal_equ_queb', _('Você deve especificar quais equipamentos estão quebrados!'))
            elif detal_equ_queb != '' and equ_queb == 0 or equ_queb == None:
                self.add_error('equ_queb', _('Você não pode detalhar os equipamentos quebrados sem informar a quantidade de equipamentos quebrados!'))
            elif detal_equ_em_manut == '' and equ_em_manut > 0:
                self.add_error('detal_equ_em_manut', _('Você deve especificar quais equipamentos estão em manutenção!'))
            elif detal_equ_em_manut != '' and equ_em_manut == 0 or equ_em_manut == None:
                self.add_error('equ_em_manut', _('Você não pode detalhar os equipamentos em manutenção sem informar a quantidade de equipamentos em manutenção!'))
        else:
            if detal_equ_func != None:
                detal_equ_func = None
                self.cleaned_data['detal_equ_func'] = detal_equ_func
                self.instance.detal_equ_func = detal_equ_func
            elif detal_equ_queb != None:
                detal_equ_queb = None
                self.cleaned_data['detal_equ_queb'] = detal_equ_queb
                self.instance.detal_equ_queb = detal_equ_queb
            else:
                detal_equ_em_manut = None
                self.cleaned_data['detal_equ_em_manut'] = detal_equ_em_manut
                self.instance.detal_equ_em_manut = detal_equ_em_manut
            
        return self.cleaned_data
    
class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['body']
        widgets = {
            'body' : forms.TextInput(attrs={'placeholder': 'Adicionar comentário ...'})
        }
        labels = {
            'body': ''
        }
        
        
class ReplyCreateForm(forms.ModelForm):
    class Meta:
        model = models.Reply
        fields = ['body']
        widgets = {
            'body' : forms.TextInput(attrs={'placeholder': 'Adicionar resposta ...', 'class': "!text-sm"})
        }
        labels = {
            'body': ''
        }

