# !pip install requests # instalando uma biblioteca
import requests # importando a biblioteca requests

url01 = 'https://api.exchangerate-api.com/v6/latest' # URL definida para ser chamada

url02 = 'https://open.er-api.com/v6/latest/USD' # Outra URL a ser chamada

req01 = requests.get(url01) # Fazendo a requisição da URL por "get" 

retorno = requests.get(url02) # Podemos fazer a requisição por "post" se for alterar os dados

# print(req01.status_code)  # Aprendi a buscar o retorno neste formato no Jupyter

# print(retorno.status_code) # Aprendi a buscar o retorno neste formato no Jupyter

# print(req01) # Funcionou neste formato também no Replit

# print(retorno) # Funcionou neste formato também no Replit

dados01 = req01.json() # fazendo requisição por JSON - Java Script Object Notation

dados02 = retorno.json() #

print(dados01)  # Imprimindo resultado da captura do material do site

# print('++++++++++++++++++++++++++++++++++++++++++++++')

# print(dados02)  # Imprimindo resultado da captura do material do site

real = float(input('Qual é o valor em Reais a ser convertido: R$ '))
cotacao = dados01['rates']['BRL']
print(f'R$ {real} em dólar valem US$ {(real / cotacao):.2f}')

dolar_australiano = float(input('Qual é o valor em Dólar Australiano a ser convertido: AUD$ '))
cotacao = dados01['rates']['AUD']
print(f'AUD$ {dolar_australiano} em dólar valem US$ {(dolar_australiano / cotacao):.2f}')

peso_argentino = float(input('Qual é o valor em Peso Argentino a ser convertido: ARS$ '))
cotacao = dados01['rates']['ARS']
print(f'ARS$ {peso_argentino} em dólar valem US$ {(peso_argentino / cotacao):.2f}')

