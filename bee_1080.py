"""
Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos
"""

valores = []

for _ in range(100):
    valores.extend(list(map(int, input().split())))

maior = valores[0]
posicao = 0

for i in range(len(valores)):
    if valores[i] > maior:
        maior = valores[i]
        posicao = i+1

print(f"{maior}\n{posicao}")