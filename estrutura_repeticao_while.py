#Reoetição While

opcao = -1

while opcao != 0:
    opcao = int(input(f'Digite Opção \n[1] Sacar \n[2] Extrato \n[3] Sair \n: '))
    
    if opcao == 1:
        print("Sacando....")
    elif opcao == 2:
        print("Extrato...")
else :
    print('Saiu por Opção sua ... = 0')
    
        