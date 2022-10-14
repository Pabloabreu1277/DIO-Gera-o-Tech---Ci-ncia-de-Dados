#exemplo 1

frutas = ["laranja", "maca", "uva"]
frutas = []
letras = list("python")
numeros = list(range(10))
carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

#exemplo 2
frutas = ["maçã", "laranja", "uva", "pera"]
print(frutas[0])
print(frutas[2])

#listas alinhadas
matriz = [[1, "a", 2],
        ["b", 3, 4],
        [6, 5, "c"]]

print(matriz[0])  
print(matriz[0][0]) 
print(matriz[1][0])  
print(matriz[-1][-1])


#exemplo de fatiamento
lista=["p", "y", "t", "h", "o", "n"]
print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])

#Exemplo com for
carros = ["gol", "celta", "palio"]
for carro in carros:
    print(carro)

#Unumereite
carros = ["gol", "celta", "palio"]
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

#Filtros usando logicas
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

#Filtro usando versao python
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

#Modificando os valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []
for numero in numeros:
    quadrado.append(numero ** 2)
    print(quadrado)

#Modificando os valores vs2
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)