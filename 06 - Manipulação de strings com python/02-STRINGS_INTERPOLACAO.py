nome = " Pablo "
idade = 28
profissao = " Programador "
linguagem = " Python "
saldo = 47.565889851245888

dados= {"nome":"Pablo","idade":28}

print("Nome: %s idade: %d" % (nome,idade))
print("Nome:{} idade: {}".format(nome,idade))
print("Nome:{1} idade:{0}".format(idade,nome))
print("Nome:{name} idade:{age}".format(age=idade,name=nome))
print("Nome:{nome} idade:{idade}".format(**dados))
print(f"nome:{nome}  idade:{idade} saldo:{saldo:0.2f}")
print(f"nome:{nome}  idade:{idade} saldo:{saldo:1.2f}")