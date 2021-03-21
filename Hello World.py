"""
################# IF ###################

height = input('Write a height to figure out whether you can ride or not')
if int(height) < 1:
    print("you re not allowed to ride")
elif int(height) >2:
    print("youre not allowed to ride")
else:
    print("youre allowed to ride")

################### IF chained, nested ###########################

x = 2
y = 3

if x == y or x + y == 5:
    print('ran')
else:
    print("did not run")

###############################################


x = 2
y = 3

if x == 2:
    if y == 3:
        print('ran')
else:
    print("did not run")

###################### FOR #########################


for x in range (0,10,1): #start, stop, step
    print(x, end="")

###################### WHILE #########################


loop = True
while loop:
    name = input('insert something: ')
    if name == 'stop':
        loop = False
    if loop == False:
        break
###################### Practice password #########################

import time


i = True
while i:
    pw = "Password123"
    if input('Password: ') == str(pw):
        print('logged in')
    else:
        print('you have 2 trials left')
        if input('Password: ') == str(pw):
            print('logged in')
        else:
            print('you have 1 trials left')
            if input('Password: ') == str(pw):
                print('logged in')
            else:
                print('wait 10s and try again')
                time.sleep(10)

###################### LISTS AND TUPLES #########################


#List

fruits =['apple', 'pear', 3]
print(fruits[1])
fruits.append('banana')
print(fruits)
fruits.append('bluberry')
print(fruits)

fruits[1] = 'ananas'
print(fruits)

#tuple

position=(2,3)
color=(255,255,255)
print(type(color))


###################### ITERATION BY ITEM #########################



fruits = ['apple', 'pear', 'ananas']

for fruit in fruits:
    if fruit == 'pear':
        print(fruit)
    else:
        print('not pears')

for x in range(len(fruits)):
    if fruits[x] == 'pear':
        print(fruits[x])
    else:
        print('not a pear')

for x in range(0, 10):
    print(x, end="-")

###################### STRING METHODS #########################


# .strip(), len(), .lower(), .upper(), .split()

text = input('Input something: ')

print(text)
print(text.strip())  #does not work, but this method removes whitespaces from string
print(len(text))
print(text.lower())
print(text.upper())
print(text.split())   # creates a list from the input ---  splitter you can add delimiter


###################### SLICE OPERATORS #########################


#slice operator
fruits = ['apples', 'pear', 'strawberrys']
text = 'Hello I like pyhton'

#  print(text[start:stop:step])

print(text[1:len(text):2])
#el  iepho

fruits.append('blueberries')
fruits[3:3] = 'hisisa'
print(fruits)

###################### FUNCTIONS #########################


def addTwo(x):
    return x + 2

def subtractTwo(x):
    return x - 2

def squared(x):
    return x**4

newNumber=7
print(addTwo(newNumber))
print(subtractTwo(newNumber))
print(squared(newNumber))

def printString(string):
    print(string)

printString('Hello')
printString('My name is Gabor')

def accel(mass, force):
    a = mass*force
    return a

printString(accel(2,5))

def doSomething():
    print('hi')

doSomething()

###################### READING A TEXT FILE #########################

file = open('readable_v2.txt', 'r')
g = file.read()
file = open('readable_v2.txt', 'r')
f = file.readlines()
print(g)
print(f)

newList = []
for line in f:
    if line[-1] == '\n':
        newList.append(line[:-1])
    else:
        newList.append(line)
print(newList)

#the upper and lower cycles are the same

newList2 = []
for line in f:
    newList2.append(line.strip())
print(newList2)

###################### WRITING TO A TEXT FILE #########################

"""
