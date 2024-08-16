"""
Entre com uma sequencia de no mínimo 5 números reais, calcule a média ponderada,
utilizando 0.3 para os dois primeiros valores e para os dois últimos valores, e a 0.1 para
os valores intermediários, exiba o resultado.
"""
def verificacao (entrada):

    soma = 0
    pesoTotal = 0
    for i in range(4):
        soma += (entrada[i] * 0.3)  
        pesoTotal += 0.3      
    for i in range(4, len(entrada)):
        soma += (entrada[i] * 0.1)
        pesoTotal += 0.1

    
    media = soma / pesoTotal

    return media 



entrada = list(map(float, input('Entre com a sequencia de do min 5 numeros:').split()))

print(f'A media ponderada dessa sequencia sera: {round(verificacao(entrada),2)}')


"""
O uso de [4:] em Python é conhecido como "slicing". É uma forma de selecionar uma parte de uma sequência (como uma lista, tupla, ou string) a partir de um determinado índice até o final da sequência.

[4:]: Seleciona todos os elementos da posição 4 até o final da lista.
[:4]: Seleciona todos os elementos do início da lista até a posição 4 (mas não incluindo o elemento na posição 4).

EXEMPLO
lista = [0, 1, 2, 3, 4, 5, 6]
print(lista[4:])  # Saída: [4, 5, 6]
print(lista[:4])  # Saída: [0, 1, 2, 3]

"""

