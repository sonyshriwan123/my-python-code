
# =======define of class===
# class Myclass:
#     x = 5
# print(Myclass)     #class name the memory location of the class
# print(Myclass.x)


# ===this is object creation in a class =============
# class anotherclass:
#     x = 5   #======== this is an attribute of the class
# p1 = anotherclass() # creating an object of the class
# print(p1.x)              # it will print the value of x which is 5

# class Person:
#     def __init__(self, name, age):   #this is a constructor which is used to initialize the attributes
#         self.name = name              #self refer to the current object of the class
#         self.age = age
# # #definding a method in the class
#     def myfunc(self):
#         print("Hello my name is " + self.name + " and I am " + str(self.age) + " years.old. ")
# p1 = Person("Ayush", 20)           # creating an object of the class and passing the value to the constructor
# # # del p1
# p1.myfunc()                            #calling the method of the class using the object


# ============08/04/2026
# class chai:
#     pass
# class chaitime:
#     pass


# print(type(chai))
# print(type(chaitime))

# ginger_tea = chai()
# ginger_tea1 = chaitime()
# del ginger_tea


# print(type(ginger_tea))
# print(type(ginger_tea) is chai)
# print(type(ginger_tea1) is chaitime)

# class car:
#     def __init__(self,brand,model,year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#     def display_info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")
# car1 = car("Toyota", "camry", 2020)
# car1.display_info()


# class car:
#     def __init__(self,brand,model,year):
#         self.brand = brand
#         self.model = model
#         self.year = year
# car1 = car("Toyota", "camry", 2020)
# print(car1.brand)
# print(car1.model)
# print(car1.year)

# # modify the properties /attributes of the class using the object
# car1.year = 2021
# print(car1.year)

# # delete the properties attribues of the class using the object==
# # del car1.year
# # print(car1.year)

# # add a new properties of the class using the object
# car1.color = "Red"
# print(car1.color)

# class person:
#     def __init__(self,name,age,city,country):
#         self.name = name
#         self.age = age
#         self.city = city
#         self.country = country
#     def __str__(self):
#         return f"name: {self.name}, age: {self.age}, city: {self.city}, country: {self.country}"
# p1 = person("Ayush", 20, "haridwar", "india")
# print(p1)



# ===inherinece is concept oop=====================
# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def introduce(self):
#         print(f"Hello, my name is  {self.name} and i am {self.age} years.old")
        
# class Ayush(person):
#     pass

# x = Ayush("Doreamon", 28)
# x.introduce()



# class human:
#     def __init__(self,name hegiht,weghit):
#         self.name = name
#         self.hegiht = hegiht
#         self.weight = weight
        
#     def eating(self,food):
#         return "{} is eating {}".format(self.name,food)
#     ram = Human("ram",6,60)        
#     steve = Human("steve",5.6,56)
# print("Height of {} is {}".format(ram.name,ram.height))  
# print("Height of {} is {}".format(ram.name,ram.weight))
# print(ram.eating("Pizza")) 
# print("weight of {} is {}.format(steve.name,steve.height)") 
# print("weight of {} is {}.format(steve.name,steve.weight)") 
# print(steave.eating("big burger"))



# class student:
#     def __init__(self,name ,roll_no,marks,):
#         self.name = name
#         self.roll_no = roll_no
#         self.marks = marks
#     def per(self):
#         print(f"student name:{self.name}, roll_no: {self.roll_no}, marks: {self.marks/500*100}")
# x =student("sonika", 12, 300,)
# x.per()


# class student:
#     def __init__(self):
#         self.n = input("enter student name:")      
#         self.m = int(input("enter student mark:"))
#     def disp(self):
#         return self.n,self.m
# for i in range(3):
#     obj = student()
#     name,mark = obj.disp()
#     print(f"{i}th student name:{name} and his mark {mark}")




# =====pholimofism===========

# class car :
#     def __init__(self,name,max_speed):
#         self.name = name
#         self.max_speed = max_speed
#     def move(self):
#         print("Drive")

# class boat:
#     def __init__(self,name,max_speed):
#         self.name = name
#         self.max_speed = max_speed
#     def move(self):
#         print("sail")
# class plane:
#     def __init__(self,name,max_speed):
#         self.name = name
#         self.max_speed = max_speed
#     def move(self):
#         print("Fly")
        
# car1 = car("Ford", "mustang")
# boat1 = boat("Boaty McBoatface", "30 knots")
# plane1 = plane("Boeing", "746")
# for x in (car1, boat1, plane1):
#     x.move()

# class datascience:
#     def area(self,length, breadth=11):
#         return length*breadth
# obje = datascience()
# l = int(input("Enter length of a rectangle:"))
# b = int(input("Enter length of a rectangle:"))
# print("area of rectangle:",obje.area(l,b))
# print("area of rectangle:",obje.area(14))
# print("area of rectangle:",obje.area(19,22))

# class circle:
#     def area(self,length=19,breadth = 26):
#         self.length = length
#         self.breadth = breadth
#         return length*breadth
# class AI(circle):
#     def perimeter(self):
#         return  2*(self.length+self.breadth)
# obj =AI()
# l = int(input("Enter length of rectangle:"))    
# b = int(input("Enter breadth of rectangle:"))    
# print(f"area of rectangle:{obj.area(l,b)}")
# print(f"perimeter of rectangle:{obj.perimeter()}")

# class circle:
#     def __init__(self,radius):
#         self.radius = radius
# class area1(circle):
#     def area(self):
#         print(f"circle of the area:{3.14*self.radius*self.radius}")
# class perameter(area1):
#     def perameter1(self):
#         print(f"circle of the perameter:{2*3.14*self.radius*self.radius}")
        
# l = int(input("Enter circle radius:"))
# obj = perameter(l)
# obj.area()
# obj.perameter1()

# print("ai"*3)
# a = [1,2,3]
# b = a
# b.append(4)
# print(a)

# def f(x,lst = []):
#     lst.append(x)
#     return lst
# print(f(1))
# print(f(2)) 

# def func(a,b=2,c=3):
#     return a+b+c 
# print(func(1,c=5))

# print(bool([])),bool([0])
# x = [i*i for i in range(3)]
# print(x)





