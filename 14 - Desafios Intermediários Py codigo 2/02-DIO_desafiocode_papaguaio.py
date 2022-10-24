"""
Desafio
Humberto tem um papagaio muito esperto. 
Quando está com as duas pernas no chão, 
o papagaio fala em português. Quando levanta a perna esquerda, fala em inglês. 
Por fim, quando levanta a direita fala em francês. Nico, amigo de Humberto, 
ficou fascinado com o animal. Em sua emoção perguntou: “E quando ele levanta as duas?”. 
Antes que Humberto pudesse responder, o papagaio gritou: “Aí eu caio, idiota!”.

Entrada
A entrada consiste de diversos casos de teste. 
Cada caso de teste consiste uma string informando qual a situação de levantamento de pernas do papagaio.

Saída
Para cada condição de levantamento de pernas do papagaio, imprima a linguagem que ele utilizará. 
Caso ele levante ambas as pernas, imprima “caiu”. Quebre uma linha a cada caso de teste.


"""
# dados de entradas
# esquerda, direita, nenhuma, ambas

while True: 
    try: 
        papagaio = input().upper()
        if papagaio == "ESQUERDA":
            print("ingles")
        elif papagaio == "DIREITA":
            print("frances")
        elif papagaio == "NENHUMA":
            print("portugues")
        elif papagaio == "AMBAS":
            print("caiu")

    except EOFError: 
        break