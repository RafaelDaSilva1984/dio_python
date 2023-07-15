#Condicionais Ternário

saldo = 1000
saque = 5000

status = "Sucesso" if saldo >= saque else "Falha" # se veradeiro retorna o que está no ínicio e se for falso o final.
print(f'{status} ao realizar Saque!')