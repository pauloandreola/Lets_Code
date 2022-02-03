idade = int(input('Digite uma idade entre 0 e 150: '))
if (idade >= 0 or idade <= 150):
    print('Ok, a idade digitada é de: ',idade) 
else:
    print('Você digitou uma idade fora dos paramêtros solicitados.')
    print('')

salario = float(input('Digite um salário maior que 0 (Zero): '))
if (salario > 0):
    print('Ok, valor do salário digitado foi de: R$',salario)
else:
    print('Você digitou um valor de salário fora dos paramêtros solicitados.')
    print('')

opcao = str(input('Digite o seu sexo conforme as opções: M, F ou Outro: '))
sexo = opcao.upper().strip
if (sexo == 'M' or sexo == 'F' or sexo == 'OUTRO'):
    print('Ok, o sexo definido foi: ',sexo)
else:
    print('Você digitou uma informação inválida')