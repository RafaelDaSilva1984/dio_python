numeros = [1, 30 ,21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0 :
        pares.append(numero)
        print("Os números pares são:", pares )
        
numeros = [1, 30 ,21, 2, 9, 65, 34]
pares =[numero for numero in numeros if numero % 2 == 0]
print("In line Números Pares da Lista [1,30,21,2,9,65,34] são: ",pares)

numeros = [1, 30 ,21, 2, 9, 65, 34]
quadrado = []
for numero in numeros:
    quadrado.append(numero ** 2)
    print("Valores ao quadrado", quadrado) 

numeros = [1, 30 ,21, 2, 9, 65, 34, 34]
quadrado = [numero ** 2 for numero in numeros]
print("Valores ao quadrado in line sem o méthodo set", quadrado )
print("Valores ao quadrado in line coms o méthodo set", set(quadrado) )
