#criando tuplas
frutas = ("laranja", "pera", "uva",)
letras = tuple("python")
numeros = tuple([1, 2, 3, 4])
pais = ("Brasil",)
print(frutas)
print(letras)
print(numeros)
print(pais)
print("="*30)

#acesso direto
frutas = ("maçã", "laranja", "uva", "pera",)
print(frutas[0])  # maçã
print(frutas[2])  
print("="*30)

#acesso indice negativo
frutas = ("maçã", "laranja", "uva", "pera",)
print(frutas[-1])  # pera
print(frutas[-3]) 
print("="*30) 

#tuplas alinhadas
matriz=((1, "a", 2),
	    ("b", 3, 4),
	    (6, 5, "c"),)
print(matriz[0])  # (1, "a", 2)
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])
print("="*30) 

carros = ("gol", "celta", "palio",)
for carro in carros:
    print(carro)
print("="*30) 
  
carros = ("gol", "celta", "palio",)
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
print("="*30) 

cores = ("vermelho", "azul", "verde", "azul",)
cores.count("vermelho")  # 1
cores.count("azul")  # 2
cores.count("verde") 
print("="*30) 

linguagens = ("python", "js", "c", "java", "csharp",)
linguagens.index("java")  # 3
linguagens.index("python")
print("="*30) 

linguagens = ("python", "js", "c", "java", "csharp",)
len(linguagens)
print("="*30) 

carros = ("gol")
print(isinstance(carros, tuple))



