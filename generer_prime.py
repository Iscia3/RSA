import random
import premier 

def gen_prime(length):
    """
    Génère un nombre premier de 'lenght' chiffres.
    Arguments:
    -lenght (int) : Nombre de chiffres du nombre premier à générer.
    Retourne:
    - (int) : Un nombre premier aléatoire de 'lenght' chiffres.
    """
    random.seed()
    # Construction du nombre aléatoire
    first_digit=random.choice("123456789") # Premier chiffre
    digit="0"+first_digit
    last_digit=random.choice("1379") # dernier chiffre
    nb=""
    nb_premier=""
    for i in range(length):
        if i==0:
            nb=nb+random.choice(first_digit)
        elif i==length-1:
            nb=nb+random.choice(last_digit)
        else:
            nb=nb+random.choice(digit)
        #print(nb)

    if premier.is_prime(nb)==True:
        nb_premier=nb
    else:
        return gen_prime(length)
            
    return nb_premier


#print(gen_prime(2000))
