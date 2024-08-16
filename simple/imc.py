"""
Problema:
Desenvolva um programa em Python que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O IMC é calculado dividindo o peso (em quilogramas) pela altura (em metros) ao quadrado.

O programa deve fazer o seguinte:

1. Solicitar ao usuário que insira seu peso em quilogramas.
2. Solicitar ao usuário que insira sua altura em metros.
3. Calcular o IMC usando a fórmula: IMC = peso / (altura ** 2).
4. Imprimir o resultado do IMC.

Exemplo de uso:
Digite seu peso em kg: 70
Digite sua altura em metros: 1.75
Seu IMC é: 22.86
"""

def calculadoraImc(peso, altura):
    
    imc = peso / (altura ** 2) #A altura é elevada ao quadrado
    return imc

def verificarImc (imc):
    if imc < 18.5:
        return 'abaixo do peso'
    elif imc >= 18.5 and imc <=24.9:
        return 'peso normal'
    elif imc >= 25.0 and imc <=29.9:
        return 'sobrepeso'
    elif imc >= 30.0:
        return 'obesidade'

peso = int(input('Insira seu peso em kg: '))
altura = float(input('Insira dua altura em metros: '))
imc = calculadoraImc(peso, altura)
print(f'Seu IMC eh: {round(imc, 2)} e sua categoria eh {verificarImc(imc)}') #Para delimitar ponto após a virgula

