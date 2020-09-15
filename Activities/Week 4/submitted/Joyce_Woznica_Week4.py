# Week 4
# Week 4 Activities - Functions
# Author: Joyce Woznica
# Class: IST 652
# 

# write Fibonacci series up to n
def fib(n):
    ## Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print (a, end = " ")
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)

# Return a list containing the Fibonacci series up to n."""
def fib2(n):  # return Fibonacci series up to n
     result = []
     a, b = 0, 1
     while a < n:
         result.append(a)    # see below
         a, b = b, a+b
     return result

f100 = fib2(100)    # call it
f100                # write the result

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
        
i = 5

def f(arg=i):
    print(arg)

i = 6
f()

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument

def function(a):
    pass
function(0, a=0)
# produces error

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
        
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


# 4.2 Activity
def fred():
    print ("Zap")

def jane():
    print ("ABC")

jane()
fred()
jane()


def computepay(hours, rate):
    if float(hours) > 40:
        pay = 40*(float(rate)) + (float(hours)-40)*(1.5*float(rate)) 
    else:
        pay = float(hours)*float(rate)
    print("Pay: $" + str(pay))

# run function
hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
computepay(hours, rate)

# define function
def nums():
    count = 0
    total = 0
    avg = 0
    while True:
        inp = input('Enter a number:')
        if inp == 'done':
            break
        try:
            total = total + float(inp) 
            count = count + 1
        except ValueError:
            print('You must enter a number.')
    avg = total / count
    return count, total, avg

# run the function
cc, tt, a = nums()  

print("Total Numbers Entered: ", str(cc))        
print("Sum of all Numbers Entered: ", str(tt))
print("Average of Numbers Entered: {:.2f}".format(a))

import numpy as np
a = np.array([1,2,3])
b = np.array([[1,2,3],[4,5,6]])

arrJ = np.array([[1,2,3,4,5], 
                 [6,7,8,9,10], 
                 [11,12,13,14,15], 
                 [16,17,18,19,20]])
arrJ
arrJ.shape

# Use Index Slicing and show how to get the 
# subarray consisting of the last two rows and the third and fourth columns.
# so would want [13,14] and [18.19]

# gives us row 3 and 4 is actually 
subJ = arrJ[2:]
# gives us 3rd column
subJ2 = arrJ[:,[2]]
# gives us 4th column
subJ3 = arrJ[:,[3]]
# final 2 x 2
finarrJ = arrJ[2:4, 2:4]
finarrJ
finarrJ.shape

# one dimensional array of the sums of the columns
sumarrJ = np.sum(arrJ, axis=0)
sumarrJ
