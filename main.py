import random


def demander_nombre(nb_min, nb_max):
    nombre_int = 0
    while nombre_int == 0:
        nombre_str = input(f"Quel est le nombre magique entre {nb_min} et {nb_max} ? ")
        try:
            nombre_int = int(nombre_str)
        except:
            print("ERREUR: Vous devez saisir un nombre. Veuillez réessayer.")
        else:
            if nombre_int < nb_min or nombre_int > nb_max:
                print(f"ERREUR: Vous devez saisir un nombre entre {nb_min} et {nb_max}. Réessayer.")
                nombre_int = 0
    return nombre_int


NOMBRE_MIN = 1
NOMBRE_MAX = 100
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NB_VIES = 10

gagne = False
for i in range(0, NB_VIES):
    vies = NB_VIES-i
    print(f"Il vous reste {vies} vies !")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print("Bravo ! Vous avez gagné !")
        gagne = True
        break
    elif nombre > NOMBRE_MAGIQUE:
        print("Le nombre est plus petit.")
        vies -= 1
    else:
        print("Le nombre est plus grand.")
        vies -= 1

if not gagne:
    print(f"Vous avez perdu. Le nombre magique était {NOMBRE_MAGIQUE}.")