x = 5
print(x)
print(type(x))

preco = 19.99
print(preco, type(preco))

cidade = 'Porto Alegre'
print(cidade, type(cidade))

disponivel = True
print(disponivel)

disponivel = False
print(disponivel, type(disponivel))

inteiro = 10
ponto_flutuante = 9.4
complexo = 3+4j

print(inteiro, type(inteiro))

print(ponto_flutuante, type(ponto_flutuante))

print(complexo, type(complexo))

print('')
print(inteiro + complexo) # Soma entre integer e complex

print(ponto_flutuante + complexo) # Soma entre float e complex

print(complexo + complexo) # Soma entre complex

print('')
print(complex(inteiro)) # Valor integer mudando para complex