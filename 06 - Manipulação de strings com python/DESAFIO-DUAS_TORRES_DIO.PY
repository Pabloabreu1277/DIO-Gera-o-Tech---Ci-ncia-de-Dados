"""#desafio duas torres
entrada = input().split(" ")
distancia = int(entrada[0])
#print (distancia)
diametro1 = int(entrada[1])
#print(diametro1)
diametro2 = int(entrada[2])
#print(diametro2)
ICM = distancia/(diametro1 + diametro2)

print(f"{ICM:.2f}")"""
"""
#desafio cachorro quente

valores = input().split(" ")
n_quentes = int(valores[0])
n_participantes=int(valores[1])
media = float(n_quentes/n_participantes)

print(f"{media:.2f}")"""

#desafio viagem
valores = input().split(" ")
n_tempo = int(valores[0])
n_velocidade=int(valores[1])
litros = float((n_tempo*n_velocidade)/12)
print(f"{litros:.3f}")


