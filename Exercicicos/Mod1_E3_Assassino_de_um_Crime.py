ponto = 0
print('Para as perguntas abaixo a resposta deve ser somente sim, ou não.')
print('')
opcao = str(input('Mora perto da vítima? '))
resposta = opcao.upper().strip()
if (resposta == 'SIM'):
    ponto = ponto + 1 
    
opcao = input('Já trabalhou com a vítima? ')
resposta = opcao.upper().strip()
if (resposta == 'SIM'):
    ponto = ponto + 1
    
opcao = input('Telefonou para a vítima? ')    
resposta = opcao.upper().strip()
if (resposta == 'SIM'):    
    ponto = ponto + 1
    
opcao = input('Esteve no local do crime? ')   
resposta = opcao.upper().strip()
if (resposta == 'SIM'):
    ponto = ponto + 1
    
opcao = input('Devia para a vítima? ')
resposta = opcao.upper().strip()
if (resposta == 'SIM'):
    ponto = ponto + 1
    
if (ponto == 5):
    print('Você atingiu 5 na pontuação, portanto é o assassino, será encaminhado para a delegacia!')
elif (ponto == 4 or ponto == 3):
    print('Você atingiu 4 ou 3 na pontuação, portanto você é cumplíce, não deve sair da cidade e deve parmanecer em casa!')
elif (ponto == 2):
    print('Você é apenas suspeito, não deve sair da cidade!')
elif (ponto <= 1):
    print('Você está liberado, não arrume confusão!')