import random

def run():
    numero_aleatorio = random.randint(1,100)
    numero_usuario = int(input("Ingrese numero del 1 al 100: "))
    while numero_usuario != numero_aleatorio:
        if numero_usuario > numero_aleatorio:
            print("El numero es menor")
        else: # elif numero_usuario < numero_aleatorio:
            print("El numero es Mayor")
        numero_usuario = int(input("Ingrese Otro Numero: "))
    print("Ganaste!!!")


if __name__ == "__main__":
    run()