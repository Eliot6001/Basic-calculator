def sum(x, y): #+function
 return      float(x) + float(y)
def neg(x, y): #-function
 return   float(x) - float(y)
def mult(x, y): #*Function
 return      float(x) * float(y)
def devi(x, y): #/function
 return      float(x) / float(y)

i = 1
while i <= 999:
    x = input("Please Enter the first number: ") #1stnumber
    z = input("Please enter the operator: ") #operator
    y = input("Please Enter the Second number: ") #2ndnumber
    if z == "+":
       print("The result is: " + str(sum(x, y)))
    if z == "-":
       print("The Result is: " + str(neg(x, y)))
    if z == "*":
        print("The Result is: " + str(mult(x, y)))
    if z == "/":
        print("The Result is: " + str(devi(x, y)))
