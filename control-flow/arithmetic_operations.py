def perform_operation(num1, num2, operation):
    match operation:
        case "+":
            print(num1+num2)
        case "-":
            print(num1-num2)
        case "*":
            print(num1*num2)
        case "/":
            if num1==0 or num2==0:
                print ("Division by zero error")
            else:
                print (num1/num2)
perform_operation(30,5,"/")