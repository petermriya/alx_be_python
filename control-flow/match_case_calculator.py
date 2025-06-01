num1 = int(input ("Enter the first number: "))
num2 = int(input ("Enter the second number: "))
operation = input ("Choose the operation (+, -, *, /)")

a=num1+num2
b=num1-num2
c=num1*num2

match operation:
    case "+":
        print (f"The result is {a}")
    case "b":
        print (f"The result is {b}")
    case "*":
        print (f"The result is {c}")
    case "/":
        if num2 == 0:
            print ("Cannot divide by zero.")
        else:
            d = num1/num2
            print (f"The result is {d}")



