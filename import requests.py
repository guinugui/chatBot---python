import requests
from bs4 import BeautifulSoup
import json

# URL da página com os dados de vendas por UF
url = "https://desenvolvedores.migrate.info/2019/05/tabela-de-codigos-ibge-de-uf-e-municipios/"

# Realiza a requisição GET para obter o conteúdo da página
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida (código 200 indica sucesso)
if response.status_code == 200:
    # Parseia o conteúdo HTML da página
    soup = BeautifulSoup(response.content, "html.parser")

    # Encontrar a tabela de vendas por UF (ajuste conforme a estrutura HTML da página)
    table = soup.find("table")

    # Inicializa uma lista vazia para armazenar as linhas da tabela
    rows_data = []

    # Itera sobre as linhas da tabela, excluindo a primeira linha que é geralmente o cabeçalho
    for row in table.find_all("tr")[1:]:
        # Extrai o texto de cada célula da linha
        cells = row.find_all("td")
        uf = cells[0].get_text(strip=True)  # UF
        valor_venda = cells[1].get_text(strip=True)  # Valor total de venda

        # Adiciona os dados da linha à lista de linhas
        rows_data.append([uf, valor_venda])

    # Monta o JSON final com os dados dinâmicos para substituir a seção "rows"
    dynamic_data = {
        "type": "Section",
        "options": {
            "section_title": "Venda por UF"
        },
        "components": [
            {
                "type": "Table",
                "options": {
                    "title": "",
                    "headings": [
                        "UF",
                        "Valor Total Venda"
                    ],
                    "striped": True,
                    "rows": rows_data  # Aqui substituímos as linhas estáticas pelas dinâmicas
                }
            }
        ]
    }

    # Converte o JSON para uma string formatada
    dynamic_json_str = json.dumps(dynamic_data, indent=2, ensure_ascii=False)
    print(dynamic_json_str)  # Exibe o JSON formatado com os dados dinâmicos
else:
    print("Erro ao obter os dados da página:", response.status_code)
