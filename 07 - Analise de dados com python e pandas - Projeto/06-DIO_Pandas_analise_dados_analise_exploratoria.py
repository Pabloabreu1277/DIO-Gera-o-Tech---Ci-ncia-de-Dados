#importando as bibliotecas
from turtle import title
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("dark_background")

#criando data frame
df = pd.read_excel("AdventureWorks.xlsx")

#Visualizando a database
print(df.head())
print("#"*45)

#quantidade de linhas e colunas
print(df.shape)
print("#"*45)

#verificando os tipos da base
print(df.dtypes)
print("#"*45)

#Qual a receita total
print(df["Valor Venda"].sum())
print("#"*45)

#Qual o custo total por venda
df["custo"] = df["Custo Unitário"].mul(df["Quantidade"]) #criandocoluna de custo
print(df.head(5))
print("#"*45)

#Qual e o custo total
print(round(df["custo"].sum(),2))
print("#"*45)

#Agora que temos a receita e o custo total podemos achar o lucro total 
#vamos criar uma coluna de lucro que sera receita custo
df["lucro"] = df["Valor Venda"] - df["custo"]
print(df.head(1))
print("#"*45)

#Total lucro
round(df["lucro"].sum(),2)

#Criando uma coluna com o total de dias para envio do produto
df["Tempo_envio"] = df["Data Envio"] - df["Data Venda"]
print(df.head(1))

#Extraindo apenas os dias
df["Tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days
print(df.head(1))
print("#"*45)

#verificando o tipo da coluna de envio
print(df["Tempo_envio"].dtype)

#Média de tempo de envio por marca
print(df.groupby("Marca")["Tempo_envio"].mean())
print("#"*45)

#Verificando se temos dados faltantes
print(df.isnull().sum())
print("#"*45)

#Qual foi o lucro por ano e por marca
#Agrupando por ano e marca
print(df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum())
print("#"*45)
pd.options.display.float_format = '{:20,.2f}'.format

#Resetando o index
lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum().reset_index()
print(lucro_ano)
print("#"*45)

#Qual o total de produtos vendidos?
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)

#Grafico total de produtos vendidos
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=True).plot.barh(title="Total de produtos vendidos")
plt.show()

#por ano
df.groupby(df["Data Venda"].dt.year)["lucro"].sum().plot.bar(title="Lucro por ano")
plt.xlabel("Ano")
plt.ylabel("Receita")
plt.show()

df.groupby(df["Data Venda"].dt.year)["lucro"].sum()

#selecionando apenas as vendas de 2009
df_2009 = df[df["Data Venda"].dt.year == 2009]
print(df_2009.head())
print("#"*45)

df_2009.groupby(df_2009["Data Venda"].dt.month)["lucro"].sum().plot(title="Lucro x mes")
plt.xlabel("Mes")
plt.ylabel("Lucro")
plt.show()

df_2009.groupby("Marca")["lucro"].sum().plot.bar(title="lucro x marca")
plt.xlabel("Mes")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal')
plt.show()

df_2009.groupby("Classe")["lucro"].sum().plot.bar(title="lucro x classe")
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal')
plt.show()

#Estatisticas
print(df["Tempo_envio"].describe())
print("#"*45)

plt.style.use("ggplot")
#grafico de boxplot
plt.boxplot(df["Tempo_envio"])
plt.show()

#HISTOGRAMA
plt.hist(df["Tempo_envio"])
plt.show()

#Tempo minimo de envio
print(df["Tempo_envio"].min())
print("#"*45)

#Tempo max de envio
print(df["Tempo_envio"].max())
print("#"*45)

#outlier
print(df[df["Tempo_envio"]==20])
print("#"*45)
#salvando a base nova editada
df.to_csv("df_vendas_novo.csv",index=False)

