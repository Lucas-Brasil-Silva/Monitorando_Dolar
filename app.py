import schedule
from time import sleep
import os

os.chdir('Monitorando_dolar')

def rodar_botcotacaodolar():
    os.system('scrapy crawl botcotacaodolar')

schedule.every(1).minutes.do(rodar_botcotacaodolar)

while True:
    schedule.run_pending()
    sleep(1)