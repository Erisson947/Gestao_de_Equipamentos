from django.db import models
from multiselectfield import MultiSelectField

from helpers.slug import gerar_slug_dinamica
from helpers.model import get_object


from usuarios.models import User

class Laboratorio(models.Model):
    AREA_PESQ = [
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
    
    nome = models.CharField(max_length=100)
    coordenador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    descricao = models.CharField(max_length=500)
    contato = models.CharField(max_length=20, null=True, blank=True)
    area_pesq = models.IntegerField(choices=AREA_PESQ, null=True, blank=True)
    horario_func = models.CharField(max_length=100, null=True, blank=True)
    local = models.CharField(max_length=100, null=True, blank=True)
    serv_real = models.CharField(max_length=500, null=True, blank=True)
    campus = models.CharField(max_length=4, null=True, default=None)
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
    
    
class Professor(models.Model):
    nome = models.ForeignKey(User, on_delete=models.CASCADE)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, related_name='professores')
    criado_em = models.DateTimeField(auto_now_add=True, editable=False)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.nome.full_name
    
    class Meta:
        ordering = ['-criado_em']
        
        
class Equipamento(models.Model):
    imagem = models.ImageField(upload_to='laboratorio/equipamentos/imagem', blank=True, null=True)
    nome = models.CharField(max_length=200)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, related_name='equipamentos')
    descrição = models.TextField(max_length=5000)
    patrimônio = models.TextField(max_length=5000)
    com_problemas = models.BooleanField(default=False)
    problemas = models.TextField(max_length=5000, null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True, editable=False)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['-criado_em']
        
  

class Material(models.Model):
    TIPO_QUANT = [
        ('UNIDADES', 'unidades'),
        ('KG', 'kg'),
        ('G', 'g'),
        ('M', 'm'),
        ('CM', 'cm'),
    ]  
    
    imagem = models.ImageField(upload_to='laboratorio/materiais/imagem', blank=True, null=True)
    descrição = models.CharField(max_length=300)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, related_name='materiais')
    quantidade = models.PositiveIntegerField(null=True, blank=True)
    tipo_quant = models.CharField(choices=TIPO_QUANT, max_length=10, null=True, blank=True)
    valor_unit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True, editable=False)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.descrição
    
    class Meta:
        ordering = ['-criado_em']
        
class Servico(models.Model):
    descrição = models.CharField(max_length=2000)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, related_name='serviços')
    equipamentos = models.ManyToManyField(Equipamento, blank=True)
    materiais = models.ManyToManyField(Material, blank=True)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True, editable=False)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.descrição
    
    class Meta:
        ordering = ['-criado_em']
        

        
class Projeto(models.Model):
    
    TIPO_PROJ = [
        ('ensino', 'Ensino'),
        ('pesquisa', 'Pesquisa'),
        ('extenção', 'Extenção'),
    ]

    SITUAÇÃO_PROJ = [
        ('em edição', 'Em Edição'),
        ('enviado', 'Enviado'),
        ('pre-selecionado', 'Pré-Selecionado'),
        ('em execução', 'Em Execução'),
        ('encerrado', 'Encerrado'),
        ('cancelado', 'Cancelado'),
    ]

    titulo = models.CharField(max_length=100)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, related_name='projetos')
    tipo = models.CharField(choices=TIPO_PROJ, max_length=10)
    situação = models.CharField(choices=SITUAÇÃO_PROJ, max_length=20)
    criado_em = models.DateTimeField(auto_now_add=True, editable=False)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ['-criado_em']
        
class Foto(models.Model):
    imagem = models.ImageField(upload_to='laboratorio/fotos/imagem', blank=True, null=True)
    titulo = models.CharField(max_length=150)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, related_name='fotos')
    criado_em = models.DateTimeField(auto_now_add=True, editable=False)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ['-criado_em']

        
class Horario_aula(models.Model):
    dia_sem = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
    turno = ['Matutino', 'Vespertino', 'Noturno']
    horas = [1, 2, 3, 4, 5, 6]
    
    HORARIO = []
    
    for Dia_sem in dia_sem:
        for Turno in turno:
            for Horas in horas:
                if Turno != 'Noturno' or Horas != 6:
                    HORARIO.append((f'{Dia_sem};{Turno};{Horas}', f'{Dia_sem};{Turno};{Horas}'),)
    
    disciplina = models.CharField(max_length=200)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, blank=True, null=True)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, related_name='horarios')
    horario = MultiSelectField(choices=HORARIO, max_length=10000)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True, editable=False)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.disciplina
    
    class Meta:
        ordering = ['-criado_em']
        
    