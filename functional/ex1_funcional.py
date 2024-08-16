

entrada = lambda: (list(map(int, input().split())))

isPar = lambda x: True if x % 2 == 0 else False
listaDePares = lambda lista: (list(filter(isPar, lista)))

isImpar = lambda y: True if (y % 2) != 0 else False
listaDeImpares = lambda lista: (list(filter(isImpar, lista)))

saida = lambda lista: f'lista de pares {listaDePares(lista)}\nlista de impares {listaDeImpares(lista)}'
#Precisa criar um lambda para saida, pois a função lambda vai receber o argumento lista e retornar ele

print(saida(entrada()))# Leitura da entrada, processamento e impressão do resultado