# 1.    print(randInt()) 		    # should print a random integer between 0 to 100

import random
def randInt():
    print(int(random.random()*100))
randInt()

# 2.    print(randInt(max=50)) 	    # should print a random integer between 0 to 50

import random
def randInt2():
    print(int(random.random()*50))
randInt2()

# 3.    print(randInt(min=50)) 	    # should print a random integer between 50 to 100

import random
def randInt3():
    values = list(range(50,100))
    print(int(random.random(values))
randInt3()

# 4.    print(randInt(min=50, max=500))    # should print a random integer between 50 and 500

import random
def randInt4():
    values = list(range(50,500))
    print(random.choice(values))
randInt4()
