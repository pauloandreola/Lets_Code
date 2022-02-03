#  Utilizamos o FOR quando precisamos interar/navegar sobre um objeto... listas 

# Criando uma LISTA e interando com o FOR.

nomes_cidades = ['São Paulo', 'Londres', 'Tóquio', 'Paris']
for nome in nomes_cidades:
  print(nome)

print('')

# Criando uma LISTA e correndo a lista com WHILE.

# Abaixo um laço de repetição com WHILE no qual o resultado é exatamente o mesmo do bloco de código acima e abaixo. Neste caso vamos ter mais linhas de código. Apesar de WHILE ter mais linhs de código ele vai ser necessário quando precisamos combinar mais condições.

contador = 0
nomes_cidades01 = ['Porto Alegre', 'Montevideu', 'Buenos Aires', 'Assunção']
while contador < len(nomes_cidades01):
  print(nomes_cidades01[contador])
  contador = contador + 1

print('')

# TUPLA

# Criando uma TUPLA e interando com um FOR. 

nomes_cidades = 'São Paulo', 'Londes', 'Tóquio', 'Paris' 
for nome in nomes_cidades:
    print(nome)

print('')

# Criando um DICIONÁRIO. Para interar sobre o dicionário, a variável deve ser representativa da chave desse dicionário.

cidade = {
  'Nome': 'Porto Alegre',
  'Estado': 'RS',
  'Populacao_milhoes': 1.5
}     

# Referenciando a chave para apresentar as chaves e os valores

for chave in cidade:
  print(f'{chave} = {cidade[chave]}')

  print('')

# No exemplo abaixo os nomes da lista não serão alterados pois o for criado é uma cópia da lista e não altera a lista original.

nome_cidades02 = ['Porto Alegre', 'Montevideu', 'Buenos Aires', 'Assunção']
for nome in nome_cidades02:
  nome = 'Rio de Janeiro'
print(nome_cidades02)

print('')

# Agora será alterada todos os elementos da lista com a função range pois estou referenciando direto em cada posição da lista.

nome_cidades02 = ['Porto Alegre', 'Montevideu', 'Buenos Aires', 'Assunção']
for posicao in range(len(nome_cidades02)):
  print(posicao) # Este linha foi somente para ver a evolução dos valores/posições da lista
  nome_cidades02[posicao] = 'Rio de Janeiro'
print(nome_cidades02)

print('')

print(list(range(10))) # Retorno de uma lista que começa em 0 e vai até 9.
print(list(range(2,10))) # Retorno de uma lista que começa em 2 e vai até 9.
print(list(range(2,10,2))) # Retorno de uma lista que começa em 2 e vai até 9 com incremento de 2 em 2.


# Abaixo resoluções do site Let's Code https://selecao.letscode.com.br/curso-digital/e44a37c9-4389-46c4-9763-a64adc6d01bf/modulo/a1fac656-3d35-474b-81b7-a74d78d5fa2b/topico/aff10629-157b-4d71-a828-cc5b53480799?uuid=70b0a661-d543-439f-8b41-c19c06893c36

# for (variável temporaria) in (lista):
# instruções...
# ...

fib = [1, 1, 2, 3, 5, 8, 13]
for elemento in fib:
    print(elemento)

# Com 1 parâmetro, ele será interpretado como valor final (exclusivo).
# O valor inicial será 0 e o incremento será 1.

for numero in range(10):
    print(numero)
    # este exemplo imprime os números de 0 a 9, de um em um

# Com 2 parâmetros, o primeiro será o valor inicial (inclusivo) e o
# segundo será o final (exclusivo).
# O incremento continuará sendo 1.

for numero in range(1,11):
    print(numero)
    # este exemplo imprime os números de 1 a 10, de um em um

# Com 3 parâmetros, o terceiro será interpretado como incremento.
for numero in range(1,20,2):
    print(numero)
    # este exemplo imprime os ímpares positivos menores do que 20
    # ele começa valendo 1 e salta de 2 em 2 até atingir ou passar 20

# O incremento pode ser também um decremento (incremento negativo).
for numero in range (10,0,-1):
    print(numero)
    #Imprimindo os números de 1 a 10 em ordem decrescente