"""
Biblioteca
Automatizar o teclado (Pyautogui)
Automatizar acesso ao site(webbrowser)
Automatizar digitação (link whatsapp)
Automatizar leitura de dados de uma planilha de contatos(openpyxl)
"""

import openpyxl as xls
#ler planilha e guardar dados

leituraAquivoDeContatos = xls.load_workbook('Numeros.xlsx') #Conseguia ler todo o aquivo xlsx/planilho de contatos

PaginaContatos = leituraAquivoDeContatos['Página1']#planilhas pode ter varias paginas entao, referancie a que voce deseja ler

for linha in PaginaContatos.iter_rows(min_row = 2): # vai percorrer todas as linhas apartir da linha 2 que esta començando os dados, linha 1 = e nome e telefone 
    
    nome = linha[0].value
    telefone = linha[1].value
    print(nome)
    print(telefone)
    

#acessar o whatsappWeb (Link) com contato e a mensagem em criptografia

#insira a planilha dentro da pasta aonde se localiza o arquivo python






