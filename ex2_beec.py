"""
Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos.
Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.
"""

valores = []

for _ in range(6):
    entrada  = float(input())
    valores.append(entrada)

count = 0
somaPositivos = 0

for e in valores:
    if e > 0:
        count += 1
        somaPositivos += e 

media = somaPositivos / count

print()
print(f'{count} valores positivos')
print(f'{media:.1f}')

