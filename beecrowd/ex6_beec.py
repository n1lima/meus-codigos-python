"""
Marcos trabalha em uma empreiteira, sua tarefa é cercar com estacas os terrenos onde serão construidos prédios. 
Existem duas restrições para a distribuição destas estacas, elas devem ser colocadas de tal forma que a distância entre duas estacas 
seja sempre igual, e a segunda restrição é que Marcos deve usar o menor número possível de estacas. Marcos é seu amigo e pediu para que 
você desenvolva um programa para ajudá-lo.

Entrada
Haverão diversos casos de teste, cada caso de teste é descrito em uma linha por dois números X e Y (1 ≤ X, Y ≤ 100000000), 
os quais representam as dimensões do terreno. O final da entrada é indicado por final de arquivo.

Saída
Para cada caso de teste imprima uma linha com o número mínimo de estacas necessário para cercar o tereno.
"""

import sys
import math

def numero_minimo_estacas(x, y):
    # Calcula o perímetro do terreno
    perimetro = 2 * (x + y)
    # Calcula o máximo divisor comum de X e Y
    mdc = math.gcd(x, y)
    # Calcula o número mínimo de estacas
    num_estacas = perimetro // mdc
    return num_estacas

# Leitura dos dados de entrada
for linha in sys.stdin:
    linha = linha.strip()  # Remove espaços em branco extras
    if linha:
        x, y = map(int, linha.split())  # Converte a linha para inteiros
        print(numero_minimo_estacas(x, y))


"""
sys para ler a entrada padrão.
math para usar a função gcd que calcula o máximo divisor comum.

.gcd
Definição: .gcd é um método da biblioteca math em Python que calcula o Máximo Divisor Comum (MDC) de dois números inteiros.
Uso: A função math.gcd(a, b) retorna o maior número inteiro que divide ambos 
sem deixar resto. É especialmente útil para simplificar frações ou encontrar o espaçamento mais 
eficiente entre pontos em problemas de geometria.
Exemplo:

import math

# Calcula o MDC de 24 e 36
resultado = math.gcd(24, 36)
print(resultado)  # Saída: 12

.strip
Definição: .strip() é um método de string em Python que remove todos os caracteres de espaço em branco (como espaços, tabs, quebras de linha) do início e do fim da string.
Uso: É útil para limpar strings de entrada, eliminando espaços extras que podem causar erros ao processar dados.
Exemplo:

texto = "  Olá, Mundo!  "
texto_limpo = texto.strip()
print(texto_limpo)  # Saída: "Olá, Mundo!"

"""
