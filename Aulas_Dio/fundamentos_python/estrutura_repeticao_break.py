#Estrutura Repetição Usando Break e Continue
while True :
    numero = int(input("Digite um valor: "))
    if numero % 2 == 0 :
        print('PAR')
    else:
        print('IMPAR - Saindo Iteração')
        break
        
for numero in range(25):
    if numero == 12:
        continue
    print(numero, end=" ")
print(" : Observe que o número 12 Não foi Impresso usando continue")