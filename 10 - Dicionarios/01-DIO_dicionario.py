#metodos para manipular dicionarios
pessoa = {"nome": "Guilherme", "idade": 28}
pessoa = dict(nome="Guilherme", idade=28)
pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(pessoa)
print("\/" * 30)

#outro exemplo
dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
dados["nome"]  # "Guilherme"
dados["idade"]  # 28
dados["telefone"]  # "3333-1234"
dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"
print(dados)
print("\/" * 30)


#mais um exemplo
pessoa = {"nome": "Guilherme", "idade": 28}
pessoa = dict(nome="Guilherme", idade=28)
pessoa["telefone"] = "3333-1234"  
print(pessoa)
print("\/" * 30)

#Acesso aos dados
dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
dados["nome"]  # "Guilherme"
dados["idade"]  # 28
dados["telefone"]  # "3333-1234"
dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"
print(dados)
print("\/" * 30)

#Dicionários aninhados
contatos = {
       "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
       "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
       "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
       "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
       }
print(contatos["giovanna@gmail.com"]["telefone"])  
print("\/" * 30)

#Iterar dicionários
for chave in contatos:
        print(chave, contatos[chave])
        for chave, valor in contatos.items():
            print(chave, valor)
print("\/" * 30)
