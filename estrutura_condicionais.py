# Condicionais

# if = (se)
# elif = (se e se não se) só retorna verdadeiro
# else = senão

MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input(f'Informe sua idade: '))

if idade >= MAIOR_IDADE:
    print(f'Você é maior de idade, pode retirar CNH. Você tem {idade} anos')
if idade == IDADE_ESPECIAL:
    print(f'Com {IDADE_ESPECIAL}, você pode fazer somente aulas teóricas.')
elif idade < MAIOR_IDADE:
    print(f'Você não pode tirar CNH, faltam {MAIOR_IDADE - idade} anos, até a atingir os {MAIOR_IDADE} anos')
