import random

def numero():
    x = random.randint(1, 100)
    a = None
    
    while x != a:
        try:
            a = int(input("Elige un número entero del 1 al 100: "))
            if isinstance(a, int):
                if a < 1 or a > 100:
                    print("El número está fuera del rango (debe ser del 1 al 100).")
                elif a < x:
                    print("El número seleccionado es menor al correcto")
                
                elif a > x:
                    print("El número seleccionado es mayor al correcto")
            else:
                print("Por favor ingresa un número entero")
        except ValueError:
            print("Ingresa un número entero válido.")
    
    print("¡Adivinaste!")

numero()