# Link para estudo de do comando .fomart    https://pyformat.info/
 
cumprimento = 'Olá, '
nome = 'Paulo'
print(cumprimento + nome)
print('')
print(nome * 5)
print('')
nome = 'Felipe'
idade = 35
nr_filhos = 2
print(nome + ' tem ' + str(idade) + ' anos e ' + str(nr_filhos) + ' filhos.')
print('')
print('{} tem {} anos e {} filhos.'.format(nome, idade, nr_filhos))
print('')
valor_gasolina = 4.556
print('O preço da gasolina hoje está em R$ {:.2f}.'.format(valor_gasolina))
print('')
print(f'{nome} tem {idade} anos e {nr_filhos} filhos.')

# Abaixo material do site: https://selecao.letscode.com.br/curso-digital/e44a37c9-4389-46c4-9763-a64adc6d01bf/modulo/a1fac656-3d35-474b-81b7-a74d78d5fa2b/topico/e61bbad7-b639-4297-87c2-7bcd5c69a312?uuid=70b0a661-d543-439f-8b41-c19c06893c36

# Dois operadores aritméticos possuem um comportamento especial em strings:
# Operador de soma (+): concatena (une) 2 strings.

palavra1 = "Let's"
palavra2 = "Code"
palavra3 = palavra1 + palavra2
print(palavra3)

# Operador de multiplicação (*): copia uma string 'n' vezes:

palavra = 'uma'
trespalavras = 3*palavra
print(trespalavras)

prod = 'chocolate'
preco = 3.14
print('O produto {} custa {}.'.format(prod, preco))

# Na linha acima, prod substituirá o primeiro {}, e preco o segundo {}.
# Saída: O produto chocolate custa 3.14.

# É possível colocar algumas opções especiais de formatação. Por exemplo:

stringoriginal = 'O litro da gasolina custa {:.2f}.'
'''
: indica que passaremos opções
.2 indica apenas 2 casas após o ponto decimal
f indica que é um float
'''
preco = 3.14159265
stringcompleta = stringoriginal.format(preco)
print(stringcompleta)

# Saída: O litro da gasolina custa 3.14
# O preço sai com apenas 2 casas após a vírgula!

# Pode-se chamar as variávies em diferentes ordens:

print('{2}, {1} and {0}'.format('a', 'b', 'c'))

# Saída: c, b and a

print('{0}{1}{0}'.format('abra', 'cad'))

# Saída: abracadabra


# Podemos especificar um número de dígitos obrigatório por campo.
# Vejamos o exemplo:

dia = 1
mes = 8
ano = 2019
data1 = '{}/{}/{}'.format(dia, mes, ano)
print(data1)

# Saída: 1/8/2019
# O dia e o mês ocupam apenas 1 espaço


data2 = '{:2d}/{:2d}/{:4d}'.format(dia, mes, ano)

# A opção 'd' significa que o parâmetro é um número inteiro.

print(data2)

# Saída:  1/ 8/2019
# Agora, dia e mês ocupam obrigatoriamente 2 espaços:  1/ 8/2019

# Podemos forçar que os espaços em branco sejam preenchidos com o número 0:

data3 = '{:02d}/{:02d}/{:04d}'.format(dia, mes, ano)
print(data3)

# Saída: 01/08/2019
# Agora sim a data está no formato usual, dd/mm/aaaa: 01/08/2019

# Um modo mais simples de utilizar o format

nome = "Pietro"
profissao = "professor"
escola = "Let's Code"

print(f'{nome} é {profissao} da {escola}.')

# Saída: Pietro é professor da Let's Code.

print('')
print('')
print('')

class Planta(object):
    classe = 'Árvore'
    tipos = [{'nome': 'Pau Brasil'}, {'nome': 'Eucalipto'}]
print('{p.classe}: {p.tipos[0][nome]}'.format(p=Planta()))

print('')

class Plant(object):
    classe = 'Árvore'
    tipos = [{'nome': 'Pau Brasil'}, {'nome': 'Eucalipto'}]
print('{p.classe}= {p.tipos[1][nome]}'.format(p=Planta()))

print('')

pessoa = {'primeiro': 'Paulo', 'ultimo': 'Andreola'}
print('{p[primeiro]} {p[ultimo]}'.format(p=pessoa))