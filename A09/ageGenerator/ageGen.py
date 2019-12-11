
import random
import os
import math

POPULATION = 1000 # Going below 1000 can cause more or less names to be generated depending on the distribution of the groups

age = os.path.dirname(__file__) + '/ages.txt'

RANGES = [(13,17),(18,24),(25,34),(35,44),(45,54),(55,64),(65,116)] # min, max age for each age group
AGES = len(RANGES) # number of age groups
DIST = [.058,.25,.322,.165,.102,.06,.043] #distribution of the age groups

agelist = []

for i in range (AGES):
    for x in range (math.ceil(POPULATION * DIST[i])):
        agelist.append(random.randint(RANGES[i][0], RANGES[i][1]))

with open(age,'w+',encoding='utf-8') as file:
    for age in agelist:
        file.write(str(age) + '\n')
# return agelist
