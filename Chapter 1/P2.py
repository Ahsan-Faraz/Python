import os 

directory_path="C:\\Users\\Lenovo\\Desktop"


contents= os.listdir(directory_path)

for items in contents:
    print(f"The content for this directory path is {items}")
