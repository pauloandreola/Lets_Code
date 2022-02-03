# A função é um importante quando vamos criar um pragrama que vai chamar um comando durante a execução deste programa. Para uma questão de organização, de entendimento de um código e facilidade de alterações o ideal é que para cada processo dentro de um programa seja criado uma função.

# def é uma palavra reservada.

def hello():
  print('Olá mundo!')

hello()

print('')

# Criando uma função chamada calcula_media que recebe 3 valores e faz o cálculo da media destes 3 valores. Ao finalizar o cálculo a função deve retornar o valor para quem chamou, pela palavra reservada return.

def calcula_media(valor1, valor2, valor3):
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media

resultado = calcula_media(10, 10, 10) # Passando 3 valores para a função calcula_média e após a execução retorna o um valor e aloca em resultado.
print(resultado) # Apresentando o conteúdo de resultado.

print('')

#  Abaixo estou passando por parâmetro os 3 valores abaixo só que propositalmente não coloquei os valores na ordem, ou seja, começei pelo valor2, depois valor3 e por último o valor1, mesmo assim como na função calcula_media ele vai calcular conforme está organizado nela.

resultado2 = calcula_media(valor2=9, valor3=10, valor1=9) 
print(resultado2, '.2')

print('')

#  No exemplo abaixo cada comando print vai ser posicionada em uma linha diferente pois esse delimitador é controlador pelo parâmetro end da função print. 

print('Olá')
print(', Paulo')

print('')

# Para ajustarmos a situação acima devemos utilizar o parâmetro end cofnorme abaixo.

print('Olá', end=(' '))
print(', Paulo')

print('Olá', end=(''))
print(', Paulo')

print('Olá,', end=(' '))
print('Paulo')

print('')

#  Outra forma de executar uma função. Sem passar nenhum valor, pois foi utilizado valores default, sem passagem por parâmetro, mas após a execução ele retorna para a função que foi chamada. 

def calcula_media(valor1=0, valor2=0, valor3=0):
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media

resultado = calcula_media()
print(resultado)

# No exemplo abaixo não vai funcionar pois está faltando um valor (valor2) default. Um argumento não padrão, está seguido de uma argumento padrão.

# def calcula_media(valor1=1, valor2, valor3=1):
#     soma = valor1 + valor2 + valor3
#     media = soma / 3
#     return media

# resultado = calcula_media()
# print(resultado)

print('')
print('')
print('')

# Abaixo itens do site da Let's Code https://selecao.letscode.com.br/curso-digital/e44a37c9-4389-46c4-9763-a64adc6d01bf/modulo/a1fac656-3d35-474b-81b7-a74d78d5fa2b/topico/b0ea1c80-8154-4cbe-9893-5f6b7010d399?uuid=70b0a661-d543-439f-8b41-c19c06893c36

def ola(nome):
    print("Olá", nome)

ola("Maria")
# Saída: Olá, Maria

aluno = "João"
ola(aluno)
# Saída: Olá, João

print('')

def dadosPessoais(nome, idade, cidade):
    print("Seu nome é {}, você tem {} anos e mora em {}.".format(nome, idade, cidade))

dadosPessoais("José", 30, "Maceió")
# Saída: Seu nome é José, você tem 30 anos e mora em Maceió.

print('')

dadosPessoais(idade=56, cidade="Florianópolis", nome="Ana")
# Saída: Seu nome é Ana, você tem 56 anos e mora em Florianópolis.

print('')

def somatorio(lista):
    soma = 0
    for item in lista:
        soma = soma + item
    return soma

numeros = [1, 2, 3, 4, 5]
soma_dos_numeros = somatorio(numeros)
print("A soma dos elementos da lista vale: ", soma_dos_numeros)

if somatorio(numeros) > 50:
    print("Que soma grande!")
else:
    print("Que soma pequena!")
    
'''
Saída:
A soma dos elementos da lista vale:  15
Que soma pequena!
'''

print('')

# Nessa função que retorna os valores por recursividade a função recebe o valor 10 vai decrementando e empilhando até chegar ao valor 1. Neste momento ele começa a retornas os valores desempilhando. Como uma pilha de pratos o primeiro a sair é o do topo, ou seja, o último a entrar, ou seja, começa pelo 1 e termina no 10.

def funcaoRecursiva(numero):
  if (numero != 1):
    funcaoRecursiva(numero - 1)
  print(numero)
  if (numero == 10):
    print('Fim')

print("Testando a função recursiva:")
print('')
funcaoRecursiva(10)