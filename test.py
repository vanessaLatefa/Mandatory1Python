import sys
from urllib.request import urlopen
from itertools import islice
from collections import Counter


""" def counters(fname):
    with open('api.txt') as f:
        return Counter(f.read().split())

print(counters('api.txt'))



#prints the file size of a plain file ( 68122)
statinfo = os.stat('api.txt')
print(statinfo.st_size)

 ifile = sys.argv[1]
ofile = sys.argv[2]

with open(ifile) as ifile , open(ofile, "w") as ofile:
        clones = ifile.readline().split(",")
        for n, clones in enumerate(clones):
            urls, clones = clones.split('""')
            clones = '",' + clones
            if len(urls) > 1:
                urls = urls.strip()
                urls = '"{}"'.format(urls)
                clones = "".join(urls + clones)
            if n < len(clones) -1:
                ofile.write(clones.strip() + ",\n")
            else:
                ofile.write(clones.strip() + "\n")
                       


  
 """
sys.exit()
l=[]
n = 1
def longes (filename):
    with open(filename,'r') as fiii:
        words = fiii.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len ]
print(longes('api.txt'))




for i in range(6):
    if (i == 3 or i == 6):
        continue
    print(i, end=' ')



datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

for i in datalist:
    print('Type of ', i , 'is\t\t\t' ,type(i))


numbers = (1,2,3,4,5,6,7,8,9,12,13,14,15,23,24,26)

for i in numbers:
    if not i % 2:
        print('This are evens : ',i)
    else:
        print('This are odds : ', i)



inp = input("Please enter a word : \n")

result = ''.join(reversed(inp)) #inp[::-1]
print(result)



# Method for showing numbers that are divisible by 7 and multiple of 5
#between 1500-2700
nl=[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))


#
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for number in numbers:
    if number == 237:
        break

    if number % 2 == 1:
        continue

    print(number)



sys.exit()
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your curretn balance is $%s"

print(format_string % data)

sys.exit()

x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = [x,y] * 10

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

sys.exit()

squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)
rem = 11 % 3
print(rem)

sys.exit()

numbers = [1,2,3]
strings = ["hello", "world"]
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = "Eric"


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)