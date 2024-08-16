"""
Entre com uma sequencia de números inteiros na mesma linha, exiba a soma somente
dos números pares da sequencia digitada.
"""
from functools import reduce

entrada = lambda: (list(map(int, input().split())))

isPar = lambda x: True if x % 2 == 0 else False
listaDePares = lambda lista: (list(filter(isPar, lista)))

soma = lambda x, y: x + y
listaSoma = lambda lista:  reduce(soma, lista)

print(f'SOMA: {listaSoma(listaDePares(entrada()))}')
