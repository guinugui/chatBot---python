import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import math

url = 'https://www.kabum.com.br/espaco-gamer/cadeiras-gamer'

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
qtd_itens = soup.find('div', id='listingCount').get_text().strip()

index = qtd_itens.find(' ')
qtd = qtd_itens[:index]

ultima_pagina = math.ceil(int(qtd)/ 20)

dic_produtos = {'marca':[], 'preco':[]}

df = pd.DataFrame(dic_produtos)

for i in range(1, ultima_pagina+1):
    url_pag = f'https://www.kabum.com.br/cadeiras/cadeiras-gamer?page_number={i}&page_size=20&facet_filters=&sort=most_searched'
    site = requests.get(url_pag, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    produtos = soup.find_all('article', class_=re.compile('productCard'))
    
    for produto in produtos:
        marca = produto.find('span', class_=re.compile('nameCard')).get_text()
        preco_elemento = produto.find('span', class_=re.compile('oldPriceCard'))
        preco = preco_elemento.get_text() if preco_elemento else None  # Assign None if not found

        print(marca, preco)
