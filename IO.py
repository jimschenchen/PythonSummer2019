with open('pi_digit.txt') as file_object:
    #contents = file_object.read()
    #这个read（）会消除掉file_object里面的内容
    for line in file_object:
        print(line.rstrip())
    #print(contents)
    
    lines = file_object.readlines()
    for i in lines:
        print(i)
    #之前读取了以后 之后的都是空的
    #所以应该理解为录取并消除

#with 帮助判定什么时候close（）

file_path = r'C:\Users\jimsc\OneDrive\桌面\PythonSummer2019\jim.txt'
print(file_path)
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())
   
''' 
pi = '124215321241511'
birthday = '511'
if birthday in pi:
    print(1)
else:
    print(0)

print(birthday in pi)
'''

with open('jim.txt', 'w') as file_object:
    file_object.write("yeah")
    
    
    
    