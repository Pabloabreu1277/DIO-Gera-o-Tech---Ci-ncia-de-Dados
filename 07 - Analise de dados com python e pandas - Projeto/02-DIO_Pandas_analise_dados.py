import pandas as pd

df = pd.read_csv("/Users/HP Workstation/Downloads/Conhecendo a sintaxe python/DIO-Geracao-Tech-Ciencia-de-Dados/07 - Analise de dados com python e pandas - Projeto/Gapminder.csv",error_bad_lines=False)
print(df.head())

print("#"*100)
df=df.rename(columns={"country":"Pais"})
print(df.head())
print("#"*100)

print(df.shape)
print(df.columns)
print(df.describe())
"""

print(df["2009"].unique())
print(df["Pais"].unique())

produção = df.loc[df["2009"] == "0"]
print(produção.head())
print(produção["2009"].unique())

print("#"*100)

print(df.groupby("2009")["Pais"].nunique())
print("#"*100)
print(df["2009"].mean())
print(df["2008"].sum())
print("#"*100)

#base de dados com um "M" apos os valores, quero extrair esse valor sem a letra m porem nao consigo calcular.
"""

