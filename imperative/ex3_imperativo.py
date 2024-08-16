"""
Entre com uma sequencia de 3 Strings, retorne todas as Strings no formato caixa alta, e
indique qual delas possui a maior quantidade de caracteres.
"""

def tranformandoStrings (entrada):

    maiorString = entrada[0]

    for string in entrada:
        if len(maiorString) < len(string):
            maiorString = string

    stringsEmCapsLock = [s.upper() for s in entrada]

    return stringsEmCapsLock, maiorString



entrada = input('Entre com uma sequencia de 3 palavras: ').split()
capsLock, maior = tranformandoStrings(entrada)
print(f'as palavras em capslock: {capsLock} ')
print(f'a maior string eh: {maior}')

"""
No Python, o loop for pode iterar diretamente sobre os elementos de uma lista (ou de qualquer iterável), não apenas sobre os índices. Quando
você escreve for palavra in entrada, você está dizendo ao Python para percorrer cada elemento da lista entrada, atribuindo o valor de cada 
elemento à variável palavra. Não precisa colocar for i in len(entrada), ele já entendi que é que para percorrer cada elemento da lista.
No caso melhor de se usar é para ver o tamanho da palavra, como len(maiorString), que recebi a primeira palavra, ela vai ver o seu tamanho e
compara com a palavra é o indice 0 também
"""

"""
 upper() em Python é um método de strings que retorna uma versão da string original em letras maiúsculas. Para aplicar esta função a 
 cada elemento da lista, é necessário iterar sobre a lista e aplicar a função a cada elemento individualmente.
 Em seu código original, você estava tentando aplicar a função upper() a um intervalo de índices usando uma compreensão de 
 lista range(len(entrada)). Isso não funcionaria corretamente, pois range(len(entrada)) criaria um intervalo de números 
 de 0 a len(entrada) - 1, e você tentou chamar upper() em números, o que resultaria em um erro.
 A maneira correta de aplicar upper() a cada elemento da lista é usar uma compreensão de lista para iterar sobre os elementos da lista e 
 aplicar upper() a cada elemento individualmente.
"""

