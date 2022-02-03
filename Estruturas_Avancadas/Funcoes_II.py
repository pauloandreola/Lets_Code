# Abaixo estou utilziando uma anotação especial, o asterisco. É obrigatório, a variável pode ser outra normalmente usam args

def calcula_media01(*argumento):
  print(argumento, type(argumento))

calcula_media01(4, 5, 6)

def calcula_media(*argumento, desvio):
  soma = sum(argumento)
  media = soma / len(argumento)
  return media + desvio

print(calcula_media(4, 5, 6, desvio=0.3))

print('')

# Estou utiliziando um asteríscos pois não sei quantos argumentos serão passados dentro da função. Neste caso vou receber uma TUPLA de argumentos.


def calcula_media01(*args, margem):
  soma = sum(args)
  media = soma / len(args)
  return media + margem

print(calcula_media01(8, 10, 9, margem=.5))

print('')
print('')

# Estou utiliziando dois asteríscos pois não sei quantos argumentos serão passados dentro da função. Neste caso vou receber um DICIONÁRIO de argumentos.

def print_info(**kwargs):
  print(kwargs, type(kwargs))

print_info(nome='Paulo', sobrenome='Andreola')

print('')

def impressao_informacao(**argumentos):
  print(argumentos, type(argumentos))

impressao_informacao(nome='Maria', sobrenome='Andreola') 

print('')
print('')
print('')

# Abaixo resolução do site da Let's Code  https://selecao.letscode.com.br/curso-digital/e44a37c9-4389-46c4-9763-a64adc6d01bf/modulo/a1fac656-3d35-474b-81b7-a74d78d5fa2b/topico/d509a836-0396-4776-afec-6862010c3855?uuid=70b0a661-d543-439f-8b41-c19c06893c36

def piscina(*infos):
    vol = infos[0]*infos[1]*infos[2]
    return vol

volume = piscina(5, 4, 5)

print('O volume 01 é: ', volume)

print('')

def piscina(prof, largura, comprimento):
    vol = prof*largura*comprimento
    return vol

lista = [5, 4, 5]

volume = piscina(*lista)

print('O volume 02 é: ', volume)

print('')

def piscina(prof, **infos):
    vol = prof*infos['largura']*infos['comprimento']
    return vol

volume = piscina(5, largura=4, comprimento=5)

print('O volume 03 é: ', volume)

print('')

def piscina(prof, **infos):
    vol = prof*infos['largura']*infos['comprimento']
    return vol

volume = piscina(5, largura=4, comprimento=5)

print('O volume 04 é: ', volume)

print('')

def piscina(prof, largura=4, comprimento=5):
    vol = prof*largura*comprimento
    return vol

infos = {'largura': 10, 'comprimento': 20}

volume = piscina(5, **infos)

print('O volume é: ', volume)

