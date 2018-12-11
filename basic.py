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
# set in python collection of unique elements
# curly bracs use for the set { }
# set is immutable 
###########################
# Set is not sequence number as it use hash wich can enhance the computation
set1 = {23,25,255,54,25,1}
print(set1) # here it will not repeat the elemet "25"
#code of date 4-12-2018
#new commnet on git

# summery on set and list 
# set is collection of unique elements, like in list if you repeat something 
# i.e some number like 12 then it is repeated again, 
# but in sets if you write 12 number 2 times then it will display only once, so this is 1st one. 
# 2nd one is set is working on concept of hash, where list not working on concept of hash! 
# 3rd one is in sets index number is not working, because sets can't maintain sequence, 
# but list maintain sequence, eo index number is working in list! 
# So these are some of difference between set and list! 


#Date 11-12-2018
num = 'navin'
print(id(num)) # we can print the address of the num usning id function 
a = 10
b = a 
print(id(a))
print(id(b))   # see here we get the same address for both variable that is why python is more efficient in memory management
# even for the following statement address will be the same 
print(id('ram'))
c = 'ram'
print(id(c))
# if any variable will not be used for the long time in the code then it will be in garbage collection 

# Data types in python 
# None,  Numeric, List, Tuple, Set, String, Range, Dictionary(Map)

#None - Data type when we won't assign anything to variable it will be null here we won't use any thing to define null
x
print(x)

#Numeric - Datatype have four subtypes 
# 1. int 
# 2. float 
# 3. complex 
# 4. Bool 
inte = 1
flo = 2.0
comp = 2 + 3j
a<b    # cause a and b both are the 10 so 10<10 will be false
print (a<b)
print(str(type(inte))+"  "+str(type(flo))+"  "+str(type(comp))+"  "+str(type(a<b)) )
# we can make typecasting in python like below
# newvarname =  datetype(oldvariable)  => so the new variable will be the type of data type we want 

# List, Tuple, Set, String, Range ===> All this data types are come under Seuence term 
lissss = [12,25,25,32,540]
tupppp = (14,25,48,54)
setttt = {14,25,25,144,18,98}
stringggg = "Ram"
rangeeeee = range(2,10,2) # range (starting, upto , difference ) ||| we can also just give upto and then it will count from 0th number
print(list(rangeeeee))

# Dictioanry (Map) --> key and value => {key1:value1 , key2:value2 , , , , }
rollno = { '1':'Bharat', '2':'Nayan', '3':'Rahul', '4':'Kishan' }
print(str(rollno.keys())) # we will get all the the keys of rollno Dictionary
print(str(rollno.values())) # we will get all the values of rollno Dictionary
print(str(rollno['1'])) # So here we are giving => dictionary_name['key'] for getting respective value
# we can also use get function ===>  directory_name.get('key')

