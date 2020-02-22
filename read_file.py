#r - only read
#a - read and add information in file, but you cant mod existing data
#r+ - read and write
#w - overwrite file

gitignore = open(".gitignore", "r")

#checking if you can read the file, retur bool
print(gitignore.readable())

print(gitignore.read())

#read first line
print(gitignore.readline())

#print line in array
print(gitignore.readlines())
print(gitignore.readlines()[1])

gitignore.close()
