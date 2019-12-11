lower = []
with open('last-names.txt', 'r',) as f:
    for line in f:
        lower.append(line.rstrip().lower())

print(lower[:10])

proper = []
for x in lower:
   proper.append(x.capitalize())

print(proper[:10])

with open('lastNames.txt', 'w+') as g:
    for line in proper:
        g.write(line + '\n')