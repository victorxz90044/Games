class Person():
    pass

person = Person()

first_key = "first"
first_val= "Bob"

setattr(person, first_key, first_val)

first = getattr(person, first_key)

print(first)



person_info= {'first': 'Bob', 'last': 'Burger'}

for key, value in person_info.items():
    setattr(person, key, value)
    
for key in person_info.keys():
        print(getattr(person,key))




