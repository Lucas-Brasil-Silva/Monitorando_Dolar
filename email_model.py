import smtplib
from email.message import EmailMessage
import magic
from time import sleep

""" Para o uso do magic, a necessidade da biblioteca python-magic:
    Sintaxe de instalação:
    pip install python-magic 
    pip install python-magic-bin """

class Email:
    def __init__(self,email_origem,senha_email):
        self.email_origem = email_origem
        self.senha_email = senha_email
    
    def defenior_conteudo(self,email_remetente,lista_de_contatos,topico,conteudo_email):
        self.mail = EmailMessage()
        self.mail['subject'] = topico
        self.mail['FROM'] = email_remetente
        self.mail['TO'] = ','.join(lista_de_contatos)
        self.mail.add_header('Content-Type', 'text/html')
        self.mail.set_payload(conteudo_email.encode('utf-8'))

    def anexar_imagem(self,lista_imagens):
        for imagem in lista_imagens:
            with open(imagem,'rb') as arquivo:
                dados = arquivo.read()
                tipo_imagem = magic.from_buffer(dados, mime=True)
                extensao_imagem = tipo_imagem.split('/')[1]
                nome_arquivo = arquivo.name
                self.mail.add_attachment(dados,maintype='image',subtype=extensao_imagem,filename=nome_arquivo)

    def anexar_arquivo(self,lista_arquivos):
        for item in lista_arquivos:
            with open(item,'rb') as arquivo:
                dados = arquivo.read()
                nome_arquivo = arquivo.name
                self.mail.add_attachment(dados,maintype='application',subtype='octet=stream',filename=nome_arquivo)

    def enviar_email(self,intervalo_em_segundos):
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as email:
            email.login(self.email_origem, self.senha_email)
            email.send_message(self.mail)
            sleep(intervalo_em_segundos)
