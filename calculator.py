class Calculations: 
    def __init__(self):
        pass
    def sum(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b
    
    def run(self):
        """Interactive method to get user input and perform calculations"""
        print("=" * 40)
        print("Welcome to Calculator")
        print("=" * 40)
        
        while True:
            print("\nChoose an operation:")
            print("1. Sum")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Exit")
            
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '5':
                print("Thank you for using Calculator!")
                break
            
            if choice not in ['1', '2', '3', '4']:
                print("Invalid choice! Please enter 1-5.")
                continue
            
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter valid numbers.")
                continue
            
            result = None
            
            if choice == '1':
                result = self.sum(num1, num2)
                print(f"\n{num1} + {num2} = {result}")
            elif choice == '2':
                result = self.subtract(num1, num2)
                print(f"\n{num1} - {num2} = {result}")
            elif choice == '3':
                result = self.multiply(num1, num2)
                print(f"\n{num1} * {num2} = {result}")
            elif choice == '4':
                result = self.divide(num1, num2)
                print(f"\n{num1} / {num2} = {result}")


calc = Calculations()
calc.run()

