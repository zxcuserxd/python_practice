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

choice = (input("Enter your choice: "))
if "+" in choice:
    print("Result: ", a+b)
elif "-" in choice:
    print("Result: ", a-b)
elif "*" in choice:
    print("Result: ", a*b)
elif "/" in choice:
    print("Result: ", a/b)
else:
    print("Unknow operation")

