#Listas Aulas
frutas = ["laranja", "maca", "uva"]
print(frutas)
print(frutas[0])
print(frutas[1])
print(frutas[2])
print(f'decrescente, o último valor é: ',frutas[-1])

frutas = []
print(frutas)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro =["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

matriz = [
    ['A', 'B', 1],
    [2, 'C', 'D'],
    [-3.5,'E', 4]
]
print(matriz)
print(matriz[0][1])
print(matriz[0][-1])#último valor da primeira linha 
print(matriz[-1][-1])#último valor da última linha

lista = ["p","y","t","h","o","n"]
print(lista)
print(lista[2:],"valor após o indice 2") # valor após o indice 2
print(lista[:2],"valor antes o indice 2") # valor antes o indice 2
print(lista[1:3],"valores 1 e 3") # valores 1 e 3
print(lista[0:3:2],"valores pulando de 2 em 2, iniciando em 0 e finalizando no 3 - 1 = 2") # valores pulando de 2 em 2 
print(lista[::],"todos os valores") # todos os valores
print(lista[::-1],"todos valor invertidos") # todos valor invertidos

carros = ["Gol", "Celta", "Palio"]
print(carros)
for carro in carros:
    print(carro)
    
carros = ["Gol", "Celta", "Palio"]
print(carros," enumerate")
for indice, carro in enumerate(carros):
    print(f'{indice} : {carro}')
    
