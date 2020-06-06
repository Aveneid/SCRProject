from os import remove
file = open("file.txt","w")
file.write("Writing something to file")
print(remove("file.txt"))
file.close()
print(remove("file.txt"))