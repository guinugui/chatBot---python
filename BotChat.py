"""
Biblioteca
Automatizar o teclado (Pyautogui)
Automatizar acesso ao site(webbrowser)
Automatizar digitação (link whatsapp)
Automatizar leitura de dados de uma planilha de contatos(openpyxl)
"""

import openpyxl as xls
from urllib.parse import quote # formatar para links expeciais
import webbrowser #usado para conseguir abrir o navegador
from time import sleep
import pyautogui as gui
import os

webbrowser.open('https://web.whatsapp.com/')
sleep(15)
"""
validaçao para que que funcione o cliente tem que estar logado no wppweb
ele vai ficar parado durante 40s ate que ele acesse o wppweb, assim que passar os 40s
o sistema continua.
"""


#ler planilha e guardar dados

leituraAquivoDeContatos = xls.load_workbook('Numeros.xlsx') #Conseguia ler todo o aquivo xlsx/planilho de contatos

PaginaContatos = leituraAquivoDeContatos['Página1']#planilhas pode ter varias paginas entao, referancie a que voce deseja ler

for linha in PaginaContatos.iter_rows(min_row = 2): # vai percorrer todas as linhas apartir da linha 2 que esta començando os dados, linha 1 = e nome e telefone

    nome = linha[0].value # vai ler na planilha o index 0 = coluna A na planilha
    telefone = linha[1].value # vai ler na planilha o index 0 = coluna B na planilha
    mensagem = f'Olá {nome}, tudo bem ?'


#acessar o whatsappWeb (Link) com contato e a mensagem em criptografia

    try:
        linkMensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
        #abra o navegador com o link expecifico
        webbrowser.open(linkMensagem_whatsapp)
        sleep(10)
        gui.press('enter')
        sleep(5)
        gui.hotkey('ctrl', 'w')
        sleep(5)
    except Exception as e:
        print(e)
        print(f'Nao foi possivel enviar mensagem para {nome}')
        with open('erros.csv', 'a', newline='', encoding='utf-8') as arquivo:
            arquivo.write(f'{nome}, {telefone}{os.linesep}')

#insira a planilha dentro da pasta aonde se localiza o arquivo python