###########################
#date 3-12-2018
###########################

print(5/2) #Its a simple devision
print (5//2) #Its intiger devison or floor devision 
print(2*3)  # It represent multiplication
print(2**3) # It represent power of 2 raise 3
print (10 % 3) # It is modulus of 10 by 3
print("vishy")  # the print of string
print('Vishy\'s laptop is "Awsome" ') # we can use dash in string by '\' (forward slash)
print(2 *  'Ram ' * 2)  # if we want to keep only one then we can keep It
print('c:\docs\navin') # \n means new line 
print(r'c:\user\navin') # This won't try to convert the \n into new line as we have used 'r' - Raw strin in the begining
print('hello to git')
x=10
print (x+20)
name = "Flower"
print(name[0])# printing string from left(first) to right(last) strats from 0
print(name[-1]) # printing string from right(last) to left(first) sarts from -1
print(name[1:4]) #from 1 to 3 including excluding position 4
# we can write [1:] ,  [:3]  
# string in python is immutabel. I can just concate it or can use certain part of it
print('Length of the string is ' +str(len(name))) # here we have made typecasting and concate the string with integer


##########################
# #################concepts of List It is resembling to concepts of the array in the other language
##################List is mutable 
###########################

num = [10,20,30,20,54,12]
print(num[0]) # we can fetch the value at index position 0 
print(num[-1]) # simmilarly as string it also work for the number from behind
print(num)
people=['Vishy','Dheeraj','Anna','Andre'] # we can have string also 
print(people)
other = ['Vishy',3.25,'Jiya',2] # we can add mix of number and string also
print(other)
combo = num+people+other # we can take addition of the all the list we want 
print(combo)
num.append(555) # will append the element at the last
print(num)
num.insert(2,245) # will insert the number at the specific index 2
print(num)
num.remove(30) # will remove the specific elemet by mentioning it 
print(num) 
num.pop(1)# will remove the elemen at the specific index 1
print(num)
del num[1:3] # We can delete more than one elements 
print(num)
num.extend([999,888,777]) # we can add multiple values in the list
print(num)
num.sort()
print(num) # We can sort the list but we can not sort the list contains string  
# some inbuilt functions are ther for the list like
print(min(num))
print(max(num))
print(sum(num))

###########################
# tuples in python 
# it is simmilar to List but tuple is immutable and we use round bracs (  )
# Iteration in the tuple is faster than the list as it is immutable 
###########################
print('\n Tuple in the python')
tup = (23,25,35,65,95,25) # tuple in the python
print(tup)
print(tup[1]) # here index fetch working same as list and string did
print(tup.count(25)) # count will count the number of the occurance of the number
print('index number of the element 25 in tuple is : '+str(tup.index(25))) # will give the index number of element 

###########################
# set in python
# curly bracs use for the set { }
# set is not mutable 
###########################
# Set is not sequence number as it use hash wich can enhance the computation
set1 = {23,25,255,54,25,1}
print(set1) # here it will not repeat the elemet "25"
#code of date 4-12-2018
#new commnet on git