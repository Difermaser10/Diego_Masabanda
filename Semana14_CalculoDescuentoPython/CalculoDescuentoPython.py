"""Crea una función llamada calcular_descuento que tome dos parámetros: el monto
total de la compra y un valor predeterminado para el porcentaje de descuento"""

# definimos la función calcular_descuento

def calcular_descuento(monto_total, porcentaje_descuento=15):
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Llamadas a la función

# 1. Monto de compra de $2500 con descuento por defecto de 15%
monto1 = 2540
descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - descuento1

# 2. Monto de compra de $700 con descuento del 20%
monto2 = 980
descuento2 = calcular_descuento(monto2, 20)
monto_final2 = monto2 - descuento2

# Mostrar resultados
print(f"Compra de ${monto1}: Descuento de ${descuento1}, Total a pagar: ${monto_final1}")
print(f"Compra de ${monto2}: Descuento de ${descuento2}, Total a pagar: ${monto_final2}")