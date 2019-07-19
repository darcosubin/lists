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
def add(x,y):
    return x+y
print map(add,seq,seq) #no ideea

def sum(seq):
    def add(x,y): return x+y
    return reduce(add,seq,0)
print sum(range(1,11))  #Makes n*n+1/2 sum
print sum ([])