def sum(x, y): #+function
 return      float(x) + float(y)
def neg(x, y): #-function
 return   float(x) - float(y)
def mult(x, y): #*Function
 return      float(x) * float(y)
def devi(x, y): #/function
 return      float(x) / float(y)
x = input("Please Enter the first number: ") #1stnumber
z = input("Please enter the operator: ") #operator
y = input("Please Enter the Second number: ") #2ndnumber

if z == "+":
   print( sum(x, y))

if z == "-":
   print( neg(x, y))

if z == "*":
    print(mult(x, y))
if z == "/":
    print(devi(x, y))
