"""
Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.
"""

valores = []

for _ in range(5):
    entrada = int(input())
    valores.append(entrada)

count = 0
for e in valores:
    if e % 2 == 0:
        count += 1

print(f'{count} valores pares')