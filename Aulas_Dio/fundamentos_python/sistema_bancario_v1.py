from datetime import date

print("========================Sistema Bancário V1=========================")
print(" ")

print("MENU DE OPERAÇÕES:")
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Digite opção desejada => """

saldo = 0
limite = 500
extrato = " "
numero_saques = 0
LIMITE_SAQUES = 3
contador_deposito = 0
contador_extratos = 0
listagem = []
listagem_deposito = 0
listagem_sacar = []
listagem_saques= 0
data_atual = date.today()

while True:
    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Qual valor será depositado: "))
        
        while deposito <= 0 :
            print("Valor de Depósito não Aceito, deve ser maior que R$ 0.00.")
            deposito = float(input("Qual valor deseja depositar em sua conta: "))
        contador_deposito += 1
        saldo += deposito        
        for c in range(contador_deposito):            
            listagem.append(deposito)
            listagem_deposito = set(listagem)   
             

    elif opcao == "s":
        sacar = float(input("Qual valor você deseja Sacar: "))                   
        if saldo <= 0 :
            print('Saldo Insuficiente, para Saque')
        elif sacar == 0 :
            print("Operação Falhou: Valor informado é inválido.")
        elif sacar > saldo:
            print ( 'Saque Não Permitido! Seu Saldo está insuficiente')
            break
        elif sacar > 500:
            print ('O Valor do saque deve ser menor que o limite permitido.')           
        elif numero_saques >= 3:
            print ("Você atingiu seu Limite de Saques")
            break            
        else:            
            print(f'Saque bem Sucedido, saque diário {numero_saques +1} limite diário: {LIMITE_SAQUES}')            
            saldo -= sacar
            numero_saques += 1 
            
        for c in range(numero_saques):  
            listagem_sacar.append(sacar)
            listagem_saques = set(listagem_sacar)   
            
    elif opcao == "e": 
        print("************************EXTRATO**********************")
        extrato = saldo
        
        if contador_deposito == 0 and numero_saques == 0:
            print("     Não foram realizadas movimentações em Conta!! ")            
            
        elif saldo > 0:                             
            print(f'Depósito número: {contador_deposito} \n Valor  R$ {listagem_deposito}')          
           
        if numero_saques <= 0 :
            print("  ")
        else:            
            print(f'Saque número:  {numero_saques} \n Valor  R$ {listagem_saques}\n')          
        print(f'=>========================Seu Saldo é: R$ {extrato:.2f} em {data_atual} <=') 
        
    elif opcao == "q":
            print("Finalizando sessão!")
            break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada...")
print(f" \n Saldo em Conta: R$ {saldo:.2f}")
print(f'\nObrigado, volte sempre')
