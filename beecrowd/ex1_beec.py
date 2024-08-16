"""
Leia 3 valores inteiros e ordene-os em ordem crescente. 
No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.
"""

entrada = list(map(int, input().split()))

for e in sorted(entrada):
    print(e)

print()

for e in entrada:
    print(e)


"""
valores_c = entrada.copy() #colocar uma lista em outra as vezes ela ocupa o mesmo local da mémoria, ai precisa copiar a lista
valores_c.sort()

for e in valores_c:
"""