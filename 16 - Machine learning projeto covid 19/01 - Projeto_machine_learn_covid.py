# projeto covid 19
## Digital innovation
#Python 3.8 somente roda nessa versão
# importando as bibliotecas
# import pmdarima as pm
# import warnings 
# warnings.filterwarnings('ignore')
from pmdarima.arima import auto_arima
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px 
import plotly.graph_objects as Go
import re
#pip install statsmodels
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

# vamos importar os dados para o projeto

url = 'https://github.com/neylsoncrepalde/projeto_eda_covid/blob/master/covid_19_data.csv?raw=true'
df = pd.read_csv(url,parse_dates=['ObservationDate', 'Last Update'])
print(df)
print("\/"*30)

#confirir os tipos de cada coluna
print(df.dtypes)
print("\/"*30)

def corrige_colunas(col_name):
    return re.sub(r"[/| ]", "",col_name).lower()
print(corrige_colunas("AdGe/ P ou"))
print("\/"*30)

#corrigindo as colunas do dataframe
df.columns = [corrige_colunas(col) for col in df.columns]
print(df)
print("\/"*30)

#Dados do Brasil
#print(df.loc[df.countryregion.unique()])
print(df.loc[df.countryregion == 'Brazil'])
print("\/"*30)
brasil = df.loc[(df.countryregion == 'Brazil') & (df.confirmed>0)]
print(brasil)
print("\/"*30)

#Casos confirmados
#Grafico da evolução de casos confirmados
fig1=px.line(brasil,'observationdate','confirmed',title='Casos confirmados no Brasil')
fig1.show()

#novos casos por dia
print(brasil.shape[0])
#tecnica de programação funcional
brasil['novoscasos'] = list(map(
    lambda x: 0 if (x==0) else brasil['confirmed'].iloc[x] - brasil['confirmed'].iloc[x-1],
    np.arange(brasil.shape[0])
))
print(brasil)
print("\/"*30)

#visu de novos casos por dia
fig2=px.line(brasil,x='observationdate',y='novoscasos',title='Novos casos por dia no Brasil')
fig2.show()

#Casos com mortes

fig3 = Go.Figure()
fig3.add_trace(
    Go.Scatter(x=brasil.observationdate, y=brasil.deaths, name='Mortes',
            mode='lines+markers',line={'color':'red'})
)
#layout
fig3.update_layout(title='Mortes por COVID-19 no Brasil')
fig3.show()

#taxa de crescimento da doença
#taxa_crescimento = (presente/passado)**(1/n)-1
def taxa_crescimento(data,variable, data_inicio=None, data_fim=None):
    if data_inicio == None:
        data_inicio = data.observationdate.loc[data[variable] > 0].min()
    else: 
        data_inicio = pd.to_datetime(data_inicio)
    if data_fim == None :
        data_fim = data.observationdate.iloc[-1]
    else:
        data_fim = pd.to_datetime(data_fim)
    #valores presentes do passado
    passado = data.loc[data.observationdate == data_inicio,variable].values[0]
    presente = data.loc[data.observationdate == data_fim, variable].values[0]
    #define o numero de pontos no tempo que vamos avaliar
    n = (data_fim-data_inicio).days
    #calculo da taxa
    taxa = (presente/passado)**(1/n) - 1
    return taxa*100

#taxa de crescimento médio do covide no brasil em todo o periodo
print(taxa_crescimento(brasil,'confirmed'))
print("\/"*30)

#taxa de crescimento diario
def taxa_crescimento_diario(data, variable, data_inicio=None):
    if data_inicio == None:
        data_inicio = data.observationdate.loc[data[variable] > 0].min()
    else: 
        data_inicio = pd.to_datetime(data_inicio)
    data_fim = data.observationdate.max()
    #definimos o numero de pontos no tempo que vamos avaliar
    n = (data_fim - data_inicio).days
    #taxa calculado de um dia para o outro
    taxas = list(map(
        lambda x: (data[variable].iloc[x] - data[variable].iloc[x-1]) / data[variable].iloc[x-1],
        range(1, n+1)
    
    ))
    return np.array(taxas) * 100

