# Write a program to find whether a given number is prime or not.

nmb=int(input("Enter the number: "))

for i in range(2,nmb):
    if(nmb%i==0):
        print("Number is not prime.")
        break
    else:
        print("Number is prime.")