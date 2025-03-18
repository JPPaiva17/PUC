from random import uniform
from math import sqrt

raio1 = 1
raio2 = 1
numeroAmostras = 100000
contDentroAreaCultivada = 0
for _ in range(numeroAmostras):
    x = uniform(0, 1)
    y = uniform(0, 1)

    distancia1 = sqrt(((x - 0)**2) + ((y - 0)**2))
    distancia2 = sqrt(((x - 1)**2) + ((y - 1)**2))

    if((distancia1 <= raio1) and (distancia2 <= raio2)):
        contDentroAreaCultivada +=1
    





pDentroAreaCultivada = contDentroAreaCultivada / numeroAmostras
areaTotal = 1
areaCultivada = pDentroAreaCultivada * areaTotal
aduboPorQuilometro = 200
numeroMeses = 12
quantidadeAdubo = areaCultivada * aduboPorQuilometro * numeroMeses

print('Quantidade (kg) = ', quantidadeAdubo)

