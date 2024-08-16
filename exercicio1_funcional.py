"""
Usuário deve entrar 
com uma sequencia numérica de inteiros, e deve exibir na telas duas linhas, uma linha com os números ímpares, e outra linha com os pares.
"""
from functools import reduce 


entrada = lambda: [int(e) for e in input().split()]

isPar = lambda x: True if (x % 2) == 0 else False
listaDePares = lambda l : list (filter(isPar, l))

isImpar = lambda y: True if (y % 2) != 0 else False
listaDeImpares = lambda l: list(filter(isImpar, l))

saida = lambda l: f'Pares: {listaDePares(l)}\n Impares: {listaDeImpares(l)}'

print(saida(entrada()))