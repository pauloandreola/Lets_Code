#  Nesta versão estamos importando a bibliotecas pandas, numpy pytz. Arquivo 'alunos.csv' importado da minha base de teste

import pandas as pd

tabela = pd.read_csv('alunos.csv', sep=',')
print(tabela)

# - Nesta versão estou utilizando a biblioteca do pandas que deixa a lista mais organizada, alinhada e fácil de avaliar. No Repl it  tive que subsituir o comando display, pelo print para rodar a tabela. Ambos comando (display e print) roda, no Jupyter, display formata melhor a tabela, deixa ela mais apresentavel. - https://www.youtube.com/watch?v=AnJPtKLtc7o