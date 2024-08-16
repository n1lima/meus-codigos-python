"""
Escreva uma função de nome quadrado, que recebe uma sequência de números inteiros e retorna uma lista com o quadrado de cada
elemento da lista.
"""

def quadrado (entrada):
    listaQuadrada = []

    for e in entrada: 
        listaQuadrada.append(e**2) #O operador "**" é usado para elevar um número a uma certa potência.

    return listaQuadrada

entrada = list(map(int,input().split()))
print(quadrado(entrada))