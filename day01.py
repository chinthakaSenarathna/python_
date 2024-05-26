##How to print without newline in python

##print("hello, ",end="")
##print("welcome to the UOM")





##List

##my_list = [1,8.9,"j","hello"]
##print(my_list)
##print(type(my_list))

##-> Square Brackets -> []
##-> Ordered -> specific order
##-> Mutable -> after the creation, can add, remove items
##-> Do not need to be unique -> can duplicates items
##-> Different data types

##for i in my_list:
##    print(i)





##Array

##-> need to be unique
##-> need to be declare

##--01 array module

##-> only one data type

##import array as arr
##
##my_arr = arr.array('i',[1,2,3,4,5])
##print(my_arr)
##print(type(my_arr))
##
##for i in my_arr:
##    print(i)





##--02 numpy package

##-> different data type

##import numpy as np
##
##my_arr = np.array([1,8.9,'h',"hello"])
##print(my_arr)
##print(type(my_arr))






##Dictionary

##my_dictionary = {
##    <key>:<value>,
##    <key>:<value>,
##    <key>:<value>,
##    .
##    .
##    .
##    <key>:<value>
##    }






##Indexcing








##slicing

##example = [1,2,3,4,5]
##print(example[0:5])
##print(example[1:5])
##print(example[0:4])
##
##print(example[:5])
##print(example[3:])
##print(example[:])






##List VS Tuple -> heterogeneous data...








##functions in python

##def absolute_value(num):
##    if num >= 0:
##        return num
##    else:
##        return -num
##
##print(absolute_value(4))
##print(absolute_value(-4))












##Modules

##import calc
##
##a = 3
##b = 4
##print(calc.add(a,b))





##Packages







##Library









##reverse string,

##method 01

##my_str = 'hello, welcome !'
##my_rev_str = ''
##
####for i in range(len(my_str)):
####    my_rev_str += my_str[len(my_str)-i-1]
##
##for i in my_str:
##    my_rev_str = i + my_rev_str
##
##print(my_rev_str)


##method 02

##my_str = 'hello'
##rev_list = list(reversed(my_str))
##print(list(reversed(my_str)))
##my_rev_str = "".join(rev_list)
##print(my_rev_str)
##
##print("".join(reversed(my_str)))



##method 03

##my_str = 'hello'
##print(my_str[::-1])





##Slicing

my_list = [1,2,3,4,5,6,7,8,9,10]
print(my_list[1::2]) # -> Even
print(my_list[::2])  # -> Odd

































