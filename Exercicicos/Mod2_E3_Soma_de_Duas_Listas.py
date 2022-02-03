lista1 = [1, 4, 5, 7]
lista2 = [3, 5, 6]
for soma1, soma2 in zip(lista1, lista2):
  print(soma1+soma2)
print('')

#  - Outra forma - Abaixo a soma dos valores retornam em uma lista

lista3 = [1, 2, 3, 4]
lista4 = [5, 6, 7]
soma = list(map(sum, zip(lista3, lista4)))
print(soma)

# Obs. - Notar que neste caso o valor 7  e 4 da primeira lista não está sendo apresentado na lista final.

#  - Comando zip para somar as listas -  https://pt.stackoverflow.com/questions/309189/soma-de-cada-elemento-de-duas-listas