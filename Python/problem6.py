'''
1. Write a program to print multiplication table of a given userber using for loop.'''
# user = int(input("enter user which table you want : "))
# for i in range(1,11):
#     print(i*user)

'''
2.Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
l = ["Harry","Soham","Sachin","Rahul"]'''

# l = ["Harry","Soham","Sachin","Rahul"]

# l = ["Harry","Soham","Sachin","Rahul"]
# for name in l:
#     if(name.startswith("S")):
#         print(f"helllo {name}")







# for person in l:
#         if(person == "Harry" ):
#                 continue
#         if(person == "Rahul"):
#                 continue
#         print(f"hello {person}")
#       
'''3. Attempt problem 1 using while loop.'''
# table= int(input("enter user :"))
# i = 1
# while(i<=10):
#     print(i*table)
#     i= i+1

'''
4. Write a program to find whether a given number is prime or not.
'''

# Program to check if a number is prime
# user = int(input("Enter a number: "))

# if user > 1:
#     for i in range(2, user):
#         if user % i == 0:
#             print(user, "is not a prime number.")
#             break
#     else:
#         print(user, "is a prime number.")
# else:
#     print(user, "is not a prime number.")


# user = int(input("enter a num"))

# for i in range (2 , user):
#     if(user % i) == 0:
#         print("this is a not prime number")
#         break
   
# else:
#   print("this is  prime")


'''
7. Write a program to print the following star pattern.
  *
 ***
***** for n = 3 '''

# user = int(input("enter a number :"))

# for i in range(1 , user+1):
#     print(" " * (user-i), end="")
#     print("*"*(2*i-1), end="")
#     print("")


# n = "*"
# for i in range (0 , 3):
#     if (i == 0 ):
#         print( n * 1)
#         continue
#     if(i == 1):
#         print(n*3)
#         continue
#     if(i == 2):
#         print(n*5)

# else:
#     print("code over")

'''
8.Write a program to print the following star pattern:
   *
   **
   *** for n = 3'''


# n = "*"
# for i in range (0 , 3):
#     if (i == 0 ):
#         print( n * 1)
#         continue
#     if(i == 1):
#         print(n*2)
#         continue
#     if(i == 2):
#         print(n*3)

# else:
#     print("code over")

# user = int(input("enter number"))

# for i in range (1 , user+1):
#     print("*"* (2*i -1), end="")
#     print("")

'''
9. Write a program to print the following star pattern.
* * *
*   * 
* * * for n = 3
'''

# user = int(input("enter a number"))

# for i in range(1 , user+1):
#     if(i == 1 or i == user):
#         print("*"*user)
#     else:
#         print("*"+" "*(user-2)+"*")

'''
10.Write a program to print multiplication table of n using for loops in reversed
   order.'''

user =int(input("enter your reverse table number :"))

for i in range (1 , user+1):
    print(i)