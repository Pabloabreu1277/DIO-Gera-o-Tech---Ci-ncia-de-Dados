#append
lista = []
lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])
print(lista)
print("%"*30)

#clear
lista = [1, "Python", [40, 30, 20]]
print(lista)  # [1, "Python", [40, 30, 20]
lista.clear()
print(lista)  
print("%"*30)

#copy
lista = [1, "Python", [40, 30, 20]]
l2=lista.copy()
print(lista)
print(l2) 
print("%"*30) 

#count
cores = ["vermelho", "azul", "verde", "azul"]
print(cores.count("vermelho"))  # 1
print(cores.count("azul"))  # 2
print(cores.count("verde")) 
print("%"*30)

#Extend
linguagens = ["python", "js", "c"]
print(linguagens)  # ["python", "js", "c"]
linguagens.extend(["java", "csharp"])
print(linguagens)  
print("%"*30)

#index
linguagens = ["python", "js", "c", "java", "csharp"]
print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  
print("%"*30)

#pop
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.pop()  # csharp
linguagens.pop()  # java
linguagens.pop()  # c
linguagens.pop(0) 
print(linguagens)
print("%"*30)

#remove
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.remove("c")
print(linguagens)  
print("%"*30)

#reverse
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.reverse()
print(linguagens) 
print("%"*30)

#sort
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)
print("%"*30)

#Len
linguagens = ["python", "js", "c", "java", "csharp"]
print(len(linguagens))  
print("%"*30)

#Sorted
linguagens = ["python", "js", "c", "java", "csharp"]
sorted(linguagens, key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
sorted(linguagens, key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)
print("%"*30)

