"""
Entre com uma sequencia de no mínimo 5 números reais, calcule a média ponderada,
utilizando 0.3 para os dois primeiros valores e para os dois últimos valores, e a 0.1 para
os valores intermediários, exiba o resultado.
"""

def mediaPonderada (lista): 

    count = 0

    for e in 3:
        e = lista
        num = float(e)
        count += (num*0.3)
    for e in lista:
        num = float(e)
        count += (num*0.1)

    media = count / len(lista)

    return media


entrada = input('entre com a sequencia de no minimo 5 numeros reais: ')
listaDeReais = entrada.split()
print(f'A media ponderada dos numeros que foram inseridos eh {mediaPonderada(listaDeReais)}')

