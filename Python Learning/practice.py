#output ways

print ("Shreya")   # simple string output
print("shreya  "+"gupta",22)   #string concatenation and output of integer variable
print (22) #output of integer variable


#variable building 

name = "shreya" #string variable
age = 22 #integer variable
price = 10.5 #float variable


# output of variables
print ("My name is ", name ) #output of string variable
age2 = age 
print (age2) #output of integer variable


# add two numbers

a=45
b=85
print(a+b)


# Arithmetic operations


print (a+b) # addition
print (a-b) # subtraction
print (a*b) # multiplication
print (a/b) #division
print (a%b) # modulus
print (a**b) #power


#Relational operators

print (a==b) # equality
print (a!=b) #inequality
print (a>b) # greater than
print (a<b) # less than
print (a>=b) # greater than or equal to
print (a<=b) # less than or equal to


#Assignment operators

a += 10
print(a)  # or b = a; print(b)
a -= 10
print(a)  # or b = a; print(b)
a *= 10
print(a)  # or b = a; print(b)
a /= 10
print(a)  # or b = a; print(b)


#Logical operators

print (a and b) # and
print (a or b) # or
print (not a) # not
print (a and b or a and not b) # and and or and not

# Type conversion

print (str(a)) # string
print (int(a)) # integer
print (float(a)) # float

#type casting 

print (int(a)) # integer
print (float (a)) # float


#input function

name = input ("Enter your name:")
age = input ("Enter your age:")
print ("Hello, my name is", name, "and I am", age, "years old")


#input 2 numbers and print their sum

a =input ("Enter no 1:")
b= input ("enter no 2 :")
sum= int (a)+int(b)
print ("Sum :",sum)

#input sides of square and calculate area 

l= int (input("length:"))
area = l*l
print ("area of square :",area )


#input two float values and average 

a=int (input("enter no 1:"))
b=int (input("enter no 2:"))
average =(a+b)/2
print (float(average))


# input 2 numbers and return boolean  of greater or not 

a=int(input("Enter no 1:"))
b=int(input("Enter no 2:"))
print(a>=b)
print(a<b)


#concatenation 

fname = input ("first name")
lname =input ("last name ")
fullname =fname+lname 
print (fullname)

