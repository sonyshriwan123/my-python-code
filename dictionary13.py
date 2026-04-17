#=================== Dictinonary python========================= 
# mydict = {"name": "sonika shriwan",
#           "age" : 20,
#           "state" : "uttarkhand",
#           "distric" : "rpg"}
# print(mydict)  

# ============acess  the value using the key======================
# print(mydict["name"])
# print(mydict["age"])
# print(mydict["state"])
# print(mydict["distric"])

# print(mydict["age"])
# print(mydict["age"])
# print(mydict["age"])

# mydict2 = {"name": "sonika shriwan",
#           "age" : 20,
#           "height" : 25,
#           "distric" : "rpg"}
# # print(mydict2)

# # ===================find the length of the =====================
# print(len(mydict2))


# ========data types of dictionary ============================
# mydict3 = {"name": "sonika shriwan",
#           "age" : 20,
#           "height" : 25,
#           "distric" : "rpg",
#           "is_married" : False}
# print(len(mydict3))
# print(mydict3)

# =================the dict constructor can be used to create a dictionary============
# mydict4 = dict(name="sonika shriwan",age = 20,height = 25,distric = "rpg",is_married = False)
# print(mydict4)


# ===============acess the dictionary item using get() method================
# print(mydict4.get("name"))
# print(mydict4.get("age"))
# print(mydict4.get("distric"))

# =======key =====================
# x = mydict4.keys()
# print(x)

# =================type of dictionary=================
# print(type(mydict4))

# =======valuse==================
# x = mydict4.values()
# print(x)


# car = {
#     "brand" : "Ford",
#     "model" : "mustang",
#     "year"  : 1964}
# x = car.values()
# car["year"] = 2020
# print(x)


# ====remove an items dictinory using the pop==============
# car = {
#     "brand" : "Ford",
#     "model" : "mustang",
#     "year"  : 1964}
# car.pop("model")
# print(car)



# car = {
#     "brand" : "Ford",
#     "model" : "mustang",
#     "year"  : 1964}

# car.popitem()
# print(car)


# ===============del===========
# car = {
#     "brand" : "Ford",
#     "model" : "mustang",
#     "year"  : 1964}
# del car["model"]
# print(car)


# =========clear=============
# car = {
#     "brand" : "Ford",
#     "model" : "mustang",
#     "year"  : 1964}
# car.clear()
# print("we have got an empty dictionary here in this ",car)

# =============== looping through for loop =========
# car = {
#     "brand" : "Ford",
#     "model" : "mustang",
#     "year"  : 1964}
# for x in car:
#     print(x)
#     print(car[x])


# car = {
#     "brand" : "Ford",
#     "model" : "mustang",
#     "year"  : 1964}

# for x in car.values():
#     print(x)

# car = {
#     "brand" : "Ford",
#     "model" : "mustang",
#     "year"  : 1964}

# for x in car.keys():
    # print(x)
# for x in car.items():
    # print(x)


# =============copy and dict===================================
# car = {
#     "brand" : "Ford",
#     "model" : "mustang",
#     "year"  : 1964}

# car2 = car.copy()
# print(car2)

# ================dict copy dict() fumction
# car = {
#     "brand" : "Ford",
#     "model" : "mustang",
#     "year"  : 1964}

# car2 =dict(car)
# print(car2)


# =====nested dictionary=================
# myfamily = {
#     "child1": {
#         "name" : "emali",
#         "year" : 2000
#     },
#     "child2": {
#         "name" : "email",
#         "year" : 2005
#     },
#     "child3": {
#         "name" : "email",
#         "year" : 2004
#     }

# print(myfamily)

# ===============neted dict===============
# child4 ={
#         "name" : "email",
#         "year" : 2009
#     },
# child5 ={
#         "name" : "email",
#         "year" : 2008}
# x = {
#     "child4":child4,
#     "child5":child5
# }
# print(x)


# myfamily = {
#     "child1": {
#         "name" : "emali",
#         "year" : 2000
#     },
#     "child2": {
#        "name" : "email",
#         "year" : 2005
#     },
#     "child3": {
#         "name" : "email",
#         "year" : 2004
#     }
# }
# print(myfamily["child2"]["name"])






