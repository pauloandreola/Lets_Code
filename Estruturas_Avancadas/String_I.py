empresa = 'Google'
print(empresa)
print('')
empresa = "Google"
print(empresa)
print('')

# empresa02 = 'Let's Code'

empresa = "Let's Code"
print(empresa)
print('')
frase = "O professor Pietro da Let's Code dise: \"Hoje a pizza é por minha conta\""
print(frase)
print('')
empresa = 'Google'
print(empresa[0])
print('')    
empresa = 'Google'
print(empresa[:3])
print('') 
nomes_cidades = "São Paulo, Belo Horizonte, Rio De Janeiro, Brasilia"
nomes_cidades = nomes_cidades.split(', ')
print(nomes_cidades)
print('') 
nomes_cidades = "São Paulo, Belo Horizonte, Rio De Janeiro, Brasilia"
nomes_cidades = nomes_cidades.split()
print(nomes_cidades)
print('')
cabecalho = "             MENU PRINCIPAL              "
print(cabecalho.strip())
print('')
nome_cidade = 'rio DE janeirO'
print(nome_cidade.title())
print(nome_cidade.capitalize())
print(nome_cidade.lower())
print(nome_cidade.upper())
print('')
nome_cidade = input('Que cidade/capital do Brasil é conhecida como cidade do chimarrão? ')
nome_cidade = nome_cidade.strip().upper()
while nome_cidade != 'PORTO ALEGRE':
    print('Não acertou, tente novamente')
    nome_cidade = input('Que cidade/capital do Brasil é conhecida como a cidade do chimarrão? ')
print('Booooa, acertou!!!')
print('')

# Abaixo o material disposto no link abaixo: https://selecao.letscode.com.br/curso-digital/e44a37c9-4389-46c4-9763-a64adc6d01bf/modulo/a1fac656-3d35-474b-81b7-a74d78d5fa2b/topico/3f390ec5-7ef5-4332-9c0d-fe3c213bbcb5?uuid=70b0a661-d543-439f-8b41-c19c06893c36

# Suponhamos que temos a seguinte string:

frase = 'uma FRASE'

# Podemos acessar individualmente cada caractere em uma frase.
# A ideia é a mesma de acessar uma lista:
print(frase[0])
print(frase[1])
print(frase[2])
print(frase[3])
print(frase[4])
print('')

tamanho = len(frase)
print("A frase possui", tamanho, "caracteres, contando com o espaço entre as palavras")

# Porém, strings são imutáveis: não podemos alterar caracteres individuais
# A linha abaixo, se for descomentada, dará erro no programa:
# frase[4] = 'C'

# Podemos converter strings para listas:
listafrase = list(frase)
print(listafrase)

# A função join() intercala cada elemento de uma lista com uma string.
stringfinal = '-py'.join(listafrase)
print(stringfinal)

# Usar um join() com uma string vazia é útil para transformar a lista de volta
# em string:
stringfinal = ''.join(listafrase)
print(stringfinal)

# Existem algumas funções interessantes que retornam a string "tratada":
s1 = frase.capitalize() # 1a letra maiúscula, restante minúscula
s2 = frase.title() # todo início de palavra em maiúscula, resto minúscula
s3 = frase.upper() # string inteira em maiúscula
s4 = frase.lower() # string inteira em minúscula
s5 = frase.replace('F', 'C') # substitui a primeira substring pela segunda

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
# Note que NENHUMA delas ALTERA a string original, elas sempre retornam
# a string nova.
print('String original:', frase)

# Outra possibilidade com strings é quebrar a string em uma lista de substrings
# Sempre que o caractere especificado é encontrado, a string é quebrada
quebra1 = frase.split(' ') # quebra a frase no caractere espaço em branco
quebra2 = s3.split('A') # quebra a frase em maiúsculas no caractere 'A'

print(quebra1)
print(quebra2)

# Podemos inserir quebras de linha com '\n'
frase = 'uma\nFRASE'
print(frase)
# Podemos inserir tabulação com '\t'
frase = 'uma\n\tFRASE'
print(frase)
# Para conseguir representar a barra '\', precisamos de 2 barras:
frase = 'uma\\FRASE'