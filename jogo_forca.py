"""
Jogo da Forca:
Desenvolva um jogo da forca onde uma função escolhe uma palavra aleatória e outra função verifica as letras fornecidas pelo jogador.
"""

palavra = 'Python'

acertos = 0
erros = 0

while acertos != len(palavra) or erros != len(palavra):
    tentativas = input('Digite uma letra')
    if tentativas in palavra:
         print("você acertou uma letra")
         acertos += 1
    else:
         print("voce errou uma letra")
         erros += 1 
