"""
1º
entrada = map(int, input().split()) #O METODO .SPLIT() TRANSFORMA AS STRINGS EM UMA LISTA

numeros = list(entrada) #POR ISSO DEPOIS DE USAR O MAP, PRECISA TRANSFORMA A ENTRADA EM UMA LISTA E UMA VARIAVEL RECEBENDO ELA

print(numeros)
"""

entrada = input()

numeros = map(int, entrada.split()) #AQUI VAI RETORNAR O OBJETO MAP, POIS A VARIAVEL NUMEROS VAI ESTAR RECEBENDO ESSE OBJETO

print(numeros)

"""
2º
A função range pode ser usada de três maneiras principais:

range(stop):

Gera números de 0 até stop - 1.
Exemplo: range(5) gera [0, 1, 2, 3, 4].
range(start, stop):

Gera números de start até stop - 1.
Exemplo: range(2, 5) gera [2, 3, 4].
range(start, stop, step):

Gera números de start até stop - 1, com um incremento de step.
Exemplo: range(1, 10, 2) gera [1, 3, 5, 7, 9].

"""

lista = [1, 2, 3, 4]

for i in range(len(lista)):
    print(f'elemento {i}: {lista[i]}')


"""
3º
O método .append() é utilizado em listas no Python para adicionar um item ao final da 
lista. Ele modifica a lista original, acrescentando o novo item sem criar uma nova lista. Aqui está um exemplo básico de como ele funciona:
"""

# Criando uma lista vazia
minha_lista = []

# Adicionando elementos à lista
minha_lista.append(1)
minha_lista.append(2)
minha_lista.append(3)

# Exibindo a lista
print(minha_lista)


# Em loop's
numeros = []
for i in range(5):
    numeros.append(i)
print(numeros)
# [0, 1, 2, 3, 4]

"""
4º
Diferença entre append e extend
"""
#- Append adiciona um bloco ao todo, é bom quando você quer adicionar uma lista inteira dentro da outra
valores = [1, 2]

valores.append([3, 4])

print(valores)

"""
- Extend adiona um por um, então não importa se você colocar "abc", ele vai adicionar ['a', 'b', 'c']. É bom para quando você quer colocar
um elemnto de cada vez
"""

lista = [1, 2]

lista.extend([2, 3])

print(lista)

"""
5º
o que usar no for para ir "até" em uma lista? for in range(len(lista)), lista ou enumerate(lista)?
"""

# para  modificar e acessar, tanto o elemento quanto o indice de uma lista
for i in range(len(lista)):
    print(f"{lista[i]}\n{i}")

# para acessar ou iterar apenas o elemento da lista
for e in lista:
    print(e)

# para poder iterar e acessar ao mesmo tempo o indice e o elemento, mas de "forma separada" no for
for i, e in enumerate(lista):
    print(f"{i}\n{e}")

"""
6º
como fazer raiz quadrada
"""
# precisa importar a biblioteca math, então:

import math

num = 14
raiz_quadrada = math.sqrt(num)
print(raiz_quadrada)

# ou, quando for numeros elevado a potencia

num1 = 13 ** 2
num2 = 15 ** 2
raiz_quadrada = math.sqrt(num1 + num2)
print(raiz_quadrada)

# ou, pode utilizar o metodo pow(base, expoente)
num1 = 13 
num2 = 15 
raiz_quadrada = math.sqrt(pow(num1, 2)) + (pow(num2,2))
print(raiz_quadrada)