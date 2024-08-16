"""
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1,
o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.
"""

entrada1 = list(map(float, input().split()))
entrada2 = list(map(float, input().split()))

quantidade1 = entrada1[1]
valor1 = quantidade1 * entrada1[2]

quantidade2 = entrada2[1]
valor2 = quantidade2 * entrada2[2]

valorTotal = valor1 + valor2

print(f'VALOR A PAGAR: R$ {valorTotal:.2f}')