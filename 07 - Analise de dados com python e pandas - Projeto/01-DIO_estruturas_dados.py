animais = ['cachorro','gato','papaguaio',12345,6.5]
print(animais)
print(animais[1])

#remover
animais.remove('cachorro')
print(animais)

#subistituir
animais[0]='avestrus'
print(animais)

#tamanho da lista
tamanho = len(animais)
print(tamanho)

quest ='gato' in animais
print(quest)

animais.extend(['cobra',66])
print(animais)

print(animais.count(66))
lista = [1,2,3,8,5,6,9,8,5,5,4,8,5,9,8,5,7,999,88,8,8,]
lista.sort()
print(lista)

#tuplas
tp = ('banana','maça', 10,50 )
print(tp[0])
#tuplas nao permitem alterações

print(tp[0:2])

#dicionarios

dc = {"maça":20,"bacana":10,"laranja":15,"uva":5}
print(dc)
print(dc["maça"])

dc["maça"]=99
print(dc)

print(dc.keys())
print(dc.values())
print(dc.setdefault("limão",22))
print(dc)






