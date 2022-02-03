# Arquivo 'alunos.csv' importado da minha base de teste
import csv

with open('alunos.csv','r') as lista:
  tabela = csv.reader(lista)
  for i, linha in enumerate(tabela):
    if i == 0:
      print('Cabeçalho: ', linha)
    else:
      print('Valor: ', linha)

      # - Nesta versão estou utilizando a boa pratica de abrir o arquivo como consta no link abaixo, utlizando somente a função 'r' -  https://pt.stackoverflow.com/questions/97269/como-ler-um-arquivo-csv-em-python

      #  - Utlizando a variável 'i' para tratar a diferença entre o cabeçalho e os valores da tabela conforme o link abaixo no tempo de 11:25 - https://www.youtube.com/watch?v=AnJPtKLtc7o