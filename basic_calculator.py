num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter first secend: "))


if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
elif op == "%":
    print(num1 % num2)
else:
    print("You need to enter one of thoes operators: +, -, *, /, %.")


def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(5, 3))
