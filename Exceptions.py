try:
    value = 10/0
    number = int(input("Enter number: "))
    print(number)
except ValueError:
    print("Invalid")
except ZeroDivisionError as error:
    print(error)