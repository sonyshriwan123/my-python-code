# print("Hello World")  
# creat a tuple==========
# thistuple = ("apple", "banana", "cherry")
# print(thistuple)
# print(thistuple[0])
# print(thistuple[1])


# thistuple = (1,) == intger=========
# print(thistuple)
# thistuple = ("apple",) string tuple====
# print(thistuple)

# type of the tuple============
# tuple = ("apple", "cherry", 1)
# print(type(tuple))

# ==============tuple constructor()================
# tuple = tuple(("apple", "cherry", "mango", "orange", "NIELIT", 1, 5, 6, 8, 9))
# print(tuple)
# print(tuple[-1])
# print(tuple[-5:])
# print(tuple[:-1])

# if "NIELIT" in tuple:
#     print("yes, is a present")


# update the tupple========

# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(x)

# x = ("apple", "banana", "cherry")
# y = list(x)
# y.append("orange")
# x = tuple(y)
# print(x)   


# ===============ad in items in to the tupple===================

# x = ("apple", "banana", "cherry") 
# y = ("orange",)
# x += y
# print(x) 
# y = list(x)
# y.remove("banana")   
# x = tuple(y)
# print(x)
# ================del==============
# del x
# print(x)


# =========================unpacking tuple=====
# tuple = ("apple", "banana", "cherry", "mango") 
# (x,y,z,a) = tuple
# print(x)
# print(y)
# print(z)  
# print(a)  


# tuple = ("apple", "banana", "cherry", "nielit") 
# (x,y,z,a) = tuple
# print(x)
# print(y)
# print(z)
# print(a)

# Fruits = ("apple", "banana", "cherry", "kiwi", "mango", "orange")
# (x,y,z,*other) = Fruits
# print(x) 
# print(y) 
# print(z) 
# print(other) 

# ===========================for loops ==========
# tuple = ("apple", "banana", "cherry") 
# for x in tuple:
#     print(x)  


# ===========inedx==================
# tuple = ("apple", "banana", "cherry") 
# print(len(tuple))  
# for i in range(len(tuple)):
#     print(tuple[i])   

# tuple = ("apple", "banana", "cherry", "orange") 
# (x,y,z,*a) = tuple
# print(x)
# print(y)
# print(z)
# print(a)






# ==========================10/03/2026=================



# ==========join two tuple
# tuple1 = ("a", "b", "c")
# tuple2 = (1, 5, 9, 5)
# # x = tuple1*2
# # print(x)
# tuple3 = tuple1 + tuple2
# print(tuple3)


# =count method==========

# thistuple = ("apple", "banana", "apple", "kiwi")
# x = thistuple.count("apple")
# print(x)

# thistuple = ("apple", "banana", "apple", "kiwi")
# x = thistuple.index("apple")
# print(x)

