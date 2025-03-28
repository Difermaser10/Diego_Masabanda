# Crear el diccionario con información personal
informacion_personal = {
    "nombre": "Diego Masabanda",
    "edad": 42,
    "ciudad": "Quito",
    "profesion": "Editor"
}

# Acceder y modificar la ciudad
informacion_personal["ciudad"] = "Guayaquil"  # Cambiar la ciudad

# Agregar una nueva clave-valor para la profesion (ya existe, pero lo aseguramos)
informacion_personal["profesion"] = "Editor de textos educativos"

# Verificar si la clave "telefono" existe y agregarla si no está
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0986437637"

# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)
