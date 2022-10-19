#parametros especiais
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0",combustivel="Gasolina") # válido
#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat",motor="1.0", combustivel="Gasolina")
print("\/"*30)


#Keyword only
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat",motor="1.0", combustivel="Gasolina") # válido
#criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0",combustivel="Gasolina") # inválido
print("\/"*30)

#Keyword and positional only
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0",
combustivel="Gasolina") # válido
#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat",
#motor="1.0", combustivel="Gasolina") # inválido
print("\/"*30)

#Objetos de primeira classe
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {resultado}")

exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtrair) # O resultado da operação 10 + 10 = 20
print("\/"*30)

#Escopo local e escopo 
salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

novo=salario_bonus(500)
print(novo)
print("\/"*30)