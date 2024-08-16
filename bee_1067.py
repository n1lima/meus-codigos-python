"""
Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X, se for o caso.
"""

X = int(input())

for i in range(0, X+1, 1):
    if i % 2 != 0:
        print(i)