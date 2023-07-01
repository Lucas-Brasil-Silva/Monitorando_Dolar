import scrapy
from email_model import Email

class CotacaoDolarSpyder(scrapy.Spider):
    name = 'botcotacaodolar'
    urls = ['https://br.investing.com/currencies/usd-brl']

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url,callback=self.parse)
    
    def parse(self,response):
        cotacao_dolar = response.xpath("//div[@data-test='instrument-header-details']//span//text()").get()
        mensagem = f'A Cotação do dolar esta atualmente em R$ {cotacao_dolar}.'
        contatos = ['E-mails destinatario']
        email = Email('E-mail conta de login','Senha para aplicação e-mail')
        email.defenior_conteudo(email_remetente='e-mail',lista_de_contatos=contatos,
                    topico='Cotação Dolar',conteudo_email=mensagem)
        email.enviar_email(30)