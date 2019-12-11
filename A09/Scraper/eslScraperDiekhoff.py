import requests
import urllib.request
import time
from bs4 import BeautifulSoup # pip install beautifulsoup4
import re
import io # used to prevent charmap errors
import os

url = 'https://www.eslfast.com/robot/'  #starting url
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
ls = soup.findAll('a')[1:26]

link = [] # holds the second part of the url
target = [] # holds the final version of the url, the target url.
for x in ls:
    url2 = x['href']
    link.append(url + url2) # second part url

for url in link:
    url = url.replace('.htm', '') # remove .htm since we're going to concatenate another string to this
    time.sleep(1)   # So I don't DoS or get kicked off the website
    print ('\n' + url +'\n------------------------------------------------------------------------------------')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    lsSub = soup.findAll('a') # find all links
    lsSub.pop() # get rid of unwanted last link


    # gets the last part of the url we'll use
    targetCounter = 0
    for x in lsSub:
        targetCounter += 1
        if targetCounter < 10:
            targetCountString = '0' + str(targetCounter)
        else:
            targetCountString = str(targetCounter)
        target.append(url + targetCountString)  # The target / final url 

# the site has weird formatting for the apartment section, this fixes it
aptCount = 1  
for url in target:
    if ('https://www.eslfast.com/robot/topics/apartment/' in url and aptCount < 10 ):
        aptStr = '0' + str(aptCount)
        replacement = '/apartment/1apartment' + aptStr
        rep = re.sub(r'/apartment/apartment\d+', replacement, url)
        idx = target.index(url)
        target.remove(url)
        target.insert(idx, rep)
        aptCount += 1
    elif('https://www.eslfast.com/robot/topics/apartment/' in url and aptCount == 10 ):
        aptStr = str(aptCount)
        replacement = '/apartment/1apartment' + aptStr
        rep = re.sub(r'/apartment/apartment\d+', replacement, url)
        idx = target.index(url)
        target.remove(url)
        target.insert(idx, rep)
        aptCount += 1
    elif ('https://www.eslfast.com/robot/topics/apartment/' in url and aptCount >= 11 ):
        if (aptCount < 20):
            aptStr ='0' + str(aptCount - 10)
        else:
            aptStr = str(aptCount - 10)
        replacement = '/apartment/2apartment' + aptStr
        rep = re.sub(r'/apartment/apartment\d+', replacement, url)
        idx = target.index(url)
        target.remove(url)
        target.insert(idx, rep)
        aptCount += 1

# # writes all the target urls to an output file
# with open('siteList.txt', 'w+') as file:
#     for x in target:
#         file.write(x +'\n')
 

# print raw html to dump.txt
dump = os.path.dirname(__file__) + '/dump.txt'
with io.open(dump, 'w+',encoding='utf-8') as outfile:
    for url in target:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        ls = soup.findAll('td')
        output = str(ls)
        outfile.write(output)
        time.sleep(1) # So I don't DoS or get kicked off the website

# read each line from dump.txt
with io.open(dump, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# filter the data and write it to ESL conversation.txt
convo = os.path.dirname(__file__) + '/ESL conversatison.txt'
with io.open(convo, 'w+', encoding='utf-8') as file:
    for line in lines:
        if '<b>' in line:
            file.write(line[9:-11] +'\n')


# # remove blank lines from .txt
# message = os.path.dirname(__file__) + "/messageGenData.txt"
# for line in fileinput.FileInput(message,inplace=1):
#     if line.rstrip():
#         print (line, end ='')

    
        
        
    




#######################################################################

# url = 'https://www.eslfast.com/robot/topics/smalltalk/smalltalk'
# response = requests.get(url)
# #print(response)

# soup = BeautifulSoup(response.text, 'html.parser')

# ls = soup.findAll('a')
# ls.pop()     # removes the bad link at the end
# links = []
# for x in ls:
#     links.append(url + '/' + x['href'])
# for x in links:
#     print (x) 

# for targeturl in links:
#     print(targeturl)


###########################################################################
# ls = ['https://www.eslfast.com/robot/topics/smalltalk/smalltalk01.htm']
# for x in ls:
#     url = 'https://www.eslfast.com/robot/topics/smalltalk/smalltalk01.htm'
#     print(url)
#     response = requests.get(url)
#     print(response)

# soup = BeautifulSoup(response.text, 'html.parser')

# ls = soup.findAll('td')
# #ls.pop()     # removes the bad link at the end
# for x in ls:
#     print (x)
# # links = []