with open('pi_digit.txt') as file_object:
    #contents = file_object.read()
    #���read������������file_object���������
    for line in file_object:
        print(line.rstrip())
    #print(contents)
    
    lines = file_object.readlines()
    for i in lines:
        print(i)
    #֮ǰ��ȡ���Ժ� ֮��Ķ��ǿյ�
    #����Ӧ�����Ϊ¼ȡ������

#with �����ж�ʲôʱ��close����

file_path = r'C:\Users\jimsc\OneDrive\����\PythonSummer2019\jim.txt'
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
    
    
    
    