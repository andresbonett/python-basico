# dolar_co = 3850.25 # Oct 15 2020

mensaje = """
Corversor de Moneda

  1 - Pesos Colombianos
  2 - Pesos Mexicanos
  3 - Pesos Argentinos

Escoje una opcion: 
"""
moneda = int(input(mensaje))
dolar = float(input("¿Cuantos Dolares tienes?:"))

def convercion(valor_dolar,  pais_moneda):
  pesos = round(dolar * valor_dolar, 2) # round 2 solo muestra dos decimales
  pesos = str(pesos)
  print("Tienes $" + pesos + " pesos " + pais_moneda)

if moneda == 1:
  convercion(3850, "Colombianos")
elif moneda == 2:
  convercion(21.20, "Mexicanos")
elif moneda == 3:
  convercion(77.58, "Argentinos")
else:
  print("no seleccionaste una moneda correctamente")