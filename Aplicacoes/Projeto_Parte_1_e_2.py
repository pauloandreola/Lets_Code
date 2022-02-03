import requests as r
import datetime as dt

# A url API abaixo vai ser armazenada na variável url.

url = 'https://api.covid19api.com/country/brazil'

# Fazendo a requisição de uma url e armazenando na variável resp.

resp = r.get(url)

# print(resp.status_code)

# Recuperando os dados desta requisição e armazenando na variável raw_data com json transformando o conteúdo em um dicionário.

raw_data = resp.json()

# print(raw_data[0])

# Criando uma lista final_data.

final_data = []

# Interando com os dados raw_data e inserindo as informações na lista final_data dos dados que queremos interar. Fazendo uma lista de listas.

for obs in raw_data:
  final_data.append([obs['Confirmed'], obs['Deaths'], obs['Recovered'], obs['Active'], obs['Date']])

# Inserindo um cabeçalho/header na lista final_data identificando cada um dos campos.

final_data.insert(0, ['Confirmados', 'Mortes', 'Recuperados', 'Ativos', 'Data']) 
# print(final_data)

# Criando variáveis para serem "constantes" para referenciar posições dos valores dentro da lista.

CONFIRMADOS = 0
OBITOS  = 1
RECUPERADOS = 2
ATIVOS = 3
DATA = 4

# Gerando um for para limpar os valores das datas na lista na posição DATA, com esse procediemnto será mantido os primeiros 10 (posições de 0 a 9) caracteres da coluna DATA/data e os demais serão excluidos.

for i in range(1, len(final_data)):
  final_data[i][DATA] = final_data[i][DATA][:10]

# print(final_data)

# Criando um arquivo Brasil-covid com formado CSV e armazenando as chaves e os valores dentro desse arquivo. Writerows escreve a lista das listas

import csv

