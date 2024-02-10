# Name : Ariba Fatima
# Email : rabbiafatima850@gmail.com

# scientific calculator
# BASIC ARITHMETIC
# 1 : add
# 2 : subtract
# 3 : multiply
# 4 : divide
# ADVANCED ARITHMETIC
# 5 : exponentiation
# 6 : square root
# TRIGONOMETRIC FUNCTIONS
# 7 : sine
# 8 : cosine
# 9 : tangent
print("select an operation to perform : ")
print("1 : add")
print('2 : subtract')
print('3 : multiply')
print('4 : divide')
print("5 : exponentiation")
print("6 : square root")
print('7 : sine')
print('8 : cosine')
print("9 : tangent")


# 1 : add
operation = input('Select  operation number : ')
if operation == "1" :
    num1 = input('Enter your first number : ')
    num2 = input('Enter your second number : ')
    sum = int(num1) + int(num2)
    print('The addition of two numbers are : ' + str(sum))


# 2 : subtract 
operation = input('Select operation number : ')
if operation == "2" :
        num1 = input("Enter your first number : ")
        num2 = input("Enter your second number : ")
        sub = int(num1) - int(num2)
        print("The subtraction of two numbers are : " + str(sub))

# 3 : multiply
operation = input('Select operation number : ')
if operation == "3":
      num1 = input("Enter your first number : ")
      num2 = input('Enter your second number : ')
      mul = int(num1) * int(num2)
      print("The multiplication of two numbers are : " + str(mul))

# 4 : divide
operation = input('Select operation number : ')
if operation == '4':
      num1 = input("Enter your first number : ")
      num2 = input('Enter your second number : ')
      div = int(num1) / int(num2)
      print('The reminder of two numbers are : ' + str(div))

# 5 : exponentiation
operation = input('Select operation number : ') 
if  operation == '5':
      base = input('Enter your first number : ')  
      power = input('Enter your second number : ')
      expo = int(base) ** int(power)
      print('The result is : ' + str(expo))

# 6 : square root
operation = input('Select operation number : ') 
if operation == '6':
      num1 = float(input('Enter your number : '))
      result = math.sqrt(num1)
      print('The result is : ' + str(result))

#  7 : sine 

operation = input('Select  operation number : ')
if operation == '7':
       angle = float(input('Enter your number in degree : '))
       result = sin(angle)
       print('The result is : '+ str(result))

#  8 : cosine      
operation = input('Select operation number : ')
if operation == '8':
       angle = float(input('Enter your number in degree :  '))
       result = cos(angle)
       print('The result is : ' + str(result))

#  9 : tangent
operation = input('Select operaton number : ')  
if operation == '9':
       angle = float(input("Enter your number in degree : "))
       result = tan(angle)
       print('The result is : ' + str(result))




      

 
     











 

