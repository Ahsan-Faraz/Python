'''1. Write a program to print multiplication table of a given number using for loop.'''
'''My logic'''
# nmb=int(input("Enter the number: "))

# for nmb in range(0,10000,nmb):
#     print(nmb)

'''Second one'''
nmb=int(input("Enter the number: "))
for i in range(1,11):
    print(f"{nmb} * {i} = {nmb*i}")
