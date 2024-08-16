"""
Entre com uma sequencia de números reais em uma linha, e exiba na tela uma linha com
o fatorial de cada número da sequencia digitada.
"""
from functools import reduce

entrada = lambda: (list(map(float, input().split())))

fatorial = lambda n: reduce(lambda x, y: x * y, range(1, int(n) + 1)) if n > 0 else 1

fatoriais = list(map(fatorial, entrada()))
print("Fatoriais:", fatoriais)