import random

nsamples = 1000
contA = 0
contB = 0

for _ in range(nsamples):
    face1 = random.choices(["CA", "CO"], weights=[2, 3])[0]
    face2 = random.choices(["CA", "CO"], weights=[2, 3])[0]
    face3 = random.choices(["CA", "CO"], weights=[2, 3])[0]

    if(((face1 == 'CA') and (face2 == 'CO')) or ((face1 == 'CO') and (face2 == 'CA'))):
        contA += 1
    elif((face2 == 'CO') and (face3 == 'CO')):
        contB += 1


PA = contA / nsamples
PB = contB / nsamples

print(PA)
print(PB)