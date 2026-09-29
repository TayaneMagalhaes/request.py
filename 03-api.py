import requests
from pprint import pprint
nome = input("Digite o nome que deseja pesquisar: \n ")
url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"
params = {
    "localidade": 33 #rj
}

response = requests.get(url, params=params)
try:
    response.raise_for_status()
except requests.HTTPError as e:
    print(f"Erro no request: {e}")
    response = None
else:
    resultado = response.json() 
    pprint(resultado[0]['res'])