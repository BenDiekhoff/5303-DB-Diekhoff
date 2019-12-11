import os
import random
import string
import math
from datetime import datetime, timedelta
from random import randrange


directory_path = os.path.dirname(__file__)

# Usernames
def username(num_results=1):
    adjectives, nouns = [], []
    with open(os.path.join(directory_path, 'data', 'adjectives.txt'), 'r') as file_adjective:
        with open(os.path.join(directory_path, 'data', 'nouns.txt'), 'r') as file_noun:
            for line in file_adjective:
                adjectives.append(line.strip())
            for line in file_noun:
                nouns.append(line.strip())

    usernames = []
    for _ in range(num_results):
        adjective = random.choice(adjectives)
        noun = random.choice(nouns).capitalize()
        num = str(random.randrange(10))
        usernames.append(adjective + noun + num)

    return usernames

# Email domains
def emailDomain():
    with open(os.path.join(directory_path, 'data', 'domains.txt'), 'r') as file_domain:
        dom = random.choice(file_domain.read().splitlines())
        domain = '@' + dom

    return domain

# First names
def firstName():
    with open(os.path.join(directory_path, 'data', 'firstNames.txt'), 'r') as file_fNames:
        name = random.choice(file_fNames.read().splitlines())

    return name

# Last names
def lastName():
    with open(os.path.join(directory_path, 'data', 'lastNames.txt'), 'r') as file_lNames:
        name = random.choice(file_lNames.read().splitlines())

    return name

# Passwords
def password(length = 11):
    chars = string.ascii_letters + string.digits 
    pw = ''
    for i in range(length):
        pw += pw.join(random.choice(chars))

    return pw

# Creation times
def createTime():
    oldest = datetime.strptime('1/1/2009', '%m/%d/%Y')
    newest= datetime.strptime('12/31/2019', '%m/%d/%Y')
    delta = newest - oldest
    dateRange = (delta.days)
    randomDays = randrange(dateRange)    
    date = oldest + timedelta(days=randomDays)

    return date

# Last update times
def lastUpdate(oldest = datetime.strptime('1/1/2009', '%m/%d/%Y')):
    newest= datetime.strptime('12/31/2019', '%m/%d/%Y')
    delta = newest - oldest
    dateRange = (delta.days)
    randomDays = randrange(dateRange)    
    date = oldest + timedelta(days=randomDays)
    date = date.date()

    return date

def ageList(POPULATION):
    #age = os.path.dirname(__file__) + '/ages.txt'

    RANGES = [(13,17),(18,24),(25,34),(35,44),(45,54),(55,64),(65,116)] # min, max age for each age group
    AGES = len(RANGES) # number of age groups
    DIST = [.058,.25,.322,.165,.102,.06,.043] #distribution of the age groups

    agelist = []

    for i in range (AGES):
        for x in range (math.ceil(POPULATION * DIST[i])):
            agelist.append(random.randint(RANGES[i][0], RANGES[i][1]))
    

    # with open(age,'w+',encoding='utf-8') as file:
    #     for age in agelist:
    #         file.write(str(age) + '\n')
    return agelist




    
