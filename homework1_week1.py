#------------------------------------------------
# Homework 1 of course "Python for Research"
# HarvardX -  PH526xEdX, EdX
#-----------------------------------------------

#Exercise 1a--------------------------------------
import string
alphabet=string.ascii_letters
alphabet

#Exercise 1b--------------------------------------
sentence = 'Jim quickly realized that the beautiful gowns are expensive'
count_letters = {}

for i in range(len(alphabet)-1): #loops through the letters
    if sentence.count(alphabet[i])>0:
        count_letters[alphabet[i]] = sentence.count(alphabet[i])


#Exercise 1c--------------------------------------
def counter(input_string):
    import string
    alphabet=string.ascii_letters
    count_letters = {}
    for i in range(len(alphabet)-1): #loops through the letters
        if input_string.count(alphabet[i])>0:
            count_letters[alphabet[i]] = input_string.count(alphabet[i])
    return(count_letters)

counter(sentence)

#Exercise 1d--------------------------------------
address_count=counter(sentence)
print(address_count)

#Exercise 1d--------------------------------------

inverse = [(value, key) for key, value in address_count.items()]
most_frequent_letter=max(inverse)[1]
print(most_frequent_letter)

#Exercise 2a-------------------------------------
import math
print(math.pi/4)

#Exercise 2b-------------------------------------
import random
random.seed(1)
def rand():
    return(random.uniform(-1,1))
rand()

#Exercise 2c-------------------------------------
import math
def distance(x, y):#x and y are tuples
   # define your func
   dif= (x[0] - y[0], x[1] - y[1])
   squared=dif[0]**2+dif[1]**2
   return(math.sqrt(squared))
x=(0,0)
y=(1,1)
print(distance(x,y))

#Exercise 2d-------------------------------------
import random, math
random.seed(1)

def in_circle(x, origin):
   return(distance(x,origin)<1)

print(in_circle((1,1),(0,0)))

#Exercise 2e-------------------------------------
R = 10000
x = []
inside = []
for i in range(R):
    point = [rand(), rand()]
    x.append(point)
    inside.append(in_circle(point, (0,0)))
print(sum(inside) / R)

#Exercise 2f-------------------------------------

import math

print(sum(inside)/R-math.pi/4)

#Excercise 3a-------------------------------------
import random
random.seed(1)

def moving_window_average(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors*2 + 1 #size of window
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors #enlarging x for the boundaries
    # To complete the function,
    # return a list of the mean of values from i to i+width for all values i from 0 to n-1.
    x_moving_average=[]
    window=[]
    for i in range(n_neighbors,len(x)-n_neighbors):
        #define window
        window=x[i-n_neighbors:i+n_neighbors+1]
        x_moving_average.append(float(sum(window)) / max(len(window), 1))
    return(x_moving_average)

#Excercise 3b-------------------------------------
import random

random.seed(1)
R = 1000
x = []
Y = [[] for x in range(0,10)] #list of lists
for i in range(R):
    x.append(random.uniform(0,1))
Y[0]=x

for n_neighbors in range(1,10):
    Y[n_neighbors]=moving_window_average(x, n_neighbors)

#Excercise 3c-------------------------------------

ranges=[]
for n  in range(0,10):
    #minima.append(min(Y[n]))
    #maxima.append(max(Y[n]))
    ranges.append(max(Y[n])-min(Y[n]))
print(ranges)
