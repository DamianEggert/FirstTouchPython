is_male = True
is_developer = False

if is_male and is_developer:
    print("He is male developer.")
elif is_male and not(is_developer):
    print("He is male.")
elif not(is_male) and is_developer:
    print("He is male.")
else:
    print("He is woman I guess.")


def min_num(num1, num2, num3):
    if num1 <= num2 and num1 <= num3:
        return num1
    elif num2 <= num1 and num2 <= num3:
        return num2
    else:
        return num3


example = min_num(12, 8, 7)
print(example)