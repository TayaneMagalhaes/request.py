import requests
## url = "https://httpbin.org/get"
url = "https://httpbin.org/post"
data = {
    "pessoa": { "nome": "Robson", "idade": 30, "profissao": "Programador"
    
    }
}

params = {
    dataInicio: "2026-01-01",
    dataFim: "2027-12-31"
}

##response = requests.get(url)
response = requests.post(url, json=data, params=params )
print(response) 
print(response.text)