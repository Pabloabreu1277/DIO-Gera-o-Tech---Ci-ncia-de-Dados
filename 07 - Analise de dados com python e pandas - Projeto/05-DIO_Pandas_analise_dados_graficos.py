import pandas as pd
import matplotlib.pyplot as plt
import mplcyberpunk

#leitura dos arquivos

df1 = pd.read_excel("Aracaju.xlsx")
df2 = pd.read_excel("Fortaleza.xlsx")
df3 = pd.read_excel("Natal.xlsx")
df4 = pd.read_excel("Recife.xlsx")
df5 = pd.read_excel("Salvador.xlsx")

#juntando todos os arquivos
df = pd.concat([df1,df2,df3,df4,df5])

#exibindo as 5 primeiras linhas

print(df.head(5))

#exebir as 5 ultimas linhas

print(df.tail(5))

#amostra de linhas no df

print(df.sample(10))
print("--"*50)

#verificar o tipo de dado de cada coluna
print(df.dtypes)

#alterando o tipo de dado da coluna lojaID
df["LojaID"] = df["LojaID"].astype("object")
print(df.dtypes)
print("--"*50)

#dados das linhas com falores em brancos
print(df.isnull().sum())
print("--"*50)

#Substituir os valores nulos pela média
#df["Vendas"].fillna(df["Vendas"].mean(),inplace=True)
#print(df.isnull().sum())
#df["Vendas"].fillna(0, inplace=True)

#apagando as linhas com valores nulos
df.dropna(inplace=True)

print(df["Vendas"].mean())

#Removendo linhas que estejam com vallores faltantes em todas as colunas 
#df.dropna(Row="all",inplace=True)

#Criando coluna receita 
df["Receita"] = df["Vendas"].mul(df["Qtde"])

print(df.head())

print(df["Vendas"].mean())

df["Receita/Vendas"] = df["Receita"] / df["Vendas"]
print(df.head())

print("--"*50)

#Maior e menor receita

max = df["Receita"].max()
min = df["Receita"].min()

print(max)
print(min)

import pandas as pd

#leitura dos arquivos

df1 = pd.read_excel("Aracaju.xlsx")
df2 = pd.read_excel("Fortaleza.xlsx")
df3 = pd.read_excel("Natal.xlsx")
df4 = pd.read_excel("Recife.xlsx")
df5 = pd.read_excel("Salvador.xlsx")

#juntando todos os arquivos
df = pd.concat([df1,df2,df3,df4,df5])

#exibindo as 5 primeiras linhas

print(df.head(5))

#exebir as 5 ultimas linhas

print(df.tail(5))

#amostra de linhas no df

print(df.sample(10))
print("--"*50)

#verificar o tipo de dado de cada coluna
print(df.dtypes)

#alterando o tipo de dado da coluna lojaID
df["LojaID"] = df["LojaID"].astype("object")
print(df.dtypes)
print("--"*50)

#dados das linhas com falores em brancos
print(df.isnull().sum())
print("--"*50)

#Substituir os valores nulos pela média
#df["Vendas"].fillna(df["Vendas"].mean(),inplace=True)
#print(df.isnull().sum())
#df["Vendas"].fillna(0, inplace=True)

#apagando as linhas com valores nulos
df.dropna(inplace=True)

print(df["Vendas"].mean())

#Removendo linhas que estejam com vallores faltantes em todas as colunas 
#df.dropna(Row="all",inplace=True)

#Criando coluna receita 
df["Receita"] = df["Vendas"].mul(df["Qtde"])

print(df.head())

print(df["Vendas"].mean())

df["Receita/Vendas"] = df["Receita"] / df["Vendas"]
print(df.head())

print("--"*50)

#Maior e menor receita

max = df["Receita"].max()
min = df["Receita"].min()

print(max)
print(min)

print("--"*50)

#nlargest
print(df.nsmallest(3,"Receita"))

#agrupamento por cidade
print(df.groupby("Cidade")["Receita"].sum())

#ordenando conjuntos de dados
print(df.sort_values("Receita", ascending=False).head(10))


import pandas as pd

#leitura dos arquivos

df1 = pd.read_excel("Aracaju.xlsx")
df2 = pd.read_excel("Fortaleza.xlsx")
df3 = pd.read_excel("Natal.xlsx")
df4 = pd.read_excel("Recife.xlsx")
df5 = pd.read_excel("Salvador.xlsx")

#juntando todos os arquivos
df = pd.concat([df1,df2,df3,df4,df5])

#exibindo as 5 primeiras linhas

print(df.head(5))

#exebir as 5 ultimas linhas

print(df.tail(5))

#amostra de linhas no df

print(df.sample(10))
print("--"*50)

#verificar o tipo de dado de cada coluna
print(df.dtypes)

#alterando o tipo de dado da coluna lojaID
df["LojaID"] = df["LojaID"].astype("object")
print(df.dtypes)
print("--"*50)

#dados das linhas com falores em brancos
print(df.isnull().sum())
print("--"*50)

#Substituir os valores nulos pela média
#df["Vendas"].fillna(df["Vendas"].mean(),inplace=True)
#print(df.isnull().sum())
#df["Vendas"].fillna(0, inplace=True)

#apagando as linhas com valores nulos
df.dropna(inplace=True)

print(df["Vendas"].mean())

#Removendo linhas que estejam com vallores faltantes em todas as colunas 
#df.dropna(Row="all",inplace=True)

#Criando coluna receita 
df["Receita"] = df["Vendas"].mul(df["Qtde"])

print(df.head())

print(df["Vendas"].mean())

df["Receita/Vendas"] = df["Receita"] / df["Vendas"]
print(df.head())

print("--"*50)

#Maior e menor receita

max = df["Receita"].max()
min = df["Receita"].min()

print(max)
print(min)

print("--"*50)

#nlargest
print(df.nsmallest(3,"Receita"))

#agrupamento por cidade
print(df.groupby("Cidade")["Receita"].sum())

#ordenando conjuntos de dados
print(df.sort_values("Receita", ascending=False).head(10))

#nlargest
print(df.nsmallest(3,"Receita"))

#agrupamento por cidade
print(df.groupby("Cidade")["Receita"].sum())

#ordenando conjuntos de dados
print(df.sort_values("Receita", ascending=False).head(10))

#Aula 4 Trabalhando com datas
#Trocando o tipo de variavel das datas pois na maioria dos casos vamos encontrar datas com esse tipo de variaveis
df["Data"] = df["Data"].astype("int64")

print(df.dtypes)

print("--"*50)

df["Data"] = pd.to_datetime(df["Data"])

print(df.dtypes)

print("--"*50)

#receita por ano
print(df.groupby(df["Data"].dt.year)["Receita"].sum())
print("--"*50)

#Criando uma nova coluna com o ano
df["Ano_Venda"] = df["Data"].dt.year
print(df.sample(5))
print("--"*50)

#Extraindo o mes e o dia
df["mes_venda"], df["dia_venda"] = (df["Data"].dt.month, df["Data"].dt.day)
print(df.sample(5))
print("--"*50)

#Retornar a data mais antiga
print(df["Data"].min())
print("--"*50)

#calculando a diferença de dias
df["diferenca_dias"] = df["Data"] - df["Data"].min()
print(df.sample(5))
print("--"*50)

#criando a coluna de trimestre

df["Trimestre_vendas"] = df["Data"].dt.quarter
print(df.sample(10))
print("--"*50)

#filtrando as vendas de 2019 do mes de março
vendas_marco_19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]
print(vendas_marco_19.sample(20))
print("--"*50)

#Aula 5 visualização de dados graficos

print(df["LojaID"].value_counts(ascending=False))
print("--"*50)

#Grafico de barras
#maior quantidade de vendas registrada foi na loja 1036 = 117
plt.style.use('dark_background')
df["LojaID"].value_counts(ascending=False).plot.bar()
plt.title("Contagem de vendas X Loja")

plt.show()

# grafico de barras horizontais
df["LojaID"].value_counts(ascending=True).plot.barh()
plt.title("Ranking de vendas")
plt.show()

#grafico de pizza
df.groupby(df["Data"].dt.year)["Receita"].sum().plot.pie()
plt.title("Receita X ano")
plt.show()

# total de vendas por cidade
print(df["Cidade"].value_counts())

# add titulos e alterar eixos
df["Cidade"].value_counts().plot.bar(title = "Total de vendas por cidade",color="green");
plt.xlabel("Cidade")
plt.ylabel("Total de Vendas")
#mudando o estilo de cores do grafico
plt.style.use('dark_background')
plt.show()

#agrupamento do mes de vendas
df.groupby(df["mes_venda"])["Qtde"].sum().plot()
plt.xlabel("Mes")
plt.ylabel("Total de Produtos vendidos")
plt.legend()
plt.show()

print(df.groupby(df["mes_venda"])["Qtde"].sum())

#selecionar apenas 2019
df_2019 = df[df["Ano_Venda"]==2019]

#totsl de pçrodutos vendidos no mes
df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker = "v")
plt.xlabel("Mes")
plt.ylabel("Total de Produtos vendidos")
plt.legend()
plt.show()

#Histograma
plt.hist(df["Qtde"],color="cyan");
plt.title("Histograma quantidade de vendas")
plt.show()

#dispersão
plt.scatter(x=df_2019["dia_venda"], y= df_2019["Receita"],color="r");
plt.title("Receita")
plt.show()

#para salvar altomatico esse grafico usamos o comando:
# plt.savefig("nome do grafico")