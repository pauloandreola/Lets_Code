# Um dicionário é composto por chaves e valores das chaves.
# O dicionário é totalmente flexível, podemos manipular/alterar/incluir/excluir tanto chaves como os valores. Cuidar quando for manipular o dicionário. 
# Para adicionar ou mudar itens em um dicionario utilizar updade(), ou criamos diretamente chaves e valores.
# Para remover itens de um dicionário podemos utilizar pop()/popitem()/del/clear().

dados_cidade = {
  'nome': 'Porto Alegre',
  'estado': 'RS',
  'area km2': 500,
  'populacao_milhoes': 1.500
}

#  Posso construir o meu dicionário conforme abaixo, vai ser o mesmo formato acima.

# dados_cidade = {'nome': 'Porto Alegre', 'estado': 'RS', 'area km2': 500,  'populacao_milhoes': 1.500}

print(type(dados_cidade)) # Tipo de dados.
print('')

print(dados_cidade)
print('')

for valores in dados_cidade: # Fazendo um FOR para apresentar os valores das chaves do dicionário.
  print(dados_cidade[valores])
print('')

for chaves in dados_cidade.keys(): # Apresentando as chaves do dicionário.
  print(chaves)
print('')

for valores in dados_cidade.values(): # Apresentando os valores do dicionário.
  print(valores)
print('')

for chaves, valores in dados_cidade.items(): # Apresentando as chaves e os valores do dicionário.
  print(chaves, ': ', valores)

dados_cidade['pais'] = 'Brasil' # incluindo uma chave e um valor dentro de um dicionário.
print('')

print(dados_cidade)
print('')

print(dados_cidade['nome']) # Aecssando um valor que está contido na chave nome.
print('')

dados_cidade['populacao_milhoes'] = 1.2 # Alterando o valor da chave populacao_milhoes.
print(dados_cidade)
print('')

dados_cidade2 = dados_cidade
dados_cidade2['nome'] = 'Canoas' # Alterando o valor da chave nome para o dicionário. Neste caso os valroes de ambos dicionários serão alterados.
print(dados_cidade)
print('')

print(dados_cidade2)
print('')

dados_cidade3 = dados_cidade.copy() # Utilizando o comando copy para copiar para um novo dicionário.
print('')

dados_cidade['nome'] = 'Porto Alegre' # Atualizei o valor da chave nome em dados_cidade e dados_cidade2.
print(dados_cidade)
print(dados_cidade2)
print(dados_cidade3) # Como o dados_cidade3 foi copiado de dados_cidade ele não será alterado.
print('')

novos_dados = { # gerando e/ou atualizando chaves e valores para incluir em dicionário existente.
    'area_km2': 121,
    'populacao_milhoes': 323,
    'fundacao': '27/07/1939'
}
dados_cidade3.update(novos_dados) # inserindo novas chaves e valores somente no dicionário dados_cidade3.

novos_dados2 = { # gerando e/ou atualizando chaves e valores para incluir em dicionário existente.
    'populacao_milhoes': 1.5,
    'fundacao': '26/03/1772'
}
dados_cidade.update(novos_dados2) # atualizando os valores nos dicionários dados_cidade2 e dados_cidade
print('')

print(dados_cidade)
print(dados_cidade3)
print('')

print(dados_cidade.get('prefeito')) # Verificar se existe o valor no dicionário. Quando não contém o retorno é None.
print('')

print(dados_cidade.keys()) # retorna uma lista de chaves de um dicionário
print('-----')

print(dados_cidade.values()) # retorna uma lista de valores de um dicionário
print('_____')

print(dados_cidade.items()) # retorna uma lista de tuplas (chave, valor) de um dicionário

# Abaixo resolução do site  da Let's Code: https://selecao.letscode.com.br/curso-digital/e44a37c9-4389-46c4-9763-a64adc6d01bf/modulo/a1fac656-3d35-474b-81b7-a74d78d5fa2b/topico/3366dd58-ca50-44fa-a286-1fabb1beeffd?uuid=70b0a661-d543-439f-8b41-c19c06893c36

# O dicionário é definido pelos símbolos { e }

dicionario = {}

# O dicionário não possui um "append".
# Adicionamos valores diretamente:

dicionario['cat'] = 'gato'
dicionario['dog'] = 'cachorro'
dicionario['mouse'] = 'rato'

print(dicionario)
print(type(dicionario))

'''
Saída:
{'cat': 'gato', 'dog': 'cachorro', 'mouse': 'rato'}
<class 'dict'>
'''

# Dicionários, assim como as listas, são mutáveis:
dicionario['dog'] = 'cão'
print(dicionario)
# Saída: {'cat': 'gato', 'dog': 'cão', 'mouse': 'rato'}

# Podemos criar o dicionário diretamente também:
dicionario2 = {'Curso': 'Python Pro', 'Linguagem':'Python', 'Módulo':2}
print(dicionario2)
# Saída: {'Curso': 'Python Pro', 'Linguagem': 'Python', 'Módulo': 2}

# Podemos utilizar o operador "in" para verificar se uma chave existe:
if 'cat' in dicionario:
    print('cat existe!') # Sim
if 'bird' in dicionario:
    print('bird existe!') # Não
if 'gato' in dicionario:
    print('gato existe!') # Não

'''
Também podemos utilizar as funções .keys() e .values() para obter listas
com apenas as chaves ou apenas os valores do dicionário.
'''
chaves = dicionario.keys()
print(chaves)
# Saída: dict_keys(['cat', 'dog', 'mouse'])

valores = dicionario.values()
print(valores)
# Saída:dict_values(['gato', 'cão', 'rato'])

# Já a função .items(), retorna uma lista de tuplas (chave, valor) de um dicionário

itens = dicionario.items()
print(itens)
# Saída:dict_items([('cat', 'gato'), ('dog', 'cão'), ('mouse', 'rato')])

# Abaixo substituindo novos dados no dicionário dados_cidade

# dados_cidade = {
#   'nome': 'Gravataí',
#   'estado': 'RS',
#   'area km2': 463,
#   'populacao_milhoes': 255,
#   'pais': 'Brasil',
#   'fundacao': '08/04/1763'

# }

# print(dados_cidade)