import sys
import os
from _io import open
from ctypes.test.test_pickling import name
from turtledemo.nim import SCREENHEIGHT
from test.test_winsound import sound_func
from pip.utils.filesystem import check_path_owner
#from test.test_zipimport import module_path_to_dotted_name
#from curses.ascii import isalnum

print("hello world")
#comment

'''
multiline comment
'''

name = "Victor"
print(name)

name = 15

print ("5+2=", 5+2)
print ("5-2=", 5-2)
print ("5*2=", 5*2)
print ("5/2=", 5/2)
print ("5%2=", 5%2)
print ("5**2=", 5**2)
print ("5//2=", 5//2)

print("1+2-3*2=", 1+2-3*2)
print("(1+2-3)*2=",(1+2-3)*2) 

quote = "\"Always remember you are unique"

multi_line_quote = ''' just 
like everyone else'''

new_string = quote + multi_line_quote

print("%s %s %s" %('I like the quote', quote, multi_line_quote))
print ('\n' * 3)
print("I don't like ", end="")
print ("newlines")

grocery_list = ['juice','Tomatoes', 'Potatoes' 'bananas']

print('First Item', grocery_list[0])
grocery_list[0] = "Green Juice"
print(grocery_list[1:3])
other_events = ['Wash car', 'Pick up kids', 'cash check']
to_do_list = [other_events, grocery_list]
print(to_do_list)
print ((to_do_list[1][1]))
grocery_list.append('Onions')
print(to_do_list)

grocery_list.insert(1,"Pickle")
grocery_list.remove("Pickle")
grocery_list.sort()
del grocery_list[1]
print (to_do_list)


to_do_list2 = other_events + grocery_list

print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))

#trubles
pi_tuple=(3,1,4,1,5,9)
new_tuple = list(pi_tuple)
new_list = tuple(new_tuple)
len(pi_tuple)
min(pi_tuple)
max(pi_tuple)

#dictionary

super_villains= {'Fiddler':'Isaac Bowin',
                'Caption Cold': 'Leonard Snart',
                'Weather Wizard':'Mark Mardon',
                'Mirror Master':'Sam Scudder',
                'Pied Piper':'Thomas Peterson'}

print (super_villains['Caption Cold'])
del   (super_villains['Fiddler'])
super_villains['Pied Piper'] = 'Hartley Rathaway'
print(len(super_villains))
print(super_villains.get("Pied Piper"))
print(super_villains.keys())

#conditionals
age = 21
if age > 16 :
    print('You are old enough to drive')
else:
    print('You are NOT old enough to drive')

if age >= 21:
    print('You are old enough to drink')  
elif age >= 16:
    print('You are old enough to drive a car') 
else:
    print('You are not old enough to drive')
     
if((age >= 1)and(age<=18)):
    print("You get a birthday party ")
elif (age == 21) or (age >= 65):
    print("You get a birthday")
elif not(age == 30):
    print("You don't get a birthday party")
else:
    print("You get a birthday party, yeah!")

#looping
for x in range(0,10):
    print(x,'',end="")    
print('\n')   

grocery_list = ['juice','Tomatoes', 'Potatoes' 'bananas']

for y in grocery_list:
    print(y)
for x in [2,4,6,8,10]:
    print(x)    
num_list = [[1,2,3],[10,20,30],[100,200,300]]

for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])

random_num = random.randrange(0,100)

while(random_num != 15):
    print(random_num)
    random_num = random.randrange(0,100)
    
i=0;
while(i <= 20):
    if(i%2 ==0):
        print(i)
    elif(i == 9):
        break
    else: 
        i += 1 #i = i + 1
        continue
    i += 1

#functions
def addnumber(fNum,lNum):
    sumNum = fNum+lNum    
    return sumNum

print(addnumber(1,4))
    
#print("What is your name?")
#name = sys.stdin.readline()
#print("Hello",name)

long_string = "I'll catch you if you fall -Floor"
print(long_string[0:5])
print(long_string[-5:])
print(long_string[:-5])
print(long_string[:4] + " be there")
print("%c is my %s letter and my number %d number is %.5f " 
      %('X', 'Fav', 1, 1.4))
print(long_string.capitalize())
print(long_string.find("Floor"))
print(long_string.isalnum())
print(len(long_string))
print(long_string.replace("Floor","Ground"))
print(long_string.strip())
quote_list = long_string.split()
print(quote_list)

#file i/o
test_file = open("test.txt","wb")
print(test_file.mode)
print(test_file.name)
test_file.write(bytes("Write me to the file \n", 'UTF-8'))
test_file.close()

test_file = open("test.txt", "r+")

text_in_file = test_file.read()
print(text_in_file)
#text_in_file.close()
#os.remove("test.txt")

#objects

class Animal:
    __name  = None
    __height= 0
    __weight= 0
    __sound = None
    
    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height 
        self.__weight = weight
        self.__sound  = sound
        
        
    
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name 
    
    def set_height(self, height):
        self.__height = height
    def get_height(self):
        return self.__height 
    
    def set_weight(self, weight):
        self.__weight = weight
    def get_weight(self):
        return self.__weight 
    
    def set_sound(self, sound):
        self.__sound = sound
    def get_sound(self):
        return self.__sound 
    
    def get_type(self):
        print("Animal")
        
    def toString(self):
        return "{} is {} cm tall and {} kilograms and say {}".format(self.__name,
                                                                     self.__height,
                                                                     self.__weight,
                                                                     self.__sound)
        
        
        
cat = Animal('Whiskers',33,10,"Meow")
print(cat.toString())

class Dog(Animal):  
    __owner = None
    
    def __init__(self, name, height, weight, sound, owner): 
        self.__owner = owner
        self.__animal_type = None
        super(Dog, self).__init__(name, height, weight, sound)
        
    def set_owner(self, owner): 
        self.__owner = owner 
    def get_owner(self):
        return self.__owner
    
    def get_type(self):
        print("Dog")
  
    def toString(self):
        return "{} is {} cm tall and {} kilograms and say {} His owner is {}".format(self.__name,
                                                                                     self.__height,
                                                                                     self.__weight,
                                                                                     self.__sound,
                                                                                     self.__owner)
        
    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound()*how_many)
            
spot = Dog("Spot", 53, 27, "Ruff", "Derek")
mia = Dog("Mia", 13, 8,"Ruff", 'Victor')
chewbie = Dog("Chewbie aka Chewbaqiya aka Chewbias", 6, 3,"Ruff","Monica")
#print(spot.toString())


class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()
        
test_animals = AnimalTesting()

test_animals.get_type(cat)
test_animals.get_type(spot)

spot.multiple_sounds(4)
spot.multiple_sounds()
print(spot.toString())
    




        
        
        
        
        
        
        













