import random

secreto = random.randint(1, 10)

while True:
    try:
        intento = int(input("Adivina (1-10): "))
    except ValueError:
        print("Escribe un número")
    else:
        if intento == secreto:
            print("¡Acertaste!")
            break
        elif intento < secreto:
            print("Muy bajo")
        else:
            print("Muy alto")