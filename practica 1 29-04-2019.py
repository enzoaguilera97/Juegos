'''
Hacer un juego donde el usuario adivine un numero.
'''


import random
intentos = 0
num_menor = 1
num_mayor = 20

numero = random.randint(num_menor,num_mayor)

print("let's play a game, choice a number between 1 and 20, the computer will tell you if you guess the number")

while intentos < 10:
    guess = int(input("guess the number"))

    intentos = intentos +1

    if guess < numero:
        print("your number is too low")
    if guess > numero:
        print("your number is too high")

    if guess == numero:
        #intentos = str(intentos)
        print("congratulations you guess the number, you did it in tries", intentos)











