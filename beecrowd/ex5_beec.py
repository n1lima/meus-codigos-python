"""
Escreva um algoritmo que leia 2 números e imprima o resultado 
da divisão do primeiro pelo segundo. Caso não for possível mostre a mensagem “divisao impossivel” para os valores em questão.
"""

def divisoes (pares):
    resultados = []
    for x, y in pares:
        if y == 0:
            resultados.append('divisao impossivel')
        else:
            resultados.append(x/y)
    return resultados
 

N = int(input())

pares = []

for _ in range(N):
    x, y = map(int, input().split())
    pares.append((x, y))

resultados = divisoes(pares)

for resultado in resultados:
    print(resultado)

