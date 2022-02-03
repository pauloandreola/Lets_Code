import csv

with open('BrasilCovid.csv','r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    for linha in leitor:
      print(linha)

print('')
print('________________________________________________________________')
print('')

# Tirando o cabeçalho e reservando na variável header
# Apresentando a relação com 1 ou mais novos_casos

with open('BrasilCovid.csv', 'r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    header = next(leitor)
    for linha in leitor:
      if float(linha[2]) >= 1:
        print(linha)

print('')
print('*****************************************************************')
print('')

with open('BrasilCovid.csv', 'r') as csv_arquivo:
    linhas = csv_arquivo.read()
    linhas = linhas.split('\n')
    for linha in linhas:
        linha = linha.split(',')
        print(linha)

print('')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('')

with open('users.csv', 'w') as arquivo_users:
    escritor = csv.writer(arquivo_users)
    escritor.writerow(['nome', 'sobrenome', 'email', 'genero'])
    escritor.writerow(['Paulo', 'Andreoila', 'pauloandreola@gmail.com', 'M'])


header = ['Nome', 'Sobrenome']
dados = []
opcao = input('O que deseja fazer?\n1 - Cadastrar\n0 - Sair\n')
while opcao != '0':
  x = input('Qual é o nome? ')
  nome = x.title() 
  y = input('Qual é o sobrenome? ')
  sobrenome = y.title()
  dados.append([nome,sobrenome])
  opcao = input('O que deseja fazer?\n1 - Cadastrar\n0 - Sair\n')

print(dados)

print('')
print('')

with open('novos_usuarios.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(header)
    writer.writerows(dados)

with open('novos_usuarios.csv', 'r') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  for row in csv_reader:
    print(row)    

#  Abaixo exemplos retirados do site da Let's Code site https://selecao.letscode.com.br/curso-digital/e44a37c9-4389-46c4-9763-a64adc6d01bf/modulo/adfb8173-da5a-49a7-a2d0-780708f19ba2/topico/389b3d6b-2e52-44b5-9f01-22d4459047e0?uuid=70b0a661-d543-439f-8b41-c19c06893c36

# import csv

# with open('tabelaExemplo.csv', 'w') as arquivo:
#     escritor = csv.writer(arquivo, delimiter = ';', lineterminator = '\n') #criando um escritor
#     lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#     escritor.writerows(lista) # writerows escreve cada "sublista" da lista como uma linha

# with open('tabelaExemplo.csv', "r") as arquivo:
#     leitor = csv.reader(arquivo, delimiter = ';', lineterminator = '\n') #criando um leitor
#     print("O conteúdo do arquivo é:")
#     print(leitor)
#     for linha in leitor:
#         print(linha)


# import csv

# with open('email.csv', 'r') as emails:
#     leitor = csv.DictReader(emails, delimiter=';') #a primeira linha é lida como um cabeçalho
#     for linha in leitor:
#         print(linha['Login email']) #podemos chamar um valor específico de cada linha pela chave no cabeçallho


# with open('names.csv', 'w', newline='') as csvfile:
#     chaves = ['first_name', 'last_name'] # definimos o cabeçalho
#     writer = csv.DictWriter(csvfile, fieldnames=chaves) # especificamos o cabeçalho

#     writer.writeheader() # escrevemos o cabeçalho
#     writer.writerow({'first_name': 'Senhor', 'last_name': 'Batata'}) # escrevemos linhas com as chaves e valores
#     writer.writerow({'first_name': 'Will', 'last_name': 'Smith'})
#     writer.writerow({'first_name': 'Elon', 'last_name': 'Musk'})
