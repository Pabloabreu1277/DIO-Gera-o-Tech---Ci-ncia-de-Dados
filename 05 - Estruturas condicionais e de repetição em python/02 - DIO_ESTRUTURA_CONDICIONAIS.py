#1)exemplo
MAIOR_IDADE = 18
IDADE_ESPECIAL = 12


idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

if idade < MAIOR_IDADE:
    print("ainda não pode tirar a CNH.")

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("ainda não pode tirar a CNH.")

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teoricas, mas não pode fazer aulas praticas")
else:
    print("ainda não pode tirar a CNH.")

print('#'*100)

#2)exemplo

conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com o cheque especial!")
        
    else:
        print("Não foi possivel realizar o saque saldo insuficiente!")
elif conta_universitaria:
    if saldo >= saque:
        print("saque realizado com sucesso!")
    else:
        print("Não foi possivel realizar o saque saldo insuficiente!")

print('#'*100)

#3) exemplo ternaria

saldo = 2000
saque = 500

status = "sucesso" if saldo >= saque else "falha"

print(f"{status} ao realizar o saque !")


