"""Crea una función llamada calcular_descuento que tome dos parámetros: el monto
total de la compra y un valor predeterminado para el porcentaje de descuento"""

# definimos la función calcular_descuento

def calcular_descuento(monto_total, porcentaje_descuento=15):
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Llamadas a la función

# 1. Monto de compra de $2540 con descuento por defecto de 15%
monto1 = 2540
descuento1 = calcular_descuento(monto1)
valor_a_pagar1 = monto1 - descuento1

# 2. Monto de compra de $980 con descuento del 20%
monto2 = 980
descuento2 = calcular_descuento(monto2, 20)
valor_a_pagar2 = monto2 - descuento2

# Mostrar los resultados finales
print(f"Con tu compra de $2540 recibes un descuento de ${descuento1}. Total a pagar: ${valor_a_pagar1}")
print(f"Con tu compra de $980 recibes un descuento de ${descuento2}. Total a pagar: ${valor_a_pagar2}")