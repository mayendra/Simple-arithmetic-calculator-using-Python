""" by Mayendra Dwika Prayudha"""
""" Simple calculator for add, subtract,multiply and divide with function"""

# add function
def add(x, y):
   return x + y
# subtract function
def subtract(x, y):
   return x - y
# multiply function
def multiply(x, y):
   return x * y
# divide function
def divide(x, y):
   return x / y

# operation menu
print("=====Select Operation=====")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# collect input form user 
choice = input("Select (1/2/3/4): ")
num1 = int(input("Type Your First Number : "))
num2 = int(input("Type Your Second Number : "))
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
   try:
       print(num1,"/",num2,"=", divide(num1,num2))
   except:
       print("Wrong Input Cant divide by zero")
else:
   print(" Wrong Input Try Again")
