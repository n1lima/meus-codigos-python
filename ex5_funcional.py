"""
Entre com 3 sequencias de números inteiros, uma sequencia em cada linha. Exiba na tela
em uma linha a sequencia dos números em ordem crescente sem números iguais.
"""
# Função para entrada de sequências de números inteiros
entrada = lambda: set(map(int, input().split()))

# Entrada das três sequências de números inteiros e combinação em um único conjunto
todos_numeros = set().union(*(entrada() for _ in range(3)))

# Exibindo a sequência resultante em ordem crescente sem números iguais
print("Sequência em ordem crescente sem números iguais:", sorted(todos_numeros))

"""
# Função para entrada de sequências de números inteiros
entrada = lambda: set(map(int, filter(lambda x: x.strip(), input().split())))

# Entrada das três sequências de números inteiros e combinação em um único conjunto
todos_numeros = set().union(*(entrada() for _ in range(3)))

# Exibindo a sequência resultante em ordem crescente sem números iguais
print("Sequência em ordem crescente sem números iguais:", sorted(todos_numeros))

"""