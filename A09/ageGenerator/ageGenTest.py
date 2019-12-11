
import random
import os

age = os.path.dirname(__file__) + '/ages.txt'


RANGES = [(13,17),(18,24),(25,34),(35,44),(45,54),(55,64),(65,116)]
counts = [0,0,0,0,0,0,0]


with open(age,'r',encoding='utf-8') as infile:
    for age in infile:
        x = int(age)
        if x >= 13 and x <=17:
            counts[0] += 1
        elif x >= 18 and x <=24:
            counts[1] += 1
        elif x >= 25 and x <=34:
            counts[2] += 1
        elif x >= 35 and x <=44:
            counts[3] += 1
        elif x >= 45 and x <=54:
            counts[4] += 1
        elif x >= 55 and x <=64:
            counts[5] += 1
        elif x >= 65 and x <=116:
            counts[6] += 1

total = 0
for i in range(7):
    print (counts[i])
    total += counts[i]
    print(total)

print (total)
print(counts)
        
