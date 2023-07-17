#Maiúsculas
curso = "   *pYtHon  *"
#Maiúsculo
print(curso.upper())
#Minúsculo]
print(curso.lower())
#Titúlo Primeira Maiúscula
print(curso.title())
curso = "   *pYtHon  "
#Removedo espaços em Branco da esquerda e direita
print(curso.strip()+ ".")
#Removedo espaços em Branco da esquerda left
print(curso.lstrip()+ ".")
#Removedo espaços em Branco da direita right
print(curso.rstrip()+ ".")
curso = "pYtHon"
#Centralizar String - #Será inserido 10 caracteres inseridos #, se não informar será espaço em Branco
print(curso.center(20, "#")) #width tamanho 
print(curso.center(20, " "))
#Junção de String Join - cada vez q passar por um item/caracter será adcionado "."
print("-".join(curso))
print(".".join(curso))