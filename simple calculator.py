print("Task - 2")
print("\n\nSimple Calculator!")

class Calculator:
    def add(self,x,y):
        return x + y
    
    def subtract(self,x,y):
        return x - y
    
    def multiply(self,x,y):
        return x * y
    
    def divide(self,x,y):
        return x / y
    
calculator = Calculator()

while True:
    print("\n\nSelect operation:")
    print(" 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n 5. Exit")
    choice = input("Enter choice 1,2,3,4,5 : ")
    
    if choice in ('1', '2', '3', '4'):
        try:
            n = float(input("Enter first number: "))
            m = float(input("Enter second number: "))
            
            if choice == '1':
                print(n, "+", m, "=", calculator.add(n,m))
            elif choice == '2':
                print(n, "-", m, "=", calculator.subtract(n,m))
            elif choice == '3':
                print(n, "*", m, "=", calculator.multiply(n,m))
            elif choice == '4':
                if m == 0:
                    print("Error! Division by zero.")
                else:
                    print(n, "/", m, "=", calculator.divide(n,m))
        
        except ValueError as e:
            print("Error:", e)
        
    elif choice == '5':
        print("Exiting the program.")
        break
    
    else:
        print("Invalid input, please enter a valid option!!!")

print("\n\nThank you for using simple calculator :)")