"""
Entre com duas sequencias numéricas de inteiros, cada sequência em uma linha, exiba
na tela o maior número das duas sequências, e o menor número das duas sequencias.
"""

def maiorEmenor(entrada1, entrada2):
    maior = entrada1[0]
    menor = entrada1[0]

    for i in entrada1:
        if i > maior: 
            maior = i
        elif i < menor:
            menor = i
        
    for i in entrada2:
        if i > maior:
            maior = i
        elif i < menor:
            menor = i
            
    return maior, menor  

entrada1 = list(map(int, input('Entre com a primeira sequencia de numero:').split()))
entrada2 = list(map(int, input('Entre com a segunda sequencia de numero:').split()))
maior, menor = maiorEmenor(entrada1, entrada2)
print(f'O maior numero das duas sequencias eh {maior} e o menor eh {menor}')