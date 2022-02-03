#  Nesta versão estamos importando a bibliotecas pandas, numpy e pytz. Arquivo 'alunos.csv' importado da minha base de teste

import pandas as pd

tabela = pd.read_csv('alunos.csv', sep=',')
print(tabela)

# - Nesta versão estou utilizando a biblioteca do pandas, numpy e pytz que deixa a lista mais organizada, alinhada e fácil de avaliar. No Repl it  tive que subsituir o comando display, pelo print para rodar a tabela. Ambos comando (display e print) roda, no Jupyter, display formata melhor a tabela, deixa ela mais apresentavel. - https://www.youtube.com/watch?v=AnJPtKLtc7o

tabela.to_csv('alunos_copia.csv')
nova_tabela = pd.read_csv('alunos_copia.csv')
nova_tabela.head()

#  - Ainda utilizando a biblioteca do pandas, numpy e pytz, faço a cópia da tabela para um novo arquivo CSV e apresento no console
