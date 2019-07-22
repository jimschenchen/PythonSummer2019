str1 = "jim "
'''
name: rstrip()
fun: remove the space in the str
'''
print(str1 + str1.rstrip())

#-1 is the last element of a list
list1 = ["1", "2", "3"]
print(list1[-1])


list2 = [1, 2, 3, 4]
print(list2)
list2[0] = 0
print(list2)
list2.append(5)
print(list2)
list2.insert(1, 1)
print(list2)

del list2[5]
print(list2)


print(list2.pop(2))
print(list2)

#remove del the first specific value
list2.remove(1)
print(list2)

#sort
list3 = ["a", "c", "b", "g", "e"]
list3.sort()
print(list3)
list3.sort(reverse = True)
print(list3)
print(sorted(list3))
list3.insert(1, "a")
print(list3)
print(sorted(list3, reverse = True))

#just reverse
list3.reverse()
print(list3)
print(len(list3))

for i in list3:
    print(i)

for i in range(0, 7):
    print(i, end = "")

print()    
#quick create number list
numbers = list(range(0, 9, 2))
#0 2 4 6 8
print(max(numbers))
print(sum(numbers))

#这叫解析？？？ List Comprehensive
cubed = [value**3 for value in range(1, 11)]
print(cubed)

#切片
#index 1 - 3
print(cubed[1:4])

#遍历切片
for value in cubed[:4]:
    print(value)

#assign value
newlist = cubed[:]
#newlist = list(cubed)
print(newlist)


#元组 tuple 不能给元素赋值 但是可以给整体变量赋值
size = (1 , 100)
print(size)
size = (2, 200)
print(size[1])

#list determine specific value
print(0 in cubed)
#return False
print(0 not in cubed)
#return True

toppings = []
print(toppings)
if toppings:
    print("1")
else:
    print("0")
#list is empty determing False in if statement