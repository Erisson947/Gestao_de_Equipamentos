# Generated by Django 4.2.11 on 2024-12-30 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='laboratorio/equipamentos/imagem')),
                ('nome', models.CharField(max_length=200)),
                ('descrição', models.TextField(max_length=5000)),
                ('patrimônio', models.TextField(max_length=5000)),
                ('com_problemas', models.BooleanField(default=False)),
                ('problemas', models.TextField(blank=True, max_length=5000, null=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-criado_em'],
            },
        ),
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=500)),
                ('contato', models.CharField(max_length=20)),
                ('area_pesq', models.IntegerField(blank=True, choices=[(1, 'CIÊNCIAS EXATAS E DA TERRA'), (2, 'CIÊNCIAS BIOLÓGICAS'), (3, 'ENGENHARIAS'), (4, 'CIÊNCIAS DA SAÚDE'), (5, 'CIÊNCIAS AGRÁRIAS'), (6, 'CIÊNCIAS SOCIAIS APLICADAS'), (7, 'CIÊNCIAS HUMANAS'), (8, 'LINGUÍSTICA, LETRAS E ARTES'), (9, 'MULTIDISCIPLINAR'), (10, 'MATEMÁTICA (CIÊNCIAS EXATAS E DA TERRA)'), (11, 'PROBABILIDADE E ESTATÍSTICA (CIÊNCIAS EXATAS E DA TERRA)'), (12, 'CIÊNCIA DA COMPUTAÇÃO (CIÊNCIAS EXATAS E DA TERRA)'), (13, 'ASTRONOMIA (CIÊNCIAS EXATAS E DA TERRA)'), (14, 'FÍSICA (CIÊNCIAS EXATAS E DA TERRA)'), (15, 'QUÍMICA (CIÊNCIAS EXATAS E DA TERRA)'), (16, 'GEOCIÊNCIAS (CIÊNCIAS EXATAS E DA TERRA)'), (17, 'OCEANOGRAFIA (CIÊNCIAS BIOLÓGICAS)'), (18, 'BIOLOGIA GERAL (CIÊNCIAS BIOLÓGICAS)'), (19, 'GENÉTICA (CIÊNCIAS BIOLÓGICAS)'), (20, 'BOTÂNICA (CIÊNCIAS BIOLÓGICAS)'), (21, 'ZOOLOGIA (CIÊNCIAS BIOLÓGICAS)'), (22, 'MORFOLOGIA (CIÊNCIAS BIOLÓGICAS)'), (23, 'FISIOLOGIA (CIÊNCIAS BIOLÓGICAS)'), (24, 'BIOQUÍMICA (CIÊNCIAS BIOLÓGICAS)'), (25, 'BIOFÍSICA (CIÊNCIAS BIOLÓGICAS)'), (26, 'FARMACOLOGIA (CIÊNCIAS BIOLÓGICAS)'), (27, 'IMUNOLOGIA (CIÊNCIAS BIOLÓGICAS)'), (28, 'MICROBIOLOGIA (CIÊNCIAS BIOLÓGICAS)'), (29, 'PARASITOLOGIA (CIÊNCIAS BIOLÓGICAS)'), (30, 'ECOLOGIA (CIÊNCIAS BIOLÓGICAS)'), (31, 'ENGENHARIA CIVIL (ENGENHARIAS)'), (32, 'ENGENHARIA SANITÁRIA (ENGENHARIAS)'), (33, 'ENGENHARIA DE TRANSPORTES (ENGENHARIAS)'), (34, 'ENGENHARIA DE MINAS (ENGENHARIAS)'), (35, 'ENGENHARIA DE MATERIAIS E METALÚRGICA (ENGENHARIAS)'), (36, 'ENGENHARIA QUÍMICA (ENGENHARIAS)'), (37, 'ENGENHARIA NUCLEAR (ENGENHARIAS)'), (38, 'ENGENHARIA MECÂNICA (ENGENHARIAS)'), (39, 'ENGENHARIA DE PRODUÇÃO (ENGENHARIAS)'), (40, 'ENGENHARIA NAVAL E OCEÃNICA (ENGENHARIAS)'), (41, 'ENGENHARIA AEROESPACIAL (ENGENHARIAS)'), (42, 'ENGENHARIA ELÉTRICA (ENGENHARIAS)'), (43, 'ENGENHARIA BIOMÉDICA (ENGENHARIAS)'), (44, 'MEDICINA (CIÊNCIAS DA SAÚDE)'), (45, 'NUTRIÇÃO (CIÊNCIAS DA SAÚDE)'), (46, 'ODONTOLOGIA (CIÊNCIAS DA SAÚDE)'), (47, 'FARMÁCIA (CIÊNCIAS DA SAÚDE)'), (48, 'ENFERMAGEM (CIÊNCIAS DA SAÚDE)'), (49, 'SAÚDE COLETIVA (CIÊNCIAS DA SAÚDE)'), (50, 'EDUCAÇÃO FÍSICA (CIÊNCIAS DA SAÚDE)'), (51, 'FONOAUDIOLOGIA (CIÊNCIAS DA SAÚDE)'), (52, 'FISIOTERAPIA E TERAPIA OCUPACIONAL (CIÊNCIAS DA SAÚDE)'), (53, 'AGRONOMIA (CIÊNCIAS AGRÁRIAS)'), (54, 'RECURSOS FLORESTAIS E ENGENHARIA FLORESTAL (CIÊNCIAS AGRÁRIAS)'), (55, 'ENGENHARIA AGRÍCOLA (CIÊNCIAS AGRÁRIAS)'), (56, 'ZOOTECNIA (CIÊNCIAS AGRÁRIAS)'), (57, 'RECURSOS PESQUEIROS E ENGENHARIA DE PESCA (CIÊNCIAS AGRÁRIAS)'), (58, 'MEDICINA VETERINÁRIA (CIÊNCIAS AGRÁRIAS)'), (59, 'CIÊNCIA E TECNOLOGIA DE ALIMENTOS (CIÊNCIAS AGRÁRIAS)'), (60, 'DIREITO (CIÊNCIAS SOCIAIS APLICADAS)'), (61, 'ADMINISTRAÇÃO (CIÊNCIAS SOCIAIS APLICADAS)'), (62, 'TURISMO (CIÊNCIAS SOCIAIS APLICADAS)'), (63, 'ECONOMIA (CIÊNCIAS SOCIAIS APLICADAS)'), (64, 'ARQUITETURA E URBANISMO (CIÊNCIAS SOCIAIS APLICADAS)'), (65, 'DESENHO INDUSTRIAL (CIÊNCIAS SOCIAIS APLICADAS)'), (66, 'PLANEJAMENTO URBANO E REGIONAL (CIÊNCIAS SOCIAIS APLICADAS)'), (67, 'DEMOGRAFIA (CIÊNCIAS SOCIAIS APLICADAS)'), (68, 'CIÊNCIA DA INFORMAÇÃO (CIÊNCIAS SOCIAIS APLICADAS)'), (69, 'MUSEOLOGIA (CIÊNCIAS SOCIAIS APLICADAS)'), (70, 'COMUNICAÇÃO (CIÊNCIAS SOCIAIS APLICADAS)'), (71, 'SERVIÇO SOCIAL (CIÊNCIAS SOCIAIS APLICADAS)'), (72, 'FILOSOFIA (CIÊNCIAS HUMANAS)'), (73, 'TEOLOGIA (CIÊNCIAS HUMANAS)'), (74, 'SOCIOLOGIA (CIÊNCIAS HUMANAS)'), (75, 'ANTROPOLOGIA (CIÊNCIAS HUMANAS)'), (76, 'ARQUEOLOGIA (CIÊNCIAS HUMANAS)'), (77, 'HISTÓRIA (CIÊNCIAS HUMANAS)'), (78, 'GEOGRAFIA (CIÊNCIAS HUMANAS)'), (79, 'PSICOLOGIA (CIÊNCIAS HUMANAS)'), (80, 'EDUCAÇÃO (CIÊNCIAS HUMANAS)'), (81, 'CIÊNCIA POLÍTICA (CIÊNCIAS HUMANAS)'), (82, 'LINGUÍSTICA (LINGUÍSTICA, LETRAS E ARTES)'), (83, 'LETRAS (LINGUÍSTICA, LETRAS E ARTES)'), (84, 'ARTES (LINGUÍSTICA, LETRAS E ARTES)'), (85, 'INTERDISCIPLINAR (MULTIDISCIPLINAR)'), (86, 'ENSINO (MULTIDISCIPLINAR)'), (87, 'MATERIAIS (MULTIDISCIPLINAR)'), (88, 'BIOTECNOLOGIA (MULTIDISCIPLINAR)')], null=True)),
                ('horario_func', models.CharField(max_length=100)),
                ('local', models.CharField(max_length=100)),
                ('serv_real', models.CharField(max_length=500)),
                ('campus', models.CharField(default=None, max_length=4, null=True)),
                ('slug', models.SlugField(max_length=220, unique=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('coordenador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-criado_em'],
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='laboratorio/materiais/imagem')),
                ('descrição', models.CharField(max_length=300)),
                ('quantidade', models.PositiveIntegerField(blank=True, null=True)),
                ('tipo_quant', models.CharField(blank=True, choices=[('UNIDADES', 'unidades'), ('KG', 'kg'), ('G', 'g'), ('M', 'm'), ('CM', 'cm')], max_length=10, null=True)),
                ('valor_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('laboratorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materiais', to='laboratorios.laboratorio')),
            ],
            options={
                'ordering': ['-criado_em'],
            },
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrição', models.CharField(max_length=2000)),
                ('ativo', models.BooleanField(default=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('equipamentos', models.ManyToManyField(blank=True, to='laboratorios.equipamento')),
                ('laboratorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='serviços', to='laboratorios.laboratorio')),
                ('materiais', models.ManyToManyField(blank=True, to='laboratorios.material')),
            ],
            options={
                'ordering': ['-criado_em'],
            },
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('tipo', models.CharField(choices=[('ensino', 'Ensino'), ('pesquisa', 'Pesquisa'), ('extenção', 'Extenção')], max_length=10)),
                ('situação', models.CharField(choices=[('em edição', 'Em Edição'), ('enviado', 'Enviado'), ('pre-selecionado', 'Pré-Selecionado'), ('em execução', 'Em Execução'), ('encerrado', 'Encerrado'), ('cancelado', 'Cancelado')], max_length=20)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('laboratorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projetos', to='laboratorios.laboratorio')),
            ],
            options={
                'ordering': ['-criado_em'],
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('laboratorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professores', to='laboratorios.laboratorio')),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-criado_em'],
            },
        ),
        migrations.CreateModel(
            name='Horario_aula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disciplina', models.CharField(max_length=200)),
                ('horario', multiselectfield.db.fields.MultiSelectField(choices=[('Segunda;Matutino;1', 'Segunda;Matutino;1'), ('Segunda;Matutino;2', 'Segunda;Matutino;2'), ('Segunda;Matutino;3', 'Segunda;Matutino;3'), ('Segunda;Matutino;4', 'Segunda;Matutino;4'), ('Segunda;Matutino;5', 'Segunda;Matutino;5'), ('Segunda;Matutino;6', 'Segunda;Matutino;6'), ('Segunda;Vespertino;1', 'Segunda;Vespertino;1'), ('Segunda;Vespertino;2', 'Segunda;Vespertino;2'), ('Segunda;Vespertino;3', 'Segunda;Vespertino;3'), ('Segunda;Vespertino;4', 'Segunda;Vespertino;4'), ('Segunda;Vespertino;5', 'Segunda;Vespertino;5'), ('Segunda;Vespertino;6', 'Segunda;Vespertino;6'), ('Segunda;Noturno;1', 'Segunda;Noturno;1'), ('Segunda;Noturno;2', 'Segunda;Noturno;2'), ('Segunda;Noturno;3', 'Segunda;Noturno;3'), ('Segunda;Noturno;4', 'Segunda;Noturno;4'), ('Segunda;Noturno;5', 'Segunda;Noturno;5'), ('Terça;Matutino;1', 'Terça;Matutino;1'), ('Terça;Matutino;2', 'Terça;Matutino;2'), ('Terça;Matutino;3', 'Terça;Matutino;3'), ('Terça;Matutino;4', 'Terça;Matutino;4'), ('Terça;Matutino;5', 'Terça;Matutino;5'), ('Terça;Matutino;6', 'Terça;Matutino;6'), ('Terça;Vespertino;1', 'Terça;Vespertino;1'), ('Terça;Vespertino;2', 'Terça;Vespertino;2'), ('Terça;Vespertino;3', 'Terça;Vespertino;3'), ('Terça;Vespertino;4', 'Terça;Vespertino;4'), ('Terça;Vespertino;5', 'Terça;Vespertino;5'), ('Terça;Vespertino;6', 'Terça;Vespertino;6'), ('Terça;Noturno;1', 'Terça;Noturno;1'), ('Terça;Noturno;2', 'Terça;Noturno;2'), ('Terça;Noturno;3', 'Terça;Noturno;3'), ('Terça;Noturno;4', 'Terça;Noturno;4'), ('Terça;Noturno;5', 'Terça;Noturno;5'), ('Quarta;Matutino;1', 'Quarta;Matutino;1'), ('Quarta;Matutino;2', 'Quarta;Matutino;2'), ('Quarta;Matutino;3', 'Quarta;Matutino;3'), ('Quarta;Matutino;4', 'Quarta;Matutino;4'), ('Quarta;Matutino;5', 'Quarta;Matutino;5'), ('Quarta;Matutino;6', 'Quarta;Matutino;6'), ('Quarta;Vespertino;1', 'Quarta;Vespertino;1'), ('Quarta;Vespertino;2', 'Quarta;Vespertino;2'), ('Quarta;Vespertino;3', 'Quarta;Vespertino;3'), ('Quarta;Vespertino;4', 'Quarta;Vespertino;4'), ('Quarta;Vespertino;5', 'Quarta;Vespertino;5'), ('Quarta;Vespertino;6', 'Quarta;Vespertino;6'), ('Quarta;Noturno;1', 'Quarta;Noturno;1'), ('Quarta;Noturno;2', 'Quarta;Noturno;2'), ('Quarta;Noturno;3', 'Quarta;Noturno;3'), ('Quarta;Noturno;4', 'Quarta;Noturno;4'), ('Quarta;Noturno;5', 'Quarta;Noturno;5'), ('Quinta;Matutino;1', 'Quinta;Matutino;1'), ('Quinta;Matutino;2', 'Quinta;Matutino;2'), ('Quinta;Matutino;3', 'Quinta;Matutino;3'), ('Quinta;Matutino;4', 'Quinta;Matutino;4'), ('Quinta;Matutino;5', 'Quinta;Matutino;5'), ('Quinta;Matutino;6', 'Quinta;Matutino;6'), ('Quinta;Vespertino;1', 'Quinta;Vespertino;1'), ('Quinta;Vespertino;2', 'Quinta;Vespertino;2'), ('Quinta;Vespertino;3', 'Quinta;Vespertino;3'), ('Quinta;Vespertino;4', 'Quinta;Vespertino;4'), ('Quinta;Vespertino;5', 'Quinta;Vespertino;5'), ('Quinta;Vespertino;6', 'Quinta;Vespertino;6'), ('Quinta;Noturno;1', 'Quinta;Noturno;1'), ('Quinta;Noturno;2', 'Quinta;Noturno;2'), ('Quinta;Noturno;3', 'Quinta;Noturno;3'), ('Quinta;Noturno;4', 'Quinta;Noturno;4'), ('Quinta;Noturno;5', 'Quinta;Noturno;5'), ('Sexta;Matutino;1', 'Sexta;Matutino;1'), ('Sexta;Matutino;2', 'Sexta;Matutino;2'), ('Sexta;Matutino;3', 'Sexta;Matutino;3'), ('Sexta;Matutino;4', 'Sexta;Matutino;4'), ('Sexta;Matutino;5', 'Sexta;Matutino;5'), ('Sexta;Matutino;6', 'Sexta;Matutino;6'), ('Sexta;Vespertino;1', 'Sexta;Vespertino;1'), ('Sexta;Vespertino;2', 'Sexta;Vespertino;2'), ('Sexta;Vespertino;3', 'Sexta;Vespertino;3'), ('Sexta;Vespertino;4', 'Sexta;Vespertino;4'), ('Sexta;Vespertino;5', 'Sexta;Vespertino;5'), ('Sexta;Vespertino;6', 'Sexta;Vespertino;6'), ('Sexta;Noturno;1', 'Sexta;Noturno;1'), ('Sexta;Noturno;2', 'Sexta;Noturno;2'), ('Sexta;Noturno;3', 'Sexta;Noturno;3'), ('Sexta;Noturno;4', 'Sexta;Noturno;4'), ('Sexta;Noturno;5', 'Sexta;Noturno;5'), ('Sábado;Matutino;1', 'Sábado;Matutino;1'), ('Sábado;Matutino;2', 'Sábado;Matutino;2'), ('Sábado;Matutino;3', 'Sábado;Matutino;3'), ('Sábado;Matutino;4', 'Sábado;Matutino;4'), ('Sábado;Matutino;5', 'Sábado;Matutino;5'), ('Sábado;Matutino;6', 'Sábado;Matutino;6'), ('Sábado;Vespertino;1', 'Sábado;Vespertino;1'), ('Sábado;Vespertino;2', 'Sábado;Vespertino;2'), ('Sábado;Vespertino;3', 'Sábado;Vespertino;3'), ('Sábado;Vespertino;4', 'Sábado;Vespertino;4'), ('Sábado;Vespertino;5', 'Sábado;Vespertino;5'), ('Sábado;Vespertino;6', 'Sábado;Vespertino;6'), ('Sábado;Noturno;1', 'Sábado;Noturno;1'), ('Sábado;Noturno;2', 'Sábado;Noturno;2'), ('Sábado;Noturno;3', 'Sábado;Noturno;3'), ('Sábado;Noturno;4', 'Sábado;Noturno;4'), ('Sábado;Noturno;5', 'Sábado;Noturno;5'), ('Domingo;Matutino;1', 'Domingo;Matutino;1'), ('Domingo;Matutino;2', 'Domingo;Matutino;2'), ('Domingo;Matutino;3', 'Domingo;Matutino;3'), ('Domingo;Matutino;4', 'Domingo;Matutino;4'), ('Domingo;Matutino;5', 'Domingo;Matutino;5'), ('Domingo;Matutino;6', 'Domingo;Matutino;6'), ('Domingo;Vespertino;1', 'Domingo;Vespertino;1'), ('Domingo;Vespertino;2', 'Domingo;Vespertino;2'), ('Domingo;Vespertino;3', 'Domingo;Vespertino;3'), ('Domingo;Vespertino;4', 'Domingo;Vespertino;4'), ('Domingo;Vespertino;5', 'Domingo;Vespertino;5'), ('Domingo;Vespertino;6', 'Domingo;Vespertino;6'), ('Domingo;Noturno;1', 'Domingo;Noturno;1'), ('Domingo;Noturno;2', 'Domingo;Noturno;2'), ('Domingo;Noturno;3', 'Domingo;Noturno;3'), ('Domingo;Noturno;4', 'Domingo;Noturno;4'), ('Domingo;Noturno;5', 'Domingo;Noturno;5')], max_length=10000)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('laboratorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horarios', to='laboratorios.laboratorio')),
                ('professor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='laboratorios.professor')),
            ],
            options={
                'ordering': ['-criado_em'],
            },
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='laboratorio/fotos/imagem')),
                ('titulo', models.CharField(max_length=150)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('laboratorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fotos', to='laboratorios.laboratorio')),
            ],
            options={
                'ordering': ['-criado_em'],
            },
        ),
        migrations.AddField(
            model_name='equipamento',
            name='laboratorio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipamentos', to='laboratorios.laboratorio'),
        ),
        migrations.AddConstraint(
            model_name='laboratorio',
            constraint=models.UniqueConstraint(fields=('nome', 'campus'), name='nome do laboratorio e campus unicos'),
        ),
    ]
