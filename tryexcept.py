import json


try:
    print(5/0)
except ZeroDivisionError:
    print("dumb")
else:
    print("all right")
    
with open('jim.txt', 'r') as file_object:
    contents = file_object.read()
words = contents.split()
print(len(words))


numbers = [1, 2, 3, 4]
file_name = 'numbers.json'
with open(file_name, 'w') as f_obj:
    json.dump(numbers, f_obj)

with open(file_name, 'r') as f_obj:
    print(json.load(f_obj))