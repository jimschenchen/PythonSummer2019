#
def position(x, y = 0):
    '''
    '''
    print("x value is: " + str(x) + ", y value is: " + str(y) + ".")
    

#def position(x = 1, y) this is error coz non-default argument cannot follows default argument

position(1, 2)

#positional argument
position(x = 1, y = 2)

#keywords argument
position(y = 2, x = 1)

#position(1, 1)


def cube(x, y = 1, z = 2):
    print("" , x, y, z)
    

cube(x = 1, z = 3, y =2)
#stupid dumb ass


def sumnum(x, y):
    return x + y

print(sumnum(1, 2))


#assign the address
def printList(flist, slist):
    while flist:
        tlist = flist.pop()
        slist.append(tlist)     

flist = [1, 2, 3, 4]
slist = []

printList(flist, slist)
slist.sort(reverse = True)
print(flist, slist)

#*无论有多少个argument 都会讲arguments变成tuple
def make_pizza(*toppings):
    print(toppings)
    
make_pizza("1", "2", "4", 'dwawd')

#**双星号为字典
#不管怎么样 任意数量的实参
    