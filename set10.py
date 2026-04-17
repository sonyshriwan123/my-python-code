# ===========declane a set using curly beaces=============
# myset = {"apple", "banana", "kiwi"}
# print(myset)

# =============duplicate value==============

# myset = {"apple", "banana", "kiwi", "apple"}
# print(myset)



# ==truse and 1 are considered the in python, and they are treated as equal when used in a set.
# myset = { True, 1, "apple", "banana", "kiwi", "apple"}
# print(myset)
# myset = { 1,True,"apple", "banana", "kiwi", "apple"}
# print(myset)  

# myset = { True, 1,True, False,0,True, 1, False,0}
# print(myset)

# ============length of set==================
# myset = {"apple", "banana", "kiwi"}
# print("the length of x set is: ",len(myset))   #is give will the length 


# myset = {"apple", "banana", "kiwi"}
# print(type(myset)) 

# ==============() constructor=======
# myset = set(("apple", "banana", "kiwi"))
# print(myset)


# ================Iterating throughj a set using  for loop======

# x = {"apple", "banana", "kiwi"}
# for i in x:
#     print(i)    

# x = {"apple", "banana", "kiwi"}
# if "apple" in x:
#     print("yes, 'apple' is in the set x")
# else:
#     print("no, 'apple' is not in the set")

# thisset = {"apple", "banna", "kiwi"}
# print("apple" in thisset)   

# ======add==========
# thisset = {"apple", "banna", "kiwi"}
# thisset.add("cherry")
# print(thisset)

# =================update set=====================

# anotherset = {"mango", "banana", "kiwi"}
# main = {"apple", "cherry", "orange"}
# main.update(anotherset)
# print(main)

# ==============addd to list and set============
# thisset = {"mango", "banana", "kiwi"}
# thislist = ["apple", "cherry", "orange"]
# thisset.update(thislist)
# print(thisset)



# ===================Remove Item from the set=========
# thisset = {"mango", "banana", "kiwi"}
# thisset.remove("banana")
# print(thisset)


# thisset.discard("apple")
# print(thisset)

# ==========================11/03/2026=============
# ===================joining the set ==============
# set1 = {"a","b","c","d"}
# set2 = {1,2, 3, 4}
# set3 = set1.union(set2)
# print(set3)


# =========multipl setsa joing updates==========
# set1 = {"a","b","c","d"}
# set2 = {1,2, 3, 4}
# set3 = ("x", "y","z")
# x = set1.union(set2,set3)
# print(x) 

# ===============another method to join mulitple sets using==========
# set1 = {"a","b","c","d"}
# set2 = {1,2, 3, 4}
# set3 = {"x", "y","z"}
# x = set1| set2| set3
# print(x)

# =============merge sets and tupples using union() method
# set1 = {"a","b","c","d"}
# tup1 = (1,2, 3, 4)
# x = set1.union(tup1)
# print(x)


# set1 = {"a","b","c","d"}
# tup1 = (1,2, 3, 4)
# set1.update(tup1)
# print(set1)

# =====not====
# 123 = {"a","b","c","d"}
# 456= (1,2, 3, 4)
# 123.update(456)
# print(set1)

# ===========intersection of sets=====================
# ===========common items of a set1 and set2====

# set1 = {"apple", "banana", "cherry", "c"}
# set2 = {"google", "microsoft", "Apple", "c"}
# x = set1.intersection(set2)
# print(x)


# ===============common=================

# set1 = {True, "banana", 1, False, 0, True,"c"}
# set2 = {False, 0, True, "microsoft",  "c"}
# set3 = set1.intersection(set2)
# print(set3)

# ==========================symmetric difference of set===============

# set1 = {"apple", "banana", "cherry", "c"}
# set2 = {"google", "microsoft", "Apple", "c"}
# set3 = set1.symmetric_difference(set2)  #not common
# print(set3)  


# set1 = {"apple", "banana", "cherry", "c"}
# set2 = {"google", "microsoft", "Apple", "c"}
# set1.symmetric_difference_update(set2)  
# print(set1)


# creating  a frozen set using the frozenset() constructor
# myfrozenset = frozenset(["apple", "banana", "cherry"])
# print(myfrozenset)





# name = input("enter your name :")
# print(name)



# x = int(input("enter your first number :"))
# y = int(input("enter your second number :"))
# z = (x//y)
# print(z)
















# ========declane a set using set() function==
# myset2 = set(("apple","banana", "kiwi"))
# print(myset2)
