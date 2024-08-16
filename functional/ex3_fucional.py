"""
Idem ao 1c.
"""

entrada = lambda: input().split()

capsLock = list(map(str.upper, entrada()))
maior = max(capsLock, key=len)

print(f'{capsLock}\n{maior}')

"""
def strings (entrada):

    capsLock = (s.upper() for s in entrada) 
    maior = entrada[0]

    for palavra in entrada:
        if len(maior) < len(palavra):
            maior = palavra

    return capsLock, maior
"""