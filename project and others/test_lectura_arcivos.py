file = open("test_lectura_archivos.txt",'w')
file.write("Hola")
file.close()

file = open("test_lectura_archivos.txt",'a')
file.write(" y Adios")
file.close()

file = open("test_lectura_archivos.txt",'r')
content = file.read()
print(content)
file.close()