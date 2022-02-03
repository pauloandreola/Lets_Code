valor_passagem = 4.3

valor_corrida = input('Qual é o valor da corrida 1 ? ')

if float(valor_corrida) <= valor_passagem * 5:
    print('Pague a corrida')
if float(valor_corrida) > valor_passagem * 5:
    print('Vá o ônibus')
print('')

valor_corrida = input('Qual é o valor da corrida 2 ? ')

if float(valor_corrida) <= valor_passagem * 5:
    print('Pague a corrida')
else:
    print('Vá de ônibus')
print('')

valor_corrida = input('Qual é o valor da corrida 3 ? ')

if float(valor_corrida) <= valor_passagem * 5:
    print('Pague a corrida')
else:
    if float(valor_corrida) <= valor_passagem * 6:
        print('Aguarde um mommento o valor pode baixar')
    else:
        print('Vá de ônibus')
print('')

valor_corrida = input('Qual é o valor da corrida 4 ? ')

if float(valor_corrida) <= valor_passagem * 5:
    print('Pague a corrida')
elif float(valor_corrida) <= valor_passagem * 6:
    print('Aguarde um instante, o valor pode baixar')
else:
    print('Vá de ônibus')