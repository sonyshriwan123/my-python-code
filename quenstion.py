# 1 = write find given no is prime or not
# 2 = enter no and find number reverse

# num = int(input("Enter your no:"))
# temp = 1
# if num ==2:
#     print("prime no")
# elif num >2:
#     for a in range(2,num):
#         if num %a==0:
#             temp = 2
#             break
#         if temp ==1:
#             print("num,is prime")
#     else:
#             print("num,not a prime")
# else:
#     print("wrong input")

# ==========2=========
# x = int(input("Enter your no:"))
# rev = 0
# temp =x
# while x>0:
#     r = x%10
#     rev = rev*10+r
#     x = x//10
# print("reverse of this no:",rev)

# if(temp==rev):
#     print("number is pallendrome")
# else:
#     print("number is not pallendrome")

# =============3===========
# n = int(input("Enter your no:"))
# arms = 0
# temp =n
# while n>0:
#     r = n%10
#     arms = arms+r*r*r
#     n = n//10
# print("armstrong of this no:",arms)

# if(temp==arms):
#     print("number is armstrong")
# else:
#     print("number is not armstrong")

odd = list(range(201,501,2))
print(odd)