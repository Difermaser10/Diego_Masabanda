# 2. Lectura de Archivo de Texto:
# Ingresamos cinco líneas de notas para el archivo de texto desde el teclado
# Se abre el archivo my_notes.txt en modo escritura ("w")
with open("my_notes.txt", "w") as archivo:
    print("Escribe cinco notas y presiona Enter después de cada una:")

# 1. Escritura de Archivo de Texto:
# Se escriben las notas en el archivo
    for i in range(5):
        nota = input(f"Nota {i+1}: ")
        archivo.write(nota + "\n")

# Lee el contenido del archivo línea por línea utilizando el metodo adecuado
# Se abre el archivo en modo lectura ("r")
with open("my_notes.txt", "r") as archivo:
    print("\nLas líneas del archivo son:")

# Se lee cada línea del archivo una por una y se muestra en consola
    linea = archivo.readline()
    while linea:
        print(linea.strip())  # .strip() elimina el salto de línea al final
        linea = archivo.readline()

# 3. Cierre de Archivos:
# Asegúrate de cerrar el archivo my_notes.txt después de realizar las operaciones necesarias.
# Se usa with open( ) que cierra automáticamente el archivo