# simple list comprehension
values =  []

for x in range(1,10):
     values.append(x)
#print(values)
# can be written like this:
values_com = [x for x in range(1,10)]
#print(values_com)

# get all of the even numbers from 0 to 50
even_vals = []
for x in range(50):
     if (x % 2==0 ):
          even_vals.append(x)
#print(even_vals)

# pythonic way:
even_vals_com = [x for x in range(50) if (x% 2 ==0 )]
#print(even_vals_com)


# comprehensions with multiple conditions:

# getting the valid strings
options = ["any" , "albany", "apple","world", "hello",""]
valid_strings = []
# unpythonic way
for string in  options:
          if len(string) <=1:
                    continue
          if string[0] != 'a':
               continue
          if string[-1] != 'y':
               continue
          valid_strings.append(string)

#print(valid_strings)
# pythoic way
valid_string_com = [
     string for string in options
     if len(string) > 1
     if string[0] == 'a'
     if(string[-1] ) == 'y'
]

#print(valid_string_com)

# multiple lists comprehension

# flatening a matrix the unpythonic way
matrix  = [[1,2,3] , [4,5,6] , [7,8,9]]
flatten = []
for list in matrix:
    for i in list:
      flatten.append(i)
#print(f"Flatten list: {flatten}")

# the pythonic way
flatten_cmp = [i for list in matrix for i in list]
#print(f"Flatten list: {flatten_cmp}")


# categorization of data in by list comprehension
categories  = []

# unpythonic way
for i in range(10):
    if i % 2 == 0:
        categories.append("Even")
    if i % 2 != 0:
        categories.append("Odd")
#print(categories)


categories_com = ["Even" if x % 2 == 0 else "Odd" for x in range(10)]
#print(categories_com)

# nested comprehension

lst = []

for i in range(5):
    li1 = []
    for j in range(5):
        li2 = []
        for k in range(5):
            li2.append(k)
        li1.append(li2)
    lst.append(li1)
print(lst)

# pythonic way

lst_com = [[[k for k in range(5)] for _ in range(5)] for _ in range(5)]
print(lst_com)