with open('Brasil-covid.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(final_data)

# Esse for serve para transformar os valores constido na chave/campo data/DATA que  estão em formato string para formato date (data).

for i in range(1, len(final_data)):
    final_data[i][DATA] = dt.datetime.strptime(final_data[i][DATA], '%Y-%m-%d')

# print(final_data)

# Função criada para construir os dados de Y e uma lista que contem os dados.

def get_datasets(y, labels):
    if type(y[0]) == list: # Verificando se o tipo de Y é uma lista.
        datasets = []  # Criando lista datasets contendo valores de y e o label de cada uma delas.
        for i in range(len(y)): # Percorrendo todo o conteúdo de Y.
              datasets.append({ # Incluindo na lista datasets um dicionário que contem a chaves...  
                  'label': labels[i], # chave label que contem a lista de labels.
                  'data': y[i]  # chave data que contem a lsita de Y.
              })
        return datasets # retornando os valores contidos em datasets.
    else:  # Caso o Y não seja uma lista de listas.
      return[
        {
            'label': labels[0], # Vai retornar uma lista de um valor do dicionário.
            'data': y  
        }
      ]

# Função para definir o título do gráfico e se apresenta ou não.

def set_title(title=''): # Caso não seja informado o título a retorno será vazio.
  if title != '':   # Verificando se title está vazio, se é diferente de vazio.
    display = 'true' # Se é diferente de vazio display recebe true.
  else:
    display = 'false'  # Se é vazio recebe false.
  return {
    'title': title,  # Retornando um dicionário que tem uma chave título.
    'display': display # Se estiver valor na chave title ele vai apresentar o título, caso esteja vazio não apressenta o título.
  }         

# Função que cria o dicionário que representa o gráfico

def create_chart(x, y, labels, kind='bar', title=''): # Os valores de x, y, labels, tipo de gráfico e o título

  datasets = get_datasets(y, labels) # Criando a variável datasets para receber os valores de Y e labels.
  options = set_title(title) # Criando a variável options para receber o título e itens referente a API.

  chart = {  # Criando o dicionário que representa o gráfico.
      'type': kind, # Chave type que é o valor de kind para referenciar o tipo de gráfico.
      'data': { # Criando a chave data que também é um dicionário com as chaves labels e datasets.
          'labels': x, # Chave labels recebe os valores de X.
          'datasets': datasets # Chave datasets recebe o valor de datasets 
      },
      'options': options # A chave options responsável pelo setup de algumas informações além do título e pode ser usado para identificação dos eixos.  
  }

  return chart

# Função que vai fazer a requisição na API utlizando o dicionário.

def get_api_chart(chart): # Recebendo o chart que é o dicionário criado acima.
  url_base = 'https://quickchart.io/chart' # Variável url_base que recebe a os dados da URL.
  resp = r.get(f'{url_base}?c={str(chart)}') # A variável resp vai guardar a requisição feita pela API.   
  return resp.content # Nesse caso como estou recebendo um valor binário (gráfico), utilizo o content (conteúdo) do arquivo.

# Função para salvar a imagem do gráfico.

def save_image(path, content):  #  Chamando o caminho (path) e o conteúdo (content) do arquivo
  with open(path, 'wb') as image: # Armazenar o arquivo e wb para escrever o valor bin[ario]
    image.write(content)  # Escrevendo o conteúdo em image

# Função para apresentar o gráfico. Abaixo a importação da bibliotecas para isso.

from PIL import Image

from IPython.display import display

# Funão para mostrar o gráfico.

def display_image(path): # Recebendo o caminho do arquivo
  img_pil = Image.open(path)  # Armazenando em img_pil o retorno de função open do módulo Image importada acima passando o caminho (path).
  display(img_pil) # Chama função display importada acima passando o valor de img_pil.

# Criando os dados de CONFIRMADOS E RECUPERADOS no gráfico em barras. Será criado dados de 60 em 60 dias (2 meses) devido a quantidade de dados

y_data_1 = [] # Criando a lista para inserir os dados de CONFIRMADOS
for obs in final_data[1::60]: # Começando em 1 para ignorar o header/ cabeçalho, pulando dados de 60 em 60 devido a quantidade de valores.
  y_data_1.append(obs[CONFIRMADOS]) # Popular os valores que estão em obs na posição CONFIRMADOS em y_data_1 

y_data_2 = [] # Criando a lista para inserir os dados de RECUPERADOS
for obs in final_data[1::60]: # Começando em 1 para ignorar o header/ cabeçalho, pulando dados de 60 em 60 devido a quantidade de valores.
  y_data_2.append(obs[RECUPERADOS]) # Popular os valores que estão em obs na posição CONFIRMADOS em y_data_2

labels = ['Confirmados', 'Recuperados'] # Criando os labels  

x = [] # Criando a lista x
for obs in final_data[1::60]: # Começando em 1 para ignorar o header/ cabeçalho, pulando dados de 60 em 60 devido a quantidade de valores.
  x.append(obs[DATA].strftime('%d/%m/%Y')) # Popular os valores que estão em obs na posição DATA em x. Porém os valores são tipo tempo e por isso para facilitar, (não é necessário) vou alterar para formato string como o comando strftime. É preciso passar o formato que precisa ser apresentado.

# strftime - Transforma de datetime para string.
# strptime - Transforma de string para datetime.

# Criando/renderizando o gráfico

chart = create_chart(x, [y_data_1, y_data_2], labels, title = 'Gráfico cofirmados vs recuperados' ) # y_data_1 e y_data_2 passando em formato de lista
chart_content = get_api_chart(chart) 
save_image('meu-primeiro-grafico.png', chart_content)
display_image('meu-primeiro-grafico.png')

# Gerar QRCode para compartilhar o gráfico.

from urllib.parse import quote

# Função para gerar QRCode 

def get_api_qrcode(link):  
  text = quote(link)  # parsin do link para url
  url_base = 'http://quickchart.io/qr' # Passando para a variável url_base a url que vai ser utilizado para gerar o QRCode.
  resp = r.get(f'{url_base}?text={text}') # Em resp vai ser armazenado a requisição da url_base para receber o link de redirecionamento text.
  return resp.content # Retornando o conteúdo de resp para exibir o conteúdo da função display_image que já foi criado. 

url_base = 'https://quickchart.io/chart' # Reutilizando a url_base em get_api_chart
link = f'{url_base}?c={str(chart)}' # Construção do link, mesma utilizada em get_api_chart
save_image('qr-code.png', get_api_qrcode(link)) # Salvando o QRCode no arquivo indicado recebendo o conteúdo (content) passado pela função get_api_qrcode
display_image('qr-code.png')  # Gerando a visualização do QRCode


# Exemplo da função datetime

# import datetime as dt

# print(dt.time(16, 30, 0, 0), 'Hora:minuto:segundo') # O Microsegundo é desconsiderado se valor for zero
# print(dt.time(16, 30, 0, 7), 'Hora:minuto:segundo:microsegundo')
# print('-----')
# print(dt.date(2022, 1, 24),  'Ano-mês-dia')
# print('-----')
# print(dt.datetime(2022, 1, 24, 16, 30, 0, 0), 'Ano-mês-dia Hora:minuto:segundo:microsegundo ')

# print('-----')
# print('-----')
# print('-----')

# natal = dt.date(2021, 12, 25)
# reveilon = dt.date(2022, 1, 1)

# tempo = reveilon - natal

# print(reveilon - natal)
# print((tempo).days)
# print((tempo).seconds)
# print((tempo).microseconds)

 
# Abaixo exemplos da Let's Code no site:  https://selecao.letscode.com.br/curso-digital/e44a37c9-4389-46c4-9763-a64adc6d01bf/modulo/adfb8173-da5a-49a7-a2d0-780708f19ba2/topico/ddb966e6-7787-414c-9d23-accefea6f974?uuid=70b0a661-d543-439f-8b41-c19c06893c36

# import datetime

# d = datetime.date(2001, 9, 11)
# tday = datetime.date.today()
# print(tday, d)


# # datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

# tdelta = datetime.timedelta(hours=12)
# print(tday + tdelta)


# bday = datetime.date(1975, 7, 8)
# till_bday = bday - tday
# print(till_bday.days)

# dt_agora = datetime.datetime.now()
# print('********')
# print(dt_agora.strftime('%B %d, %Y'))
# print(dt_agora.strftime('%b %d, %Y'))
# print('********')

# dt_str = 'July 08, 1975'
# dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
# print(dt)

# strftime - Datetime para String
# strptime - String para Datetime