tx_dia = taxa_crescimento_diario(brasil,'confirmed')
print(tx_dia)

primeiro_dia = brasil.observationdate.loc[brasil.confirmed > 0].min()
fig4 = px.line(x=pd.date_range(primeiro_dia, brasil.observationdate.max())[1:],
            y=tx_dia, title='Taxa de crescimento de casos confirmados no Brasil')

fig4.show()

#predições
confirmados = brasil.confirmed
confirmados.index = brasil.observationdate
print(confirmados)
print("\/"*30)

res = seasonal_decompose(confirmados)

fig5, (ax1,ax2,ax3,ax4) = plt.subplots(4,1,figsize=(10,8))

ax1.plot(res.observed)
ax2.plot(res.trend)
ax3.plot(res.seasonal)
ax4.plot(confirmados.index, res.resid)
ax4.axhline(0, linestyle='dashed', c='black')
plt.show()

#ARIMA
#pip install pmdarima

modelo = auto_arima(confirmados)


#observado dados captados
fig = Go.Figure(Go.Scatter(
    x=confirmados.index, y=confirmados, name='Observados'
))
#aprendizado dados gerados pelo aprendicado da predição
fig.add_trace(Go.Scatter(
    x=confirmados.index, y=modelo.predict_in_sample(), name='Preditos'
))
#previsão com o modelo 31 dias
fig.add_trace(Go.Scatter(
    x=pd.date_range('2020-05-01','2020-06-01'), y=modelo.predict(31),name='Forecast'
))

fig.update_layout(title='Previsão de casos confirmados no Brasil para o futuro 30 dias 1 ano 2 anos')
fig.plt.show()

"""Acontece que o Prophet não instala em versões de Python maiores que a 3.8. Pela minha pouca experiência, sei que isso se resolve no PyCharm com o Ambiente Virtual que a própria IDE fornece, mas como sou mais acostumado ao Jupyter NB para ciência de dados, eu penei um pouquinho até encontrar a solução nesses artigos:

https://medium.com/data-folks-indonesia/installing-fbprophet-prophet-for-time-series-forecasting-in-jupyter-notebook-7de6db09f9

e

https://dev.to/gelopfalcon/python-virtual-environments-25gc.



Em resumo o que eles ensinam é basicamente criar um Ambiente Virtual no prompt do Anaconda com a versão do Python que você desejar usar e dentro dele instalar o Jupyter e as bibliotecas necessárias para rodar o pacote que precisar usar, no meu caso o fbprophet.



Segue os passos:

1 – Abrir o prompt anaconda;

2 – Criar uma Venv: conda create -n “nome da venv” python=3.8

3 – Ativar a Venv: conda activate “nome da venv”

Daqui pra baixo são as dependências que o pacote precisa:

*No caso do Prophet foi necessário instalar a instalar o compiler do C++

C++ compiler: conda install libpython m2w64-toolchain -c msys2
MatPlotLib: conda install matplotlib scipy pandas -c conda-forge
Pystan: conda install pystan -c conda-forge
Ephem: conda install -c anaconda ephem
scikit-learn: pip install -U scikit-learn
pmdarima: pip install pmdarima
e por fim o Prophet: conda install -c conda-forge prophet


Só depois desse passo a passo eu consegui concluir o projeto (mais uma vez: eu utilizo o Jupyter NB com python 3.10).

Confesso que perdi um bom tempo até chegar a essa solução, mas se você deparar com o mesmo problema aí está a resposta.

O lado bom em tudo isso foi que aprendi a utilizar a venv no jupyter e agora tenho duas versões do python nele e, se necessário, já sei como resolver problemas futuros de compatibilidade.



Bom, espero que para quem enfrentar o mesmo problema essa solução seja de grande ajuda.



Ótimo estudos e boa sorte a todos!!!"""

