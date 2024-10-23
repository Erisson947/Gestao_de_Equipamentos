from django import forms

from django.utils.translation import gettext_lazy as _

from laboratorios import models


class LaboratorioForm(forms.ModelForm):
    AREA_PESQ = [
        ("" ,"----------"),
        (1 ,"CIÊNCIAS EXATAS E DA TERRA"),
        (2 ,"CIÊNCIAS BIOLÓGICAS"),
        (3 ,"ENGENHARIAS"),
        (4 ,"CIÊNCIAS DA SAÚDE"),
        (5 ,"CIÊNCIAS AGRÁRIAS"),
        (6 ,"CIÊNCIAS SOCIAIS APLICADAS"),
        (7 ,"CIÊNCIAS HUMANAS"),
        (8 ,"LINGUÍSTICA, LETRAS E ARTES"),
        (9 ,"MULTIDISCIPLINAR"),
        (10,"MATEMÁTICA (CIÊNCIAS EXATAS E DA TERRA)"),
        (11,"PROBABILIDADE E ESTATÍSTICA (CIÊNCIAS EXATAS E DA TERRA)"),
        (12,"CIÊNCIA DA COMPUTAÇÃO (CIÊNCIAS EXATAS E DA TERRA)"),
        (13,"ASTRONOMIA (CIÊNCIAS EXATAS E DA TERRA)"),
        (14,"FÍSICA (CIÊNCIAS EXATAS E DA TERRA)"),
        (15,"QUÍMICA (CIÊNCIAS EXATAS E DA TERRA)"),
        (16,"GEOCIÊNCIAS (CIÊNCIAS EXATAS E DA TERRA)"),
        (17,"OCEANOGRAFIA (CIÊNCIAS BIOLÓGICAS)"),
        (18,"BIOLOGIA GERAL (CIÊNCIAS BIOLÓGICAS)"),
        (19,"GENÉTICA (CIÊNCIAS BIOLÓGICAS)"),
        (20,"BOTÂNICA (CIÊNCIAS BIOLÓGICAS)"),
        (21,"ZOOLOGIA (CIÊNCIAS BIOLÓGICAS)"),
        (22,"MORFOLOGIA (CIÊNCIAS BIOLÓGICAS)"),
        (23,"FISIOLOGIA (CIÊNCIAS BIOLÓGICAS)"),
        (24,"BIOQUÍMICA (CIÊNCIAS BIOLÓGICAS)"),
        (25,"BIOFÍSICA (CIÊNCIAS BIOLÓGICAS)"),
        (26,"FARMACOLOGIA (CIÊNCIAS BIOLÓGICAS)"),
        (27,"IMUNOLOGIA (CIÊNCIAS BIOLÓGICAS)"),
        (28,"MICROBIOLOGIA (CIÊNCIAS BIOLÓGICAS)"),
        (29,"PARASITOLOGIA (CIÊNCIAS BIOLÓGICAS)"),
        (30,"ECOLOGIA (CIÊNCIAS BIOLÓGICAS)"),
        (31,"ENGENHARIA CIVIL (ENGENHARIAS)"),
        (32,"ENGENHARIA SANITÁRIA (ENGENHARIAS)"),
        (33,"ENGENHARIA DE TRANSPORTES (ENGENHARIAS)"),
        (34,"ENGENHARIA DE MINAS (ENGENHARIAS)"),
        (35,"ENGENHARIA DE MATERIAIS E METALÚRGICA (ENGENHARIAS)"),
        (36,"ENGENHARIA QUÍMICA (ENGENHARIAS)"),
        (37,"ENGENHARIA NUCLEAR (ENGENHARIAS)"),
        (38,"ENGENHARIA MECÂNICA (ENGENHARIAS)"),
        (39,"ENGENHARIA DE PRODUÇÃO (ENGENHARIAS)"),
        (40,"ENGENHARIA NAVAL E OCEÃNICA (ENGENHARIAS)"),
        (41,"ENGENHARIA AEROESPACIAL (ENGENHARIAS)"),
        (42,"ENGENHARIA ELÉTRICA (ENGENHARIAS)"),
        (43,"ENGENHARIA BIOMÉDICA (ENGENHARIAS)"),
        (44,"MEDICINA (CIÊNCIAS DA SAÚDE)"),
        (45,"NUTRIÇÃO (CIÊNCIAS DA SAÚDE)"),
        (46,"ODONTOLOGIA (CIÊNCIAS DA SAÚDE)"),
        (47,"FARMÁCIA (CIÊNCIAS DA SAÚDE)"),
        (48,"ENFERMAGEM (CIÊNCIAS DA SAÚDE)"),
        (49,"SAÚDE COLETIVA (CIÊNCIAS DA SAÚDE)"),
        (50,"EDUCAÇÃO FÍSICA (CIÊNCIAS DA SAÚDE)"),
        (51,"FONOAUDIOLOGIA (CIÊNCIAS DA SAÚDE)"),
        (52,"FISIOTERAPIA E TERAPIA OCUPACIONAL (CIÊNCIAS DA SAÚDE)"),
        (53,"AGRONOMIA (CIÊNCIAS AGRÁRIAS)"),
        (54,"RECURSOS FLORESTAIS E ENGENHARIA FLORESTAL (CIÊNCIAS AGRÁRIAS)"),
        (55,"ENGENHARIA AGRÍCOLA (CIÊNCIAS AGRÁRIAS)"),
        (56,"ZOOTECNIA (CIÊNCIAS AGRÁRIAS)"),
        (57,"RECURSOS PESQUEIROS E ENGENHARIA DE PESCA (CIÊNCIAS AGRÁRIAS)"),
        (58,"MEDICINA VETERINÁRIA (CIÊNCIAS AGRÁRIAS)"),
        (59,"CIÊNCIA E TECNOLOGIA DE ALIMENTOS (CIÊNCIAS AGRÁRIAS)"),
        (60,"DIREITO (CIÊNCIAS SOCIAIS APLICADAS)"),
        (61,"ADMINISTRAÇÃO (CIÊNCIAS SOCIAIS APLICADAS)"),
        (62,"TURISMO (CIÊNCIAS SOCIAIS APLICADAS)"),
        (63,"ECONOMIA (CIÊNCIAS SOCIAIS APLICADAS)"),
        (64,"ARQUITETURA E URBANISMO (CIÊNCIAS SOCIAIS APLICADAS)"),
        (65,"DESENHO INDUSTRIAL (CIÊNCIAS SOCIAIS APLICADAS)"),
        (66,"PLANEJAMENTO URBANO E REGIONAL (CIÊNCIAS SOCIAIS APLICADAS)"),
        (67,"DEMOGRAFIA (CIÊNCIAS SOCIAIS APLICADAS)"),
        (68,"CIÊNCIA DA INFORMAÇÃO (CIÊNCIAS SOCIAIS APLICADAS)"),
        (69,"MUSEOLOGIA (CIÊNCIAS SOCIAIS APLICADAS)"),
        (70,"COMUNICAÇÃO (CIÊNCIAS SOCIAIS APLICADAS)"),
        (71,"SERVIÇO SOCIAL (CIÊNCIAS SOCIAIS APLICADAS)"),
        (72,"FILOSOFIA (CIÊNCIAS HUMANAS)"),
        (73,"TEOLOGIA (CIÊNCIAS HUMANAS)"),
        (74,"SOCIOLOGIA (CIÊNCIAS HUMANAS)"),
        (75,"ANTROPOLOGIA (CIÊNCIAS HUMANAS)"),
        (76,"ARQUEOLOGIA (CIÊNCIAS HUMANAS)"),
        (77,"HISTÓRIA (CIÊNCIAS HUMANAS)"),
        (78,"GEOGRAFIA (CIÊNCIAS HUMANAS)"),
        (79,"PSICOLOGIA (CIÊNCIAS HUMANAS)"),
        (80,"EDUCAÇÃO (CIÊNCIAS HUMANAS)"),
        (81,"CIÊNCIA POLÍTICA (CIÊNCIAS HUMANAS)"),
        (82,"LINGUÍSTICA (LINGUÍSTICA, LETRAS E ARTES)"),
        (83,"LETRAS (LINGUÍSTICA, LETRAS E ARTES)"),
        (84,"ARTES (LINGUÍSTICA, LETRAS E ARTES)"),
        (85,"INTERDISCIPLINAR (MULTIDISCIPLINAR)"),
        (86,"ENSINO (MULTIDISCIPLINAR)"),
        (87,"MATERIAIS (MULTIDISCIPLINAR)"),
        (88,"BIOTECNOLOGIA (MULTIDISCIPLINAR)"),
        ]
    
    required_css_class = 'required'
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    class Meta:
        model = models.Laboratorio
        fields = '__all__'
        exclude = ['campus', 'slug', 'criado_em', 'atualizado_em']


    nome = forms.CharField(
        max_length=75,
        label='Nome: ',
        required= True,
    )
    
    coordenador = forms.ModelChoiceField(
        label='Coordenador: ',
        queryset=models.User.objects.all(),
    )

    descricao = forms.CharField(
        max_length=75,
        label='Descrição: ',
    )

    contato = forms.CharField(
        max_length=75,
        label='Contato: ',
    )

    local = forms.CharField(
        max_length=75,
        label='Local: ',
    )

    area_pesq = forms.ChoiceField(
        choices=AREA_PESQ,
        widget=forms.Select(),
        label='Área de Pesquisa: ',
    )



    horario_func = forms.CharField(
        max_length=75,
        label='Horário de Funcionamento: ',
    )


    serv_real = forms.CharField(
        max_length=75,
        label='Serviço Realizado: ',
    )


class HorarioForm(forms.ModelForm):
    required_css_class = 'required'
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    class Meta:
        dia_sem = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
        turno = ['Matutino', 'Vespertino', 'Noturno']
        horas = [1, 2, 3, 4, 5, 6]
        
        HORARIO = []
        
        for Dia_sem in dia_sem:
            for Turno in turno:
                for Horas in horas:
                    if Turno != 'Noturno' and Horas != 6:
                        HORARIO.append((f'{Dia_sem};{Turno};{Horas}', f'{Dia_sem};{Turno};{Horas}'),)
        
        model = models.Horario_aula
        fields = '__all__'
        exclude = ['laboratorio', 'horario', 'autor', 'criado_em', 'atualizado_em']
        
        professor = forms.ModelChoiceField(
            label="Professor: ",
            required=False,
            queryset= models.Professor.objects.all(),
        )
        
        
        