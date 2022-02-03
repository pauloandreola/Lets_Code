import csv

with open('alunos.csv','r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    for linha in leitor:
      print(linha)