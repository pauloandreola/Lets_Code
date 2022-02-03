contador = 0

while contador < 10:
    contador = contador +1
    if contador ==1:
      print(contador, 'item limpo')
    else:
      print(contador, 'itens limpos')

print('Fim da repetição do bloco while')
print('')

contador = 0

while  contador < 10:
    contador = contador + 1
    if contador == 1:
      continue
    print(contador, 'itens limpos')  

print('Fim da reprodução de mais um bloco de while')

contador = 0

while True:
    if contador <= 10:
        contador = contador +1
        if contador == 1:
            print(contador, 'item limpo')
        else:
            print(contador, 'itens limpos')
    else:
        break

print('Novamente fim da repetição do bloco while')
print('')

senha = input('Digite sua senha: ')

while senha != 'LetsCode':
    senha = input('Senha inválida, tente novamente: ')

print('Acesso permitido')