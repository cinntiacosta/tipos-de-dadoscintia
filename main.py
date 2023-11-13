#tipos de dados: str 

nome = "Cintia"
idade = 28
altura = 1.70
peso = 54.0
print(nome, idade, altura, peso)

frase = "Letramento digital em Londrina."
print(frase)
frase_maiuscula = frase.upper()
print("A frase em maiúsculas é: ", frase_maiuscula)
frase_minuscula = frase_maiuscula.lower()
print("A frase em minúsculas é: ", frase_minuscula)

print(frase.replace("digital", "Londrina"))
print(frase.replace("Londrina", "Pato Branco"))

print("-----------------------")
# Tipo de dados: int

idade = 28
print(idade)
print(type(idade))
print(str(idade) + "2")
print(float(idade))

print("-----------------------")
# Tipo de dados: float

altura = 1.70
print(altura)
print(type(altura))
print(int(altura))

print("-----------------------")	

import math

print(math.ceil(altura))

temperatura = -2.3
print(temperatura)
print(int(temperatura))
print(math.ceil(temperatura))
print(math.floor(temperatura))

n1 = 3.345
print("n1 = ", round(n1, 2))

print("-------------------------")
# Tipos de dados: complex

complexo = 4 + 7j
print(complexo)
print(type(complexo))

print(complexo.real)
print(complexo.imag)

complexo2 = 5 + 12j

soma = complexo + complexo2
print(soma)

print("-------------------------")
# Tipo de dados: bool

booleano1 = True
print(booleano1)
booleano2 = False
print(booleano2)
print(type(booleano1))

print("pergunta?", 3 > 15)

print(booleano1 and booleano2)

booleano3 = True

print("not", not(booleano3))

print(booleano1 or booleano2)

print("-------------------------")
# Tipo de dados: list

numeros = [1, 2, 3, 4, 5]
nomes = ["Paula", "Leonardo", "Gabriela"]
misturado = [8, "Paula", 5.6, True]

print(numeros)
print(nomes)
print(misturado)
print(type(numeros))

print("posição: ", numeros[3])
print("posição: ", nomes[2])
print("posição: ", misturado[1])

print(len(misturado)) # quantidade elementos
print(len(nomes))
print(len(numeros))

numeros.append(6) # adiciona elemeno
print(numeros)

nomes[0] = "Flávia" # modificando elemento
print(nomes)

misturado[3] = False
print(misturado)

misturado.remove(8) # remove elemento
print(misturado)


print("------------------------")
# Tipo de dados: tuple

numero = (5, 6, 7)
cores = ("vermelho", "azul", "verde")
misturada = (3, "dois", 3.0)

print(numero)
print(cores)
print(misturada)
print(type(numero))

print(cores[1])
print(len(misturada))

#numero.append(6) # adiciona elemento
print(numero)

#misturada.remove(1) # remove elemento
print(misturada)

#numero[0] = 2 # modifica elemento
print(numero)


print("-----------------------")
# Tipo de dados: set

numeral = {1, 2, 3, 4, 4, 5, 6}

print(numeral)
print(type(numeral))
print(len(numeral))

conjunto = {3, 5, 8, 9}
print(conjunto)

intersecao = numeral & conjunto
print(intersecao)

uniao = numeral | conjunto
print(uniao)

diferenca = numeral - conjunto
print(diferenca)

uniao.add(7)
print(uniao)

uniao.remove(9)
print(uniao)

print("-----------------------")
# Tipo de dados: dict

pessoa = {"nome": "Julia", "idade": 13, "cidade": "São Paulo"}
notas = {"português": 7.5, "matemática": 8.0, "biologia": 9.5}

print(pessoa)
print(type(pessoa))

print(pessoa["nome"])
print(notas["biologia"])
print(notas["matemática"])

pessoa["endereço"] = "Rua XV de novembro, 73" # adiciona uma nova chave-valor
print(pessoa)

print(pessoa["endereço"]) # busca o valor dentro da chave
print(pessoa.get("endereço"))

pessoa.pop("cidade") # apaga elelmento
print(pessoa)

pessoa.clear() # limpa todo dicionário
print(pessoa)

lista_pessoas = [8, "dois", 4.3,
  {"nome": "Lucia", "idade": 56, "cidade": "Florianópolis"},
  {"nome": "Carol", "idade": 23, "cidade": "Curitiba"},
  {"nome": "Márcio", "idade": 42, "cidade": "Porto Alegre"}
]
print(lista_pessoas)



