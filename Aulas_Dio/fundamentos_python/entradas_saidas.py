

nome = input("Infome seu nome: ")
sobrenome = input("Informe Seu Sobrenome: ")
idade = int(input("Qual sua idade: "))
print(nome)
print(sobrenome)
print(idade)

print(nome, sobrenome)
print(nome, sobrenome, end="...\n") #end terminar em ... adicionadno quebra de linha no final
print(nome, sobrenome, sep="#") #sep significa separador mudar separos de espaço para #
print(nome, sobrenome, idade, sep="***")
print(type(nome))
print(type(sobrenome))
print(type(idade))

