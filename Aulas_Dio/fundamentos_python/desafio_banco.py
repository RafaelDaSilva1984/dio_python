from datetime import date

print("========================Sistema Bancário Python=========================")
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
numero_depositos = 0
LIMITE_SAQUES = 3
data_atual = date.today()

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            numero_depositos += 1
        else:
            print("Operção falhou: O valor informado é inválido.")
        
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo 
        
        excedeu_limite = valor > limite 
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo Suficiente.")
        elif excedeu_limite:
            print("Operação falhou. O valor do saque excede o limite Diário.")
        elif excedeu_saques:
            print("Operação falhou: Número máximo de saques excedido.")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou: O valor informado é inválido.")
            
    elif opcao == "e":
        print("\n*************************EXTRATO***********************") 
        if saldo == 0 and numero_depositos <= 0 and numero_saques<= 0:
            print("Não foram realizada movimentações." )
        else:            
            print(f"\nSaldo: R$ {saldo:.2f}")
            print(f'=>========================Seu Saldo é: R$ {saldo:.2f} em {data_atual} <=') 
            print("\n*******************************************************")
        
    elif opcao == "q":
        print("Finalizando sessão!")
        break
        
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada...")
print('Obrigado, volte sempre')
