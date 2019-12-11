#!/usr/bin/python
from timeit import default_timer as timer
import markovify
import os
import io
import json
import argparse

# Comment this out to remove command line argument requirement
#########################################################################
parser = argparse.ArgumentParser(description='Generate random messages.')
parser.add_argument('NUM', metavar='<number of messages>', type=int, nargs=1,
                help='the number of messages to generate')
args = parser.parse_args()
NUM = int(args.NUM[0])
#########################################################################


# NUM = 1000 ## Use this if you commented out the command line section

# Get raw text as string.
infile = os.path.dirname(__file__) + '/ESL conversatison.txt'
with io.open(infile, 'r', encoding='utf-8') as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)


# Fill a list with generated sentences
data = []
start = timer()
for i in range(NUM):
    message = text_model.make_sentence()
    data.append({
        'message' + str(i): message
        })

# Write the list to a json file
messages = os.path.dirname(__file__) + '/messages.json'
with io.open(messages, 'w+', encoding='utf-8') as f:
    json.dump(data, f)# , indent=4) 
        # indent=4 gives the file pretty formatting but uses many more lines

stop = timer()
time = stop - start
print(time)
input()