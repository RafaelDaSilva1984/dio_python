def sacar(valor):
    saldo = 500
    
    if saldo >= valor:
        print("Valor Sacado")
        print("Retire seu dinheiro na boca do caixa.")
        
    print("Obrigado por ser nosso Cliente.")
    
    
    
def depositar(valor):
    saldo = 500
    saldo += valor
    print(saldo)
        
sacar(1000)
depositar(1500)

