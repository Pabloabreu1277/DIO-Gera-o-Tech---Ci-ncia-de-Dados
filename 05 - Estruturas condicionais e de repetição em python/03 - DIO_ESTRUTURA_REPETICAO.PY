#1) exemplo for com str

texto = input ( " Informe um texto : " )
VOGAIS = "AEIOU"
for letra in texto :
    if letra.upper( ) in VOGAIS :
        print( letra , end = " " )
else :
        print( ) # adiciona uma quebra de linha

print('#'*100)

#2) exemplo 2 for com range

for numero in range (0,51,5):
    print(numero, end=" ")
print('#'*100)

#3) exemplo com while

opcao = -1
while opcao != 0 :
    opcao = int( input( " [ 1 ] Sacar \n [ 2 ] Extrato \n [ 0 ] Sair \n: ") )
    if opcao == 1 :
        print ( " Sacando ... " )
    elif opcao == 2 :
        print ( " Exibindo o extrato ...." )
    
else :
    print ( " Obrigado por usar nosso sistema bancário , até logo ! " )

print('#'*100)

#4) exemplo while infinito

while True :
    numero = int ( input ( " Informe um número : " ) )
    if numero == 10 :
        break
    print ( numero )

for numero in range(100):
    if numero == 10:
        break
    print(numero, end=" ")