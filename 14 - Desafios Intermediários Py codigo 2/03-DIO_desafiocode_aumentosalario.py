salario = float(input())

if salario >= 0 and salario <= 600:
    percentual = 17
    novo_salario = float(salario * (1 + (percentual / 100)))
    ganho = float( novo_salario - salario)
    print(f'Novo salario: {"{:.2f}".format(novo_salario)}\nReajuste ganho: {"{:.2f}".format(ganho)}\nEm percentual: {percentual} %')

elif salario >= 601  and salario <= 900:
    percentual = 13
    novo_salario = float(salario * (1 + (percentual / 100)))
    ganho = float( novo_salario - salario)
    print(f'Novo salario: {"{:.2f}".format(novo_salario)}\nReajuste ganho: {"{:.2f}".format(ganho)}\nEm percentual: {percentual} %')

   
elif salario >= 901  and salario <= 1500:
    percentual = 12
    novo_salario = float(salario * (1 + (percentual / 100)))
    ganho = float( novo_salario - salario)
    print(f'Novo salario: {"{:.2f}".format(novo_salario)}\nReajuste ganho: {"{:.2f}".format(ganho)}\nEm percentual: {percentual} %')

  
elif salario >= 1501  and salario <= 2000:
    percentual = 10
    novo_salario = float(salario * (1 + (percentual / 100)))
    ganho = float( novo_salario - salario)
    print(f'Novo salario: {"{:.2f}".format(novo_salario)}\nReajuste ganho: {"{:.2f}".format(ganho)}\nEm percentual: {percentual} %')


    
elif salario >= 2001 :
    percentual = 5
    novo_salario = float(salario * (1 + (percentual / 100)))
    ganho = float( novo_salario - salario)
    print(f'Novo salario: {"{:.2f}".format(novo_salario)}\nReajuste ganho: {"{:.2f}".format(ganho)}\nEm percentual: {percentual} %')

