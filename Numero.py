import random

def generate_num():
    return random.randint(1, 100)
     
def player_guess():
    while True:
        try:
            guess = int(input('Seleccionar un numero entero del 1 al 100: '))
            return guess
        except ValueError:
            print("El valor ingresado no es un número entero. Por favor, intenta nuevamente.")

def valid_guess(guess):
    return 1 <= guess <= 100

def verif_valid_guess(valid, guess, num_to_guess):
    if valid:
        if guess < num_to_guess:
            return "El numero elegido es menor al correcto"
        elif guess > num_to_guess:
            return "El numero elegido es mayor al correcto"
        elif guess == num_to_guess:
            return "Adivinaste!"
    else:
        return "El valor ingresado no es valido. Por favor ingresa un numero entero del 1 al 100" 

def status_game(guess, num_to_guess):
    return guess != num_to_guess

def game():
    num_to_guess = generate_num()
    status = True
    while status:
        guess = player_guess()
        valid = valid_guess(guess)
        print(verif_valid_guess(valid, guess, num_to_guess))
        status = status_game(guess, num_to_guess)

game()
