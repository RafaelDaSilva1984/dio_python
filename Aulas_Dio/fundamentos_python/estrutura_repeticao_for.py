# Estrutura de repetição For e While
for i in range(0, 11):
    print([i])
c = 1
for tabuada in range(5, 51 , 5):    
    print(f'Tabuada do 5 x {c} ' , [tabuada])
    c += 1
   
texto = input("Informe um Texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra.upper(),'Vogal')
    else:
        print(letra.lower(),'Consoante')
