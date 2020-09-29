print("Wellcome to shantanu's store")

sum = 0
while(True):
    userInput = input("Enter the item price one by one or press q for quit: \n")
    if (userInput != 'q'):
        sum = sum + int(userInput)
        print(f"Order total so far : {sum}")
        
    else:
        print(f"Your Bill total is {sum}. Thanks for visit, Have a Nice Day")
        break
    
