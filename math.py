print("Welcome to the Simple Calculator.")

num_1 = input("Enter number: \n")
operator = input("Select operation (+, -, *, /): \n")
num_2 = input("Second number: \n")


num_1 = float(num_1)
num_2 = float(num_2)

if (operator == "+"):
    print(num_1 + num_2)
elif (operator == "-"):
    print(num_1 - num_2)
elif (operator == "*"):
    print(num_1 * num_2)
elif (operator == "/"):
    print(num_1 / num_2)


    
    
    
