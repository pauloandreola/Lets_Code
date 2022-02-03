
arquivo = open('Dom_Casmurro.txt', 'r')
texto = arquivo.read()
print(texto)

print('____________________________________________')
print('')
print('')

arquivo = open('Dom_Casmurro.txt', 'r')
linha = arquivo.readline()
while linha != '':
  print(linha, end='')
  linha = arquivo.readline()
arquivo.close()

print('')
print('')
print('++++++++++++++++++++++++++++++++++++++++++++')
print('')
print('')

arquivo = open('Dom_Casmurro.txt', 'r') # Abrindo arquivo para leitura
for linha in arquivo:
  print(linha, end='')
arquivo.close()  # Fechabdo o arquivo

print('')
print('')
print('********************************************')
print('')
print('')

with open('Dom_Casmurro.txt', 'r') as arquivo: # Com comando with ele abre e fecha o arquivo
    texto = arquivo.read()
    print(texto)

print('')
print('')
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print('')
print('')

with open('Arquivo_teste.txt', 'w') as arquivo:
    arquivo.write('Essa é a primeira linha escrita através do programa Python\n')
    arquivo.write('Essa é a segunda linha escrita através do programa Python\n')

with open('Arquivo_teste.txt', 'r') as arquivo:
    print(arquivo.read(), end='')

print('')
print('')
print('#############################################')
print('')
print('')

with open('Arquivo_teste.txt', 'a') as arquivo:
    arquivo.write('Essa é a terceira linha que escrevi no Python\n')

with open('Arquivo_teste.txt', 'r') as arquivo:
    print(arquivo.read(), end='')    