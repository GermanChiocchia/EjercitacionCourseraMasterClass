file = open("demo.txt",'w')
file.write("Primera linea")
file.close()

file = open("demo.txt",'r')
print(file.read())
file.close()

file = open("demo.txt",'a')
file.write("\nSegunda linea")
file.close()

file = open("demo.txt",'r')
print(file.read())
file.close()