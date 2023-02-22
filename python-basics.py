# birthYear = input('Birthyear: ')
# print(type(birthYear))
# age = 2023 - int(birthYear)

# conversions

# int()
# float()
# bool()
# print(age)


string = '''
Hello there,
This is a test 
for mult lines on chart
'''
#  ###### String Methods #####
#  .upper() - .find() - .endswith() - .index() - .replace(x, y)
# print(string[1]) output: H
# string[:6] output Hello
# print(string[0:6]) 
# print('chart' in string)  output: true
# print(len(string))
copy = string[:]

# Formatted string
# print(f'This is a copy: {copy}')


# ###### Arithmatic operator #########
# - + / *
#  // convert float to string 
#  % returns remainder
#  5 ** 2  returns 25
# round(number)
# abd(-2.9) returns +

work = False
is_hot = True
is_cold = True
is_snowing = False

if is_hot and not work: 
    print("Learning")
elif is_cold or is_snowing:
    print("Pack a jacket")
else:
    print("Have a nice day")
    
# condition operators 
# aissignment : =
# comparisson : ==
# not euqal : !=


#  whiile loop 

i = 1
while i <= 5:
    # print(i)
    i += 1
    if i == 3:
        # print("Max cap hit.")
        break
    

clothingItems = [10,20,15]

total = 0

for item in clothingItems:
    total += item
# print(f'Total: ${total}')    

# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# print(matrix[1][1]) : output 5

# Arrays 
#  add to end    add num to space     remove item     empty list      remove last    count instances
# .append() -   .inset(slot, num)  -  .remove()    -   .clear()   -   .pop()     -     .count()        
# 
# 
#  .sort()    .reverse()     .copy()


# Tuple : cannot edit 
# num = (1,2,3,4)

# key value pair / object

customer = {
    "name": "John Smith",
    "age": 30,
    "is_online": True
}

customer['name'] = "Chris Jimenez"
customer['is_verified'] = True

# print(customer.get("name"))
# print(customer['is_verified'])


# let user type message
# message = input(">")

# functions 
# functions return none by default 
def power_of_two(num):
    return num * num


# number 3 is a postional arguement
result = power_of_two(3)
# print(result)


def get_receipt(total, shipping, discount):
    print(f'Discount: {discount}')
    print(f'Total: {total}')
    print(f'Shipping: {shipping}')

# keyword arguements 
# get_receipt(total=50, shipping=5, discount=0)

# try:
#     age = int(input("Age: "))
#     print(age)
# except ValueError:
#     print('Invalid Value')
    


class Point:
    def __init__(self, name):
        self.name = name
    
    
    def greet(self):
        print(f'Hi my name is {self.name}')
    

class Teacher(Point):
    def job(self):
        print(f'Hello class my name is {self.name}, I am you new teacher')

person = Point('Chris')
# person.greet()

Jimenez = Teacher("Mr.Jimenez")
# Jimenez.greet()


# ######## Modules ###########

import modulesFile

modulesFile.talk()
