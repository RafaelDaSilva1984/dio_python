print(30*"----")
print('Old Style %')
nome="Rafael"
idade=38
profissao="Pcm"
linguagem="Python"
print("Olá me chamo %s. Eu tenho %d anos de idade, trabalho com %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))
print(30*"----")
print('.format')
nome="Rafael Silva"
idade=38
profissao="Pcm"
linguagem="Python"
dados = {"nome": "Rafinha", "idade": 38,"profissao": "Pcm", "linguagem": "Python"}
print("Olá me chamo {}. Eu tenho {} anos de idade, trabalho com {} e estou matriculado no curso de {}." .format (nome, idade, profissao, linguagem))
print("Olá sou {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}." .format (**dados))
print(30*"----")
print('f"fstring"')
nome="Rafael Da Silva"
idade=38
profissao="Pcm"
linguagem="Python"
PI = 3.14159999
print(f'Olá me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}. \n Valor PI= {PI:.2f} e {PI:10.2f}')
print(30*"----")
