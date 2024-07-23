# Generated by Django 4.2.11 on 2024-06-10 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('laboratorios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('body', models.CharField(max_length=150)),
                ('status', models.BooleanField(default=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('body', models.CharField(max_length=150)),
                ('status', models.BooleanField(default=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='replies', to=settings.AUTH_USER_MODEL)),
                ('parent_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='equipamentos.comment')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capa', models.ImageField(upload_to='equipamentos/capas')),
                ('titulo', models.CharField(max_length=200, verbose_name='Nome')),
                ('slug', models.SlugField(max_length=220, unique=True)),
                ('total_eq', models.PositiveIntegerField(blank=True, null=True, verbose_name='Total de Equipamentos')),
                ('equ_func', models.PositiveIntegerField(blank=True, null=True, verbose_name='Equipamentos Funcionados')),
                ('equ_queb', models.PositiveIntegerField(blank=True, null=True, verbose_name='Equipamentos Quebrados')),
                ('equ_em_manut', models.PositiveIntegerField(blank=True, null=True, verbose_name='Equipamentos em Manutenção')),
                ('detalhar', models.BooleanField(default=False)),
                ('conteudo', models.TextField(blank=True, max_length=5000, null=True, verbose_name='Definição')),
                ('detal_equ_func', models.TextField(blank=True, max_length=5000, null=True, verbose_name='Detalhar Equipamentos Funcionados')),
                ('detal_equ_queb', models.TextField(blank=True, max_length=5000, null=True, verbose_name='Detalhar Equipamentos Quebrados')),
                ('detal_equ_em_manut', models.TextField(blank=True, max_length=5000, null=True, verbose_name='Detalhar Equipamentos em Manutenção')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('laboratorio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='laboratorios.laboratorio')),
                ('tags', models.ManyToManyField(related_name='equipamentos', to='tags.tag')),
            ],
            options={
                'ordering': ['-criado_em'],
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='parent_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='equipamentos.equipamento'),
        ),
        migrations.AddConstraint(
            model_name='equipamento',
            constraint=models.UniqueConstraint(fields=('titulo', 'laboratorio'), name='laboratorio e equipamento unicos'),
        ),
    ]
