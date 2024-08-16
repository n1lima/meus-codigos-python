"""""
Crie uma função para calcular o fatorial de um número.
"""

def calculadoraDeFatorial (numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * calculadoraDeFatorial(numero - 1)

def main():
    numero = int(input("digite o numero"))
    print("o numero fatorial eh: ", calculadoraDeFatorial(numero))

main()