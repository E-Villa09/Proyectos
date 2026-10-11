#este código hay que mejorarlo mucho
import random

#Introduccion.
print()
print("****************************************")
print("¡Bienvenido al juego del ahorcado!\n")

dificultad=int(input("Que dificultad prefiere, 1. facil, 2. normal o 3. dificil: "))


# Definir las variables dependiendo de la dificultad.

if dificultad==1:
    lista=("casa", "mesa", "gato", "luna", "sol", "perro", "silla", "vaso", "flor", "reloj")
    oportunidades=9
elif dificultad==2:
    lista=("ventana", "hermano", "escuela", "biblioteca", "cuaderno", "montaña", "telefono", "playa", "zapato", "coche")
    oportunidades=7
elif dificultad==3:
    lista=("murcielago", "astronauta", "ventrilocuo", "hipopotamo", "hexagono", "ferrocarril", "criptografia", "electricidad", "cinematografia")
    oportunidades=5
else:
    print("No se ha introducido una dificultad valida.")


#definir el resto de variables.
palabra_aleatoria = random.choice(lista).lower()
palabra = ["_"] * len(palabra_aleatoria)
letras_adivinadas = set()

# Instrucciones del juego.

print("****************************************")
print("Tendrás que adivinar esta palabra:\n")
print(" ".join(palabra), "\n")
print(f"Tienes {oportunidades} oportunidades.\n")
print("****************************************")


#Bucle del juego.
while oportunidades > 0 and "_" in palabra:

    var=input("¿Quiere adivinar la palabra completa? (s/n): ")

    if var=="s":

        #Adivinar la palabra completa
        var2=input("Introduzca la palabra: ")

        if var2==palabra_aleatoria:
            palabra="A"
        else:
            oportunidades -= 1
            print(f"\nLa palabra es incorrecta, tienes {oportunidades} oportunidades.\n")


            print(" ".join(palabra))
            print(f"\nLetras introducidas: {', '.join(letras_adivinadas)}\n")


    elif var=="n":

        letra = input("\nAdivina una letra: ").lower()

        #Asegurarse de que se haya introducido una letra valida.
        if not letra.isalpha() or len(letra) != 1:
            print("Por favor, introduzca una letra válida.\n")
        elif letra in letras_adivinadas:
            print("Ya ha introducido esa letra, inténtelo de nuevo.\n")
        
        #Si la letra es valida continua el bucle
        else:
            print("\n****************************************")
            letras_adivinadas.add(letra)

            #La letra es correcta y se añade a la palabra.
            if letra in palabra_aleatoria:
                print(f"\n¡Bien hecho! {letra} está en la palabra.")
                for index, letter in enumerate(palabra_aleatoria):
                    if letter == letra:
                        palabra[index] = letra

            #La letra es incorrecta y se resta una vida.            
            else:
                oportunidades -= 1
                print(f"\nLa letra no está en la palabra, tienes {oportunidades} oportunidades.\n")


            print(" ".join(palabra))
            print(f"\nLetras introducidas: {', '.join(letras_adivinadas)}\n")

    else:
        print("Introduzca un caracter valido")



# Fin del juego.
if "_" not in palabra:
    print(f"¡Muy bien! Adivinaste la palabra '{palabra_aleatoria}'.")
else:
    print(f"Fin del juego, la palabra era '{palabra_aleatoria}'.")