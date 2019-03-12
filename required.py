import os
import sys
from urllib.request import urlopen
import subprocess
import glob


directory_path = '/Users/vanessalatefapampilo/Desktop/4thSemPython/Mandatory1/*/'
readMeList = []


def getAllReadMeFiles(someList):
    for filename in glob.glob( directory_path +'README.md'):
        with open(filename) as f:
            for line in f:
                if line.startswith('## Required reading'):
                    readMeList.append(next(f, '').strip())
                    while next(f, '') != '\n':
                        readMeList.append(next(f, '').strip())
  
    #To do : sort the list
    someList.sort()
    # To do : check for duplications
    someList = list(dict.fromkeys(someList))
    
    with open ('required_reading.md', 'w') as r:
        for i in someList:
            if i != '':
                r.writelines('%s \n' %i)
        r.close()        
    
#TO DO : push the 
#create a new directory, create the file.md
#then do the os cmd push to git

getAllReadMeFiles(readMeList)



sys.exit()

clone_urls = []
lesson_number = [1,2,3,4,5,6,7,8,9]
find_string = '"clone_url"'



def saveInfoToDict():
    with open('new_api.txt') as file:
        for lineNumber, line in enumerate(file,1):
            if find_string in line :
                slice(line)
                clone_urls.append(line[13:-2])

    clone_dictionary = dict(zip(lesson_number, clone_urls))
    print(clone_dictionary)    
    return clone_dictionary

clone_dictionary = saveInfoToDict()   
       

def slice(val,start=1,stop=None):
    return val[start:stop]

def is_git_directory(path = "."):
    iscloned = os.popen('git clone ' + path)
    print(iscloned.read())
    #TO DO : if git already exist, then git pull use os.chdir



#cloneRepo function, takes in a user input and matches at a lesson number == keys in the clone dictionary
#when matched it will clone
#TO DO : still need to catch some errors
#TO DO: when repository already exist, pull the latest version

while True:
    try:
        user_input = int(input("Please enter lesson number : "))

    except ValueError as err:
        print("Sorry, you must enter a number", err)
        continue
    if user_input in clone_dictionary :
        print("cloning lesson : ", user_input)
        #matched with value
        print("cloning success with :", clone_dictionary[user_input])
        gitPath = clone_dictionary[user_input]
        is_git_directory(gitPath)
        break
    else:
        print("git pull should be done here")
        print("pulling up to date repository", user_input)


sys.exit()


def getAllInfoFromApi():
    res = urlopen('https://api.github.com/orgs/python-elective-1-spring-2019/repos?per_page=100')
    with open('api.txt', 'w+') as f : 
        api = res.read().decode('utf-8')
        f.write(api)

        new_api = str(api).split(",")

        new_api = "\n".join(["".join(new_api[i:i+1]) for i in range(0,len(new_api))])
            # join into chunks of 1 and add a newline to separate the output
        with open('new_api.txt', 'w+') as n : 
            n.write(new_api)

getAllInfoFromApi()
    

sys.exit()

