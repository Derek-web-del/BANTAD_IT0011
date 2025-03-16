def divide(x, y):
    if y != 0:
        return x / y
    else:
        return None

def exponentiation(x, y):
    return x ** y

def remainder(x, y):
    if y != 0:
        return x % y
    else:
        return None

def summation(x, y):
    if y > x:
        return sum(range(x, y + 1))
    else:
        return None

def main():
    print("Functions Display")
    print("=========================")
    print("[D] Divide \n[E] Exponentiation \n[R] Remainder \n[F] Summation ")
    print("=========================")
    choice = input("Enter Operation Choice: ")
    
    if choice == "D":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = divide(num1, num2)
        if result is not None:
            print("Result:", result)
        else:
            print("Denominator cannot be zero")
    
    elif choice == "E":
        num1 = float(input("Enter the base number: "))
        num2 = float(input("Enter the exponent: "))
        result = exponentiation(num1, num2)
        print("Result:", result)

    elif choice == "R":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = remainder(num1, num2)
        if result is not None:
            print("Result:", result)
        else:
            print("Denominator cannot be zero")

    elif choice == "F":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = summation(num1, num2)
        if result is not None:
            print("Result:", result)
        else:
            print("Second number must be greater than the first number")

    else:
        print("Error, Try Again.")

if __name__ == "__main__":
    main()
