"""
Usuário deve entrar com uma sequencia numérica de inteiros 
em uma linha, exiba na tela qual o maior, qual o menor, e calcule a média aritmética dos valores.
"""

entrada = input()
listaDeEntrada = entrada.split() #Split ira quebrar cada elemento em uma string 

maior = int(listaDeEntrada[0])
menor = int(listaDeEntrada[0])
soma = 0

for e in listaDeEntrada:
    soma += int(e)
    if maior < int(e):
        maior = int(e)
    if menor > int(e):
        menor = int(e)

media = soma / len(listaDeEntrada)

print(f'O maior numero eh: {maior}')
print(f'O menor numero eh: {menor}')
print(f'A media da lista eh: {media:2f}')


#VERSAO COM FUNCAO
"""
def verificacao (listaDeEntrada):
    maior = int(listaDeEntrada[0])
    menor = int(listaDeEntrada[0])
    soma = 0

    for e in listaDeEntrada:
        num = int(e)
        soma += num
    if maior < num:
        maior = num
    if menor > num:
        menor = num

    media = soma / len(listaDeEntrada)

    return maior, menor, media
    
entrada = input()
listaDeEntradas = entrada.split()
maior, menor, media = verificacao(listaDeEntradas)
print(f'O maior numero eh: {maior}')
print(f'O menor numero eh: {menor}')
print(f'A media da lista eh: {round(media, 2)}')
"""

"""
entrada =  input().split()

menor = int(entrada[0])
maior = int(entrada[0])

soma = 0
for i in range(0,len(entrada)):
    entrada[i] = int(entrada[i])
    soma += entrada[i]
    if menor > entrada[i]:
        menor = entrada[i]

    if maior < entrada[i]:
        maior = entrada[i]

print(entrada)
print("Menor valor "+str(menor))
print("Maior valor "+str(maior))
print("Media: "+str(soma/len(entrada)))
"""