#       Passo 1: Importar a base de Dados
#       Passo 2: Visualizar a base de Dados

import pandas
import plotly.express as px

tabela = pandas.read_csv("clientes.csv", encoding="latin", sep=";")

# deletar a coluna inútil --> axis = 0 - se for linha; axis = 1 = se for coluna
tabela = tabela.drop("Unnamed: 8", axis=1)

#       Passo 3: Tratamento de Dados
# Acertar informações que estão sendo reconhedidas de forma errada ==> coluna salario e transf em numerica / coerce em numero vazio
tabela["Salário Anual (R$)"] = pandas.to_numeric(tabela["Salário Anual (R$)"], errors="coerce")

# Corrigir as informaçãoes vazias (dropna deletar linhas vazias)
tabela = tabela.dropna()

#print(tabela.info())
#print(tabela.describe())

#       Passo 4: Analise inicial -> Entender as notas dos clientes ==> # cria o grafico depois exibe
#       Passo 5: Analise completa - > Entender como cada caracteristica do cliente impacta na nota
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, y="Nota (1-100)", histfunc="avg", text_auto="True")
    grafico.show()







