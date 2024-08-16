"""
Escreva um programa que o usuário irá digitar em uma sequencia de números inteiros, e o programa deverá retornar uma lista com todos os números
dobrados(multiplicados por 2) que sejam positivos. Exemplo: 

Entrada:
1 2 3 -1 -2 0

Saida:
[2, 4, 6]
"""

entrada = lambda: (list(map(int, input().split())))

isPositivo = lambda x: x > 0 
listaPositivo = lambda lista: (list(filter(isPositivo, lista))) 
"""
filter(isPositivo, lista): Aplica a função isPositivo a cada elemento da lista e retorna apenas aqueles que são True (números positivos).
list(): Converte o objeto filter resultante em uma lista de números positivos.
"""

dobro = lambda lista: (list(map(lambda x : x*2,lista)))
listaProcessada = lambda lista: dobro(listaPositivo(lista))
"""
listaPositivo(lista): Aplica a função listaPositivo para obter uma lista de números positivos.
dobro(): Aplica a função dobro para dobrar os números positivos.
"""
saida = lambda lista: f'{listaProcessada(lista)}'

print(saida(entrada()))
"""
entrada(): Chama a função 
entrada para ler e processar a entrada do usuário, retornando uma lista de inteiros.
saida(): Chama a função saida para processar a lista de entrada, filtrando os positivos e dobrando-os, 
e retorna a lista formatada como uma string.
"""