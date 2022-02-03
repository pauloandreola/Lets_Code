inicial = 0
palavra = str(input('Digite uma palavra: '))
print('Apresentando uma letra desta(S) palavra(S) em cada linha')
print('')
final = len(palavra)
lista = []
lista.append(palavra)

for lista in range(inicial, final, +1):
  print('A letra número',lista+1, 'da(s) palavra(s) é: ',palavra[lista])

# - Comando len https://qastack.com.br/programming/4967580/how-to-get-the-size-of-a-string-in-python

#  - Comando range https://www.delftstack.com/pt/howto/python/python-loop-through-list/