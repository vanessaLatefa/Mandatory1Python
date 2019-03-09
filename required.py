import os
import sys
from urllib.request import urlopen


clone = []
find_string = '"clone_url"'



with open('new_api.txt') as file:
    for lineNumber, line in enumerate(file,1):
        if find_string in line :
            print('Found it in line : ',lineNumber)
            slice(line)
            clone.append(line[12:-2])

print(clone)          


def slice(val,start=1,stop=None):
    return val[start:stop]

               
            


sys.exit()

res = urlopen('https://api.github.com/orgs/python-elective-1-spring-2019/repos?per_page=100')
with open('api.txt', 'w+') as f : 
    api = res.read().decode('utf-8')
    f.write(api)
    
    new_api = str(api).split(",")
    
    new_api = "\n".join(["".join(new_api[i:i+1]) for i in range(0,len(new_api))])
        # join into chunks of 1 and add a newline to separate the output
    with open('new_api.txt', 'w+') as n : 
        n.write(new_api)
    #TO do: Save the print into another file nln #DONEEEEEE!!!!
    #TO DO : Get all the clone_url from the file, save it on a list.

sys.exit()

