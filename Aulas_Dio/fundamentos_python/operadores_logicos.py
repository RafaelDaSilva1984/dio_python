#Operadores Lógicos

saldo = 1000
saque = 250
limite = 200
conta_especial = True

if (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque):
    print("Saque autorizado")

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficinente = conta_especial and saldo >= saque

if conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficinente:
    print('Saque Autorizado')