#  - Diferenças entre Tuplas e Listas:
#  - Lista são flexíveis, podemos editar, remover, adicionar.
#  - Tupla não podemos editar, remover e adicionar.
#  - Na tupla uma vez definida não podemos fazer qualquer alteração.
#  - A tupla permite algumas implementações que a Lista não atende.
#  - A Tupla [e um pouco menor que a lista em função da sua rigidez.
#  - Se é puder sempre que possível utilizar uma Tupla ao invês da Lista.

#  - Lista
print('')
nomes_paises = ['Brasil', 'Argentina', 'China', 'Canadá', 'Japão']
print(nomes_paises, type(nomes_paises))
print('Tamanho da lista: ', len(nomes_paises)) 
print('')
print('Nome do País: ', nomes_paises[4])
print('Nome do País: ', nomes_paises[-1])
print('')
nomes_paises[4] = 'Colômbia'
print('País: ', nomes_paises[4])
print(nomes_paises)
print('')
# nomes_paises[5] = 'Chile' # - Não vai funcionar pois está fora do alcance da lista
print('')

# Fazer slice na lista. O índice final não é apresentado

print(nomes_paises[1:3])
print(nomes_paises[1:-1])
print(nomes_paises[2:])
print(nomes_paises[:3])
# Os dois comandos abaixo retornam o mesmo resultado, ou seja toda a lista
print(nomes_paises[:])
print(nomes_paises)
print(nomes_paises[::2])
print(nomes_paises[::-1])
print('Brasil' in nomes_paises)
print('Canadá' not in nomes_paises)
print('')
lista_capitais = []
lista_capitais.append('Brasília')
lista_capitais.append('Buenos Aires')
lista_capitais.append('Pequim')
lista_capitais.append('Bogotá')
print(lista_capitais)
lista_capitais.insert(2, 'Paris')
print(lista_capitais)
lista_capitais.remove('Buenos Aires')
print(lista_capitais)
cidade_removida = lista_capitais.pop(2)
print(lista_capitais, cidade_removida)
print('')

# - Tupla

nomes_paises_tupla = 'Brasil', 'Argentina', 'China', 'Canadá', 'Japão'
print(nomes_paises_tupla, type(nomes_paises_tupla))
nome_estado = 'Rio Grande do Sul'
print(nome_estado, type(nome_estado))
len(nomes_paises_tupla)
nomes_paises_tupla[0]
# - Abaixo 'Unpack', algo que a Tupla faz que a Lista não faz
b, a, c, ca, j = nomes_paises_tupla
print(c, b, j)
# - Imprimindo a lista de dados que foi desempacotado 'Unpacked'
print(*nomes_paises_tupla) 
print('')
print('')
print('')


#  Abaixo exemplos no site da Lets' Code https://selecao.letscode.com.br/curso-digital/e44a37c9-4389-46c4-9763-a64adc6d01bf/modulo/a1fac656-3d35-474b-81b7-a74d78d5fa2b/topico/24338f84-0512-4dc6-b0c9-098af07ad0c0?uuid=70b0a661-d543-439f-8b41-c19c06893c36

print("Abaixo exemplos no site da Let's Code")
# Criando uma lista vazia.
listavazia = []

# Criando uma lista com alguns valores.
numeros = [1, 3, 7, 8, 9]

# Listas podem mesclar diferentes tipos de valores.
listamista = [14, "let's code", 0.1, True]

# Acessamos cada elemento da lista através de um índice entre colchetes.
# Os índices começam em 0.
print(numeros[0])
print(numeros[1])
print(numeros[2])
print(numeros[3])
print(numeros[4])

# Listas são mutáveis: podemos alterar o valor de seus itens.
numeros[2] = 5
print(numeros)

# Um jeito inteligente de trabalhar com listas é utilizando loops.
indice = 0
while indice < 5:
    print(numeros[indice])
    indice = indice + 1

print('')

indice = 0
while indice < len(numeros):
    print(numeros[indice])
    indice = indice + 1

print('')

animais = []
resposta = 's'
while resposta == 's' or resposta == 'S':
    resposta = input('Deseja adicionar um animal à lista (s/n)? ')
    if (resposta == 's' or resposta == 'S'):
        animal = input('Digite o nome do animal: ')
        animais.append(animal) # adiciona o novo animal à lista
print(animais)  # Ajustar validação para UPPERCASE

print('')

animal = input('Digite o animal a ser deletado da lista: ')
animais.remove(animal)
print(animais)

print('')

jogadores = ['Ronaldo', 'Rivaldo', 'Ronaldo', 'Adriano']
ronaldos = jogadores.count('Ronaldo')
print(jogadores)
print('Quantidade de Ronaldos: ', ronaldos)

print('')

rivaldo = jogadores.index('Rivaldo')
print("Rivaldo está na posição ", rivaldo)

print('')

jogadores.sort()
print("jogadores em ordem alfabética: ", jogadores)

print('')

digitos = [3, 1, 4, 1, 5, 9, 2, 6, 5]
maior = max(digitos)
menor = min(digitos)
print(digitos)
print("Maior = ", maior, "e menor = ", menor)

print('')

# Tuplas

# Uma tupla é uma coleção de objetos que lembra muito as listas.

# Ao invés de colchetes, usamos parênteses para declarar as tuplas:
numeros = (1,2,3,5,7,11)

# Podemos declarar sem parênteses também:
numeros = 1,2,3,5,7,11

# Para acessar um valor, utilizamos a mesma sintaxe das listas:
print(numeros[4])
print(type(numeros))

'''
Porém, tuplas são imutáveis: não é possível adicionar ou modificar valores.
Descomentar a linha abaixo provocará erro de execução:
'''
# numeros[4] = 8

# Podemos gerar uma tupla a partir de uma lista...
lista1 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
tupla1 = tuple(lista1)
print(tupla1)

# ...ou uma lista a partir de uma tupla:
tupla2 = [1, 6, 1, 8]
lista2 = list(tupla2)
print(lista2)

# Também pode-se usar o unpacking com uma tupla:
a, b, c, d, e, f = numeros # "desempacota" a tupla numeros
print("O primeiro vale:", a, "e o ultimo vale:", f)