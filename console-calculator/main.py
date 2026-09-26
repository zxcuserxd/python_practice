print("Welcome to my console calculator!\n")

def read_numbers(prompt):
    while True:
        try:
           number = int(input(prompt))
        except ValueError:
            print("Please enter a number!")
            continue
        text = str(number)
        if len(text) <= 6:
            return int(text)
        print("Too many numbers!")


a = read_numbers("Enter A: ")
b = read_numbers("Enter B: ")

print("Choice operations: [ + ][ - ][ * ][ / ]")

choice = input("Enter your choice: ").strip()
match choice:
    case "+":
        print("Result: ", a+b)
    case "-":
        print("Result: ", a-b)
    case "*":
        print("Result: ", a*b)
    case "/":
        if b == 0:
            print("Division by zero is undefined")
        else:
            print("Result: ", a / b)
    case _:
        print("Invalid choice!")
