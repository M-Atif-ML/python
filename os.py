import os 
print(os.getcwd())

# os.makedirs('OS-Demo-2/subdirs')

# os.rename('gcd.cpp','NewC++.cpp')

file_path = input("Enter your file path: ")
size_of_file = os.stat(file_path).st_size

if size_of_file  >1000111 :
    print("The file is removed")
    os.remove(file_path)
else:
    print("The file is not removed")
