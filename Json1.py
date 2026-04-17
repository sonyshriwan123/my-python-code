# ==============json format=======================
# import json 
# converation to json string to python dictionary====
# x ='{"name" : "john","age" : 30,"city" : "new york"}'
# y = json.loads(x)
# # print(y)
# print(type(y))



# ======converation form python dictionary to json string=======
# x ={"name" : "john",
#       "age" : 30,
#       "city" : "new york"
#       }
# y = json.dumps(x)
# # print(y)
# print(type(y))

# ===========converatin another deta ====

# z = ("aaple", "banana")
# a = json.dumps(z)
# print(type(a))
# print(a)


# z = [ 1, "banana", True, None]
# a = json.dumps(z)
# print(type(a))
# print(a)



# print(json.dumps({"name" : "john", "age": 30}))
# print(json.dumps(["banana", "apple"]))
# print(json.dumps(("kiwi", "cherry")))
# print(json.dumps("Hello"))
# print(json.dumps(42))
# print(json.dumps(36.5))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

# import camelcase
# c = camelcase.CamelCase()
# text = "hello world"
# print(c.hump(text))