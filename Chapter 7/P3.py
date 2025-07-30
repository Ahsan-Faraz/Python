'''1. Write a program to print multiplication table of a given number using while loop.'''

nmb=int(input("Enter the number: "))
i=1
while(i<11):
    print(f"{nmb} * {i} = {nmb*i}")
    i+=1