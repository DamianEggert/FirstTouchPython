def credential():
    name = input("What is your name?\n")
    surname = input("What is your surname?\n")
    age = input("What is your age?\n")
    sex = input("What is your sex?\n")
    print("Hello " + name + surname + ". You are " + str(age) + " years old " + sex + ".")


credential()