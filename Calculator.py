from datetime import datetime

def do_add(a,b):
    return a+b

def do_sub(a,b):
    return a-b

def do_mul(a,b):
    return a*b

def do_div(a,b):
    return a/b

def do_pow(a,b):
    return a**b

def do_mod(a,b):
    return a%b

operations = {
    '+': do_add,
    '-': do_sub,
    '*': do_mul,
    '/': do_div,
    '**': do_pow,
    "^": do_pow, # На случай, если пользователь не знает про ** в python
    '%': do_mod,
}

def main():
    while True:

        first_number = input("Enter first number: ").lower()
        if first_number == "exit" or first_number == "":
            break

        second_number = input("Enter second number: ").lower()
        if second_number == "exit" or second_number == "":
            break

        operation = input("Enter operation: ").lower()
        if operation == "exit" or operation == "":
            break


        try:
            result = operations[operation](float(first_number), float(second_number))
            print(result)
        except KeyError:
            print("Invalid input or invalid operation. Available: {', '.join(operations.keys())}")
            continue
        except ZeroDivisionError:
            print("You can't divide by zero")
            continue

        print("The result has been logged")
        with open("all operations.txt", "a") as f:
            f.write(f"First num: {first_number}, second num: {second_number},"
                    f" operation: {operation}, result: {result}, at {datetime.now()}\n")

if __name__ == '__main__':
    main()