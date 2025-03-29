# 1. Crear un diccionario
# Crear el diccionario con información personal, permitiendo ingreso manual de los datos
informacion_personal = {
    "nombre": input("Ingrese su nombre: "),
    "edad": int(input("Ingrese su edad: ")),  # Aquí convertimos el dato a un entero, por eso difiere del resto
    "ciudad": input("Ingrese su ciudad: "),
    "profesion": input("Ingrese su profesión: ")
}

#2. Acceder y modificar valores
# Accedemos al dato de ciudad y lo modificamos
informacion_personal["ciudad"] = input("Ingrese una ciudad donde quisiera vivir o solo modifique la ciudad: ")  # Permite cambiar la ciudad manualmente

# Accedemos al dato de profesión y lo modificamos
informacion_personal["profesion"] = input("Revise si su profesión es correcta o modifique la que está: ")

# 3.Verificar existencias de clave
# Verificamos si la clave telefono existe y la agregamos si no está
if "telefono" not in informacion_personal:
    print("No se encontró un número de teléfono en la información. Ingréselo a continuación.")
    informacion_personal["telefono"] = input("Ingrese su número de teléfono: ")
else:
    print("Ya existe un número de teléfono en la información.")

# 4. Eliminammos una clave
# Eliminar la clave edad del diccionario ya que no es necesaria
del informacion_personal["edad"]

# 5. Imprimir el diccionario resultante después de realizar todas las operaciones
print("\nInformación personal")
for clave, valor in informacion_personal.items():
    print(f"{clave.capitalize()}: {valor}")