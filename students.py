from Student import Student

student1 = Student("Damian", "IT", 4.4, True)
student2 = Student("Agata", "Dentis", 5.1, False)

print("Is " + student1.name + " honor to upper class?\n" + str(student1.on_honor_roll()))
print("Is " + student2.name + " honor to upper class?\n" + str(student2.on_honor_roll()))


