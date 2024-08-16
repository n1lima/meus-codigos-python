"""
Usuário deve entrar com uma sequencia numérica de inteiros em uma linha, exiba na
tela qual o maior, qual o menor, e calcule a média aritmética dos valores.
"""

def verificacao (entrada):
    maior = (entrada[0])
    menor = (entrada[0])
    soma = 0

    for e in entrada:
        soma += e
        if maior < e:
            maior = e
        elif menor > e:
            menor = e

    media  = soma / len(entrada)

    return maior, menor, media 
        
entrada = list(map(int, input('Entre com uma sequencia de numeros: ').split()))

maior, menor, media = verificacao(entrada)

print(f'O maior numero da sequencia eh {maior}, o menor eh {menor} e a media dessa sequencia eh {media} ')

 
