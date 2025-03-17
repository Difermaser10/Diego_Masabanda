#Calcula la temperatura promedio de 3 ciudades, Quito, Guayaquil y Cuenca
#Utilizaremos los datos de las 4 semanas del código de la semana anterior

#Definimos la función

def calcular_promedio_temperaturas(temperaturas):

    promedios_por_ciudad = {}

    for ciudad, semanas in temperaturas.items():
        promedios_por_ciudad[ciudad] = []  # Lista para almacenar los promedios de cada semana
        #Sumamos los datos de la semana, calcula el promedio y redondea a 2 decimales

        for i, semana in enumerate(semanas):
            suma_temperaturas = sum(dia['temp'] for dia in semana)
            promedio_semana = suma_temperaturas / len(semana)
            promedios_por_ciudad[ciudad].append(round(promedio_semana, 2))

    return promedios_por_ciudad


# Datos del código de la semana anterior para Quito, Guayaquil y Cuenca con 4 semanas
temperaturas = {
    "Quito": [
        [  # Semana 1
            {"dia": "Lunes", "temp": 14},
            {"dia": "Martes", "temp": 16},
            {"dia": "Miércoles", "temp": 15},
            {"dia": "Jueves", "temp": 17},
            {"dia": "Viernes", "temp": 18},
            {"dia": "Sábado", "temp": 19},
            {"dia": "Domingo", "temp": 20}
        ],
        [  # Semana 2
            {"dia": "Lunes", "temp": 13},
            {"dia": "Martes", "temp": 15},
            {"dia": "Miércoles", "temp": 16},
            {"dia": "Jueves", "temp": 18},
            {"dia": "Viernes", "temp": 17},
            {"dia": "Sábado", "temp": 20},
            {"dia": "Domingo", "temp": 21}
        ],
        [  # Semana 3
            {"dia": "Lunes", "temp": 12},
            {"dia": "Martes", "temp": 14},
            {"dia": "Miércoles", "temp": 15},
            {"dia": "Jueves", "temp": 17},
            {"dia": "Viernes", "temp": 18},
            {"dia": "Sábado", "temp": 19},
            {"dia": "Domingo", "temp": 22}
        ],
        [  # Semana 4
            {"dia": "Lunes", "temp": 15},
            {"dia": "Martes", "temp": 17},
            {"dia": "Miércoles", "temp": 18},
            {"dia": "Jueves", "temp": 19},
            {"dia": "Viernes", "temp": 20},
            {"dia": "Sábado", "temp": 21},
            {"dia": "Domingo", "temp": 23}
        ]
    ],
    "Guayaquil": [
        [  # Semana 1
            {"dia": "Lunes", "temp": 24},
            {"dia": "Martes", "temp": 25},
            {"dia": "Miércoles", "temp": 26},
            {"dia": "Jueves", "temp": 27},
            {"dia": "Viernes", "temp": 28},
            {"dia": "Sábado", "temp": 29},
            {"dia": "Domingo", "temp": 30}
        ],
        [  # Semana 2
            {"dia": "Lunes", "temp": 23},
            {"dia": "Martes", "temp": 24},
            {"dia": "Miércoles", "temp": 25},
            {"dia": "Jueves", "temp": 26},
            {"dia": "Viernes", "temp": 27},
            {"dia": "Sábado", "temp": 28},
            {"dia": "Domingo", "temp": 29}
        ],
        [  # Semana 3
            {"dia": "Lunes", "temp": 22},
            {"dia": "Martes", "temp": 23},
            {"dia": "Miércoles", "temp": 24},
            {"dia": "Jueves", "temp": 25},
            {"dia": "Viernes", "temp": 26},
            {"dia": "Sábado", "temp": 27},
            {"dia": "Domingo", "temp": 28}
        ],
        [  # Semana 4
            {"dia": "Lunes", "temp": 21},
            {"dia": "Martes", "temp": 22},
            {"dia": "Miércoles", "temp": 23},
            {"dia": "Jueves", "temp": 24},
            {"dia": "Viernes", "temp": 25},
            {"dia": "Sábado", "temp": 26},
            {"dia": "Domingo", "temp": 27}
        ]
    ],
    "Cuenca": [
        [  # Semana 1
            {"dia": "Lunes", "temp": 15},
            {"dia": "Martes", "temp": 18},
            {"dia": "Miércoles", "temp": 15},
            {"dia": "Jueves", "temp": 16},
            {"dia": "Viernes", "temp": 20},
            {"dia": "Sábado", "temp": 19},
            {"dia": "Domingo", "temp": 12}
        ],
        [  # Semana 2
            {"dia": "Lunes", "temp": 13},
            {"dia": "Martes", "temp": 14},
            {"dia": "Miércoles", "temp": 16},
            {"dia": "Jueves", "temp": 17},
            {"dia": "Viernes", "temp": 17},
            {"dia": "Sábado", "temp": 19},
            {"dia": "Domingo", "temp": 21}
        ],
        [  # Semana 3
            {"dia": "Lunes", "temp": 12},
            {"dia": "Martes", "temp": 13},
            {"dia": "Miércoles", "temp": 15},
            {"dia": "Jueves", "temp": 18},
            {"dia": "Viernes", "temp": 19},
            {"dia": "Sábado", "temp": 19},
            {"dia": "Domingo", "temp": 12}
        ],
        [  # Semana 4
            {"dia": "Lunes", "temp": 17},
            {"dia": "Martes", "temp": 15},
            {"dia": "Miércoles", "temp": 18},
            {"dia": "Jueves", "temp": 16},
            {"dia": "Viernes", "temp": 11},
            {"dia": "Sábado", "temp": 13},
            {"dia": "Domingo", "temp": 10}
        ]
    ]
}

# Llamamos a la función y mostramos los resultados
resultados = calcular_promedio_temperaturas(temperaturas)
for ciudad, promedios in resultados.items():
    print(f"\nCiudad: {ciudad}")
    for i, promedio in enumerate(promedios):
        print(f"Semana {i + 1}: Promedio de temperatura = {promedio}°C") #imprime los promedios de cada semana