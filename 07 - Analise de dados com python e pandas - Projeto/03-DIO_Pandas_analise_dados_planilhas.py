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


