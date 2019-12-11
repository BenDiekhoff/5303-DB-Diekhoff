#!/usr/bin/python

import argparse
import re
import json
import csv
import generate as gen
import random

# Uncomment the block below to make the program prompt your for input
##############################################################################
# filetype = input("Enter 'csv' or 'json' to choose your output file type: ")
# numstring = input("Enter the number of users you want to generate: ")
# num = int(numstring)
###############################################################################


# Comment out the block below to remove the required command line arguments
################################################################################# 
parser = argparse.ArgumentParser(description='Generate a random data file.')
parser.add_argument('filetype', metavar='<file type>', type=str, nargs=1,
                action='store',
                help='type \'csv\' or \'json\' to choose your output file type')

parser.add_argument('num', metavar='<number of users>', type=int, nargs=1,
                help='the number of users to generate data for')
args = parser.parse_args()
filetype = args.filetype[0]
num = int(args.num[0])
##################################################################################


def csvFile():
    ls = gen.username(num)
    count = 0
    with open('data.csv', 'w+', newline='') as file:
        write = csv.writer(file)
        write.writerow(['user_id', 'email', 'username', 'first_name',
            'last_name', 'password', 'create_time', 'last_update', 'age'])

        ageList = gen.ageList(num)
        for username in ls:
            firstEmail = username[0]
            secondEmail = re.findall ('[A-Z][^A-Z]*', username)
            dom = gen.emailDomain()
            email = str(firstEmail) + "." + str(secondEmail[0]) + str(dom)
            fName = gen.firstName()
            lName = gen.lastName()
            password = gen.password()
            date = gen.createTime()
            createTime = date.date()
            lastUpdate = gen.lastUpdate(date)
            age = random.choice(ageList)
            ageList.remove(age)


            write.writerow([str(count), email,
            str(username), fName, lName, password, 
            str(createTime), lastUpdate, int(age)])
            count += 1



def jsonFile():
    ls = gen.username(num)
    count = 0
    data = []
    with open('data.json', 'w+') as file:
        ageList = gen.ageList(num)
        for username in ls:
            firstEmail = username[0]
            secondEmail = re.findall ('[A-Z][^A-Z]*', username)
            dom = gen.emailDomain()
            email = str(firstEmail) + "." + str(secondEmail[0]) + str(dom)
            fName = gen.firstName()
            lName = gen.lastName()
            password = gen.password()
            date = gen.createTime()
            createTime = date.date()
            lastUpdate = gen.lastUpdate(date)
            age = random.choice(ageList)
            ageList.remove(age)
			
            data.append({
                'user_id': count,
                'email': email,
                'username': username,
                'first_name': fName,
                'last_name': lName,
                'password': password,
                'create_time': str(createTime),
                'last_update': str(lastUpdate),
                'age': int(age)
                })
    
            count += 1
            json.dump(data, file) #, indent=4) 
        # indent=4 gives the file pretty formatting but uses many more lines



if filetype == 'csv': 
    csvFile()
elif filetype == 'json':
     jsonFile()

