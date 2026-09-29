import requests
from pprint import pprint

url = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios?orderBy=nome"
params = {
    "view": "nivelado"
}


response = requests.get(url)
try:
    response.raise_for_status()
except requests.HTTPError as e:
    print(f"Erro no request: {e}")
    response = None
else:
    resultado = response.json() 
    pprint(resultado)