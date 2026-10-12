def add (a,b):
    return a+b
def diff (a,b):
    return a-b
def product (a,b):
    return a*b
def div (a,b):
    if (b==0):
        return "Denominator cannot be Zero"
    else:
        return a/b
def even_odd (value):
    if (num%2==0):
        return f"{num} is an Even Number"     
    else:
        return f"{num} is an Odd Number"
def even_odd(num):
    if num % 2 == 0:
        return f"{num} is Even"
    else:
        return f"{num} is Odd"
def calculate_percentage(obt, tot):
    if tot == 0:
        return "Cannot Calculate Percentage when Denominator is Zero"
    else:
        return f"Result: {(obt/tot) * 100}%"
        
def menu():
    print("\t *****Calculator Menu*****")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Check Even/Odd")
    print("6. Calculate Percentage")
    print("7. Exit")

while True:
    menu()
    action = input("Enter Your Action:")
        
    if (action == "7"):
        print ("Exiting Calculator")
        break
        
    if action in ["1","2","3","4"]:
        try:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
        except ValueError:
            print("Invalid Input!")
        if (action == "1"):
            result = add(num1,num2)
            print (f"Sum = {result}")
        elif (action == "2"):
            result = diff(num1,num2)
            print(f"Difference = {result}")
        elif (action == "3"):
            result = product(num1, num2)
            print(f"Product = {result}")
        elif (action == "4"):
            print(f"{div(num1, num2)}")
    elif (action == "5"):
        try:
            num = int(input("Enter a Number: "))
            print(even_odd(num))
        except ValueError:
            print("Invalid Input!")
    elif (action == "6"):
        try:
            obtained=float(input("Obtained Value: "))
            total=float(input("Total Value: "))
            print (calculate_percentage(obtained , total))
        except ValueError:
            print("Invalid Input!")
    else:
        print("Invalid Action!")
            

        



    
