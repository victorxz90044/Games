'''
def revrot(strng,sz):
    if strng == "":
        print("")
    elif sz%2==0:
        strng[::-1]
        print(strng)
    else:
        print(strng[-1:] + strng[:-1])




revrot("1234", 1)
revrot("", 0)#, "")
revrot("12346789", 6)#, "")
s = "733049910872815764"
revrot(s, 5)#, "330479108928157"

array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print(array)
print(array[1::2])
print(array[::-2])
print(array[9:])
print(array[7:9])
print(array[0:10:2])
print(array[-2:])
print(array[:-2])
'''
  

'''
def remove_every_other(my_list):
    for item in range(len(my_list)):
        if item%2==0:
            print(my_list[item])
        else:
            pass
    

remove_every_other(['one','two','three','four','five','six','seven','eight','nine','ten'])
remove_every_other((['Hello', 'Goodbye', 'Hello Again']),(['Hello', 'Hello Again']))
remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 5, 7, 9][[1, 2]], [[1, 2]] [['Goodbye'], {'Great': 'Job'}],[['Goodbye']])


try:
    with open('man_data.txt','w') as man_file:
        print (man, file=man_file)
    with open('other_data.txt','w') as other_file:
        print(other,file=other_file)
except IOError as err:
    print("File Error:"+ str(err))
    
         
'''
'''
def namelist(names):
    x=0
    while x < len(names):
        print(names[x].get('name'))
        
        x=x+1
        

for name in names:
        print( "key: %s , value: %s" % (key, name[key]))

namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}])#, 'Bart, Lisa, Maggie, Homer & Marge',"Must work with many names")
namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}])#, 'Bart, Lisa & Maggie',"Must work with many names")
namelist([{'name': 'Bart'},{'name': 'Lisa'}]) #, 'Bart & Lisa',"Must work with two names")
namelist([{'name': 'Bart'}])#, 'Bart', "Wrong output for a single name")
#namelist([])#, '', "Must work with no names")

'''

'''
writeMe= 'Example Text'
saveFile = open('exampleFile.txt','w')
saveFile.write(writeMe)
saveFile.close()

appendMe= 'Example Text2'
saveFile = open('exampleFile.txt','a')
saveFile.write(appendMe)
saveFile.close()

readMe = open('exampleFile.txt','r')
print(readMe)
splitMe = readMe.split('\n')
print(splitMe[])
'''
'''
class calc:
    def add(x,y):
        answer = x+y
        return answer
    def sub(x,y):
        answer = x-y
        return answer

name = input("Pull up!: ")
print('Sup',name)

import statistics as stat

exList=[7,5,8,5,4,45,54,12,65,984,65,321,5,12,6,8,9,19,6,4,5,45,32,15,35,25,85,74]
x= stat.mean(exList)
print(x)
x= stat.stdev(exList)
print(x)
x= stat._sum(exList)
print(x)
x= stat.variance(exList)
print(x)
x= stat.median(exList)
print(x)
x= stat.harmonic_mean(exList)
print(x)

'''

#enumerate
name =['Corey','Bill','Timmy','Billy','Jack','John','Sue']
for index, name in enumerate(name, start=1):
    print(index,name)



#looping over two list
names = ['Peter Parker','Clark Kent','Wade Wilson','Bruce Wayne']
heroes =['Spiderman', 'Superman', 'Deadpool','Batman']
universes=['Marvel','DC','Marvel','DC']

for names, hero, universes in zip(names,heroes, universes):
    print(f'{names} is actually {hero} from {universes}')


# unpacking values

a,b,*c, d = (1,2,3,4,5,6,7)

print(a)
print(b)
print(c)
print(d)


#Getpass
from getpass import getpass

username= input("Username: ")
password= getpass("Password")



