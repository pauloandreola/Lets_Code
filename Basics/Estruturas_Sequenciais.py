idade = input("Favor informar a sua idade: ")
print(idade, type(idade))  # Se não declar o tipo de variável ela vai retornar no tipo string, mesmo sendo número

print('')
idade = int(idade)  # Para isso faço um casting para transformar en inteiro, transformar string em integer
print(idade, type(idade))

# int('123abc') Vai dar erro pois neste caso "abc" não são passível de conversão, ou seja não é possível transformar as letras em inteiro

print('')
print(float('123.25')) #Transformando a string em valor do tipo float
print(str(123.35)) #Transforma o inteiro (integer) em palavra(string)
print(bool('')) # Booleano vazio é falso
print(bool('abc')) # Booleano com palavra (string) é verdadeiro
print(bool(0)) # Booleano com inteiro (integer) ZERO é falso
print(bool(-2)) #Booleano com inteiro diferente de ZERO é verdadeiro
print('')
salario_mensal = input("Digite o valor do seu salário mensal: ")
salario_mensal = float(salario_mensal)
gasto_mensal = float(input("Digite o valor do seu gasto mensal em média: "))

salario_total = salario_mensal * 12
gasto_total = gasto_mensal * 12

economizado = salario_total - gasto_total
print('O montante que você pode economizar ao final de 12 meses é de: ', economizado)

print('')
y = 3.14 # uma variável do tipo real (float)
escola = "Let's Code" # uma variável literal (string)

# Podemos exibir textos na tela e/ou valores de variáveis com a função print().

print('eu estudo na ', escola)
print('pi vale', y)

# Podemos fazer operações dentro do print:

print(y+1, y**2)

# Para arrendondar os valores podemos utilzair os seguintes comandos

print('Três casas de resolução', format(y+1,'.3f'))
print('Duas casas de resolução', + round(y+1,2))
print('Três casas de resolução', format(y**2,'.3f'))
print('Duas casas de resolução ', + round(y**2,2))
print('Três casas de resolução (Verificar este resultado) -> ', + round(y**2,3))
print('Quatro casas de resolução ', + round(y**2,4))

print("Três casas de resolução, com método diferente", '%.3f' %(y+1))