from __future__ import annotations
from distutils import core
from importlib.util import module_for_loader


class Bicicleta:
    def __init__(self,cor,modelo,ano,valor,aro=18):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano 
        self.valor = valor 
        self.aro = aro

    def buzinar(self):
        print("Prim Prim...")
    
    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")
    
    def correr(self):
        print("Lets go vrummm...")
    
    def __str__(self):
        return f"Bicicleta: {self.cor},{self.modelo},{self.ano},{self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}:{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    

b1 = Bicicleta("vermelha","caloi",2022,650)
b1.correr()
b1.buzinar()
b1.parar()
print(b1.cor,b1.modelo,b1.ano,b1.valor)
print(b1)
print("\/"*30)

b2 = Bicicleta("Verde","Monark",2021,1000)
b2.correr()
b2.buzinar()
b2.parar()
print(b2.cor,b2.modelo,b2.ano,b2.valor)
print(b2)
print("\/"*30)