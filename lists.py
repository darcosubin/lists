a=[66.25,333,333,1,1234.5]
print a.count(333), a.count(66.25), a.count('x') #it will count those elements between ()

a.insert(2, -1) #insert on 2nd position number -1
a.append(334)
print a

print "The position of number 33 is: ", a.index(333)
print "The position of number 1234.5 is: ", a.index(1234.5) #it will show the position of that element

a.reverse() #it will reverse the entire list
print a

a.remove(66.25) #it will remove that element
print a

a.sort() #it will sort the list
print a

print "The popped element is: ",a.pop() #it will get out the last element of that list
print a

print
print "-" *10,"THE STACKS", "-"*10
print
stack=[3,4,5]
print stack
stack.append(6)
stack.append(7)
stack.append(8)
print stack

stack.pop()
print stack
stack.pop()
print stack

print
print "-" *10,"QUEUES", "-"*10
print "-" *5,"First-in, First-out", "-"*5
print
from collections import deque
queue=deque(["First","Second","Third","Fourth"])
print "1", queue
queue.append("Fifth") #fifth arrives
print "Fifth arrives" 
print "2", queue
queue.append("Sixth"), #sixth arrives
print "Sixth arrives"
print "3", queue
print queue.popleft(), "goes away" #first to arrive now leaves
print "4", queue
print queue.popleft(), "goes away" #second to arrive now leaves
print "5", queue

print
print "-" *10,"FUNCTIONAL PROGRAMMING TOOLS", "-"*10
print

def f(x):
    return x%3==0 or x%5==0
print "Numbers divided by 3 or 5 between 2-50", filter(f,range(2,50)) #it will filter the elements

def cube(x):
    return x*x*x
print "Cubes of numbers between 1-30", map(cube, range(1,30))#it will give a map of the cubes between those elemnents

seq =range(8)
seqv=(range(2,24,3))
def add(x,y):
    return x+y
print map(add,seq,seqv) #it will make this 1st element from seq + 1st element of seqv and so on

def sum(seq):
    def add(x,y): return x+y
    return reduce(add,seq,0)
print sum(range(1,11))  #Makes n*n+1/2 sum
print sum ([])

print
print "-" *10,"LIST COMPREHENSIONS", "-"*10
print

squares=[]
for x in range(10):
    squares.append(x**2) #squares of the range of numbers
print "Squares are: ", squares
#square=[x**2 for x in range(10)]
#print square

print "Combs: ", [(x,y) for x in[1,2,3] for y in[3,1,4]if x!=y]

combs=[]
for x in[1,2,3]:
    for y in[3,1,4]:
        if x!=y:
            combs.append((x,y))
print "Combs: ", combs

from math import pi 
print "Pi rounded: ", [str(round(pi,i)) for i in range(1,6)] #it will give the round number

matrix=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]
print "Matrix: ", matrix

print "Transposed: ", [[row[i] for row in matrix] for i in range(4)]
transposed=[]
for i in range(4):
    transposed.append([row[i] for row in matrix])
print "Transposed: ", transposed

print "Transposed: ", zip(*matrix)

tel={'jack':4098,'sape':4139}
tel['guido']=4127
print tel