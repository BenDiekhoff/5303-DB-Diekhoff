# RandomDataGenerator
Generates random user data (ideally 1000+ users) in a csv or json file.  
Run ```dataGenDiekhoff.py <file type> <number of users to generate>```  
from the command line, where `<file type>` is either 'csv' or 'json'  

# This repo is part of a school assignment!
The standalone repo can be found ![here](https://github.com/BenDiekhoff/RandomDataGenerator)

# Mac or Linux users
remove `, newline= ''` from line 36 in dataGenDiekhoff.py.  
This prevents Windows from inserting a blank line between entries.

# Data
- user_id
- email
- username
- first_name
- last_name
- password
- create_time
- last_update
- ages (the distribution can be adjusted in generate.py)

# Originally forked from
https://github.com/williexu/random_username

# Uses lists from:
- https://github.com/williexu/random_username
- https://github.com/dominictarr/random-name
- https://github.com/arineng/arincli/tree/master/lib
- https://gist.github.com/tbrianjones/5992856/
