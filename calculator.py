print("----------------Welcome-------------   ")
print("  ")


def printvalues():  #show the arithmetic and control operator
    print("---------------------------------------")
    print("       Addition       ->  + ")
    print("       Subtraction    ->  - ")
    print("       Multiplication ->  * ")
    print("       Divide         ->  / ")
    print("       Power          ->  ** ")
    print("       Remainder      ->  % ")
    print("---------------------------------------")

def calculation():
   
        x = float(input("Enter the First Number: "))
        y = float(input("Enter the Second Number: "))
        printvalues()  # call printvalues() function
        z = input("Enter the arithmetic and control operator: ")

        if z == "+":
            result = (x + y)            

        elif z == "-":
            result = (x - y)           

        elif z == "*":
            result = (x * y)      

        elif z == "/":
            result = (x / y)            

        elif z == "**":
            result = (x ** y)           

        elif z == "%":
            result = (x % y)
                
        else:
            print("You entered the wrong value. Please try again.")
        

        print(str(x) + " "+ str(z) + " " + str(y) + " = ", result)

calculation()
