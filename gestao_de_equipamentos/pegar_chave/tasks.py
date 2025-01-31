from pegar_chave import models
from usuarios.models import User
from django.core.mail import send_mail, send_mass_mail
from datetime import datetime


from celery import shared_task

@shared_task
def checar_chaves_atrasadas():

    chaves_pegadas = models.Pegar_Chave.objects.all()
    dias_atraso = 0
    
    for chave in chaves_pegadas:
        if chave.situacao != 'devolvida':
            if chave.situacao == 'em uso':
                chave.situacao = 'atrasada'
            elif chave.situacao == 'atrasada':
                d1 = datetime.strptime(chave.tempo_max_devolucao, "%d/%m/%Y %H:%M:%S")
                d2 = datetime.strptime(datetime.now(), "%d/%m/%Y %H:%M:%S")
                dias_atraso = abs((d2 - d1).days)
            admins = []
            for admin in User.objects.filter(is_admin=True):
                admins.append(admin.school_email)
            
            if chave.chave.laboratorio:
                sala = chave.chave.laboratorio
            else:
                sala= 'Sala Comum'
            mensagem1 = (f'Chave {chave.chave} Atrasada!',
                f'O usuário {chave.usuario} - {chave.usuario.registration} não devolveu a chave {chave.chave}, da {sala}, até o final do dia {chave.pegada_em.date}, e ela encontrasse atrasada a {dias_atraso}!',
                'no-reply@gestao_de_laboratorios.com.br',
                admins)
            mensagem2 = (f'Chave {chave.chave} Atrasada!',
                f'Você não devolveu a chave {chave.chave}, da {sala}, até o final do dia {chave.pegada_em.date}, e ela encontrasse atrasada a {dias_atraso}!',
                'no-reply@gestao_de_laboratorios.com.br',
                [chave.usuario.school_email])
            
            send_mass_mail((mensagem1, mensagem2), fail_silently=False)
    return None