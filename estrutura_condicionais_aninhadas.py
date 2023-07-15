conta_normal = False
conta_universitaria = False
conta_especial = True

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque será Realizado com Sucesso, Conta Normal")
    elif saque <= (saldo + cheque_especial):
        print('Saque realizado através de cheque Especial')
    else:
        print(f'O Saque não pode ser efetuado pois o Saldo é Insuficiente, nem mesmo com Cheque Especial, seu SALDO= R$ {saldo + cheque_especial} tentativa de saque = R$ {saque}')                         
elif conta_universitaria:
    if saldo >= saque:
        print("Saque será Realizado com Sucesso Conta Universitária")
    else:
        print(f"Saldo insuficiente. O valor do seu sacado é 0.")
elif conta_especial:
    print('Conta Especial Selecionda...')
else:
    print('Sua conta não foi reconhecida, entre e contato com seu Gerente.')