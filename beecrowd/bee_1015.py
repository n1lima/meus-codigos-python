"""
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais, segundo a fórmula:

Distancia = √(x2 - x1)² + (y2 - y1)²
"""
import math

x1, y1 = (list(map(float, input().split())))
x2, y2 = (list(map(float, input().split())))

p1 = (x2 - x1)
p2 = (y2 - y1)

distancia = math.sqrt(pow(p1, 2) + pow(p2, 2))
print(f"{distancia:.4f}")

"""
import math

x1, y1 = (list(map(float, input().split())))
x2, y2 = (list(map(float, input().split())))

p1 = (x2 - x1)**2
p2 = (y2 - y1)**2

distancia = math.sqrt(p1 + p2)
print(f"{distancia:.4f}")
"""