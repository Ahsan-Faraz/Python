username=input("Enter your username: ")
characterCount=len(username)
if(characterCount<10):
    print("This Username has less than 10 characters.")
else:
    print("This username has more than 10 characters.")