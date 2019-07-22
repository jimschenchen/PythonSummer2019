dir1 = {'color' : 'blue', 'avalue' : 1, "time" : 1}
print(dir1)
dir1['un'] = 'jim'
print(dir1)

del dir1['un']
print(dir1)

for key, value in dir1.items():
    print(key + ": " + str(value))
    
#default£º
for key in dir1.values():
    print(key)
for key in dir1.keys():
    print(key)
for key in dir1:
    print(key)  
    
print("\n", sorted(dir1))

#set del the repeated value
for value in set(dir1.values()):
    print(value)
    

aliens = []

for alien_number in range(30):
    aliens.append(
        {'color' : 'green', 'point' : 5, 'number' : alien_number + 1}
    )
    
for alien in aliens[:30]:
    print(alien)
    
print(len(aliens))
print(alien_number)


msg = input("what's your name?\n\t")
print(msg)

active = True
while active:
    if input("msg") == 'quit':
        active = False
        
