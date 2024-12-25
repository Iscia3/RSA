import subprocess

def is_prime(n):
    """
    Vérifie si un nombre est premier en utilisant la commmande OpenSSL.
    Arguments:
    - n (int) : Le nombre à vérifier.
    Retourne:
    - bool: True si le nombre est premier, False sinon.
    """
    if not isinstance(n,int) or n <= 1: # vérifie que l'entrée est un entier strictement supérieur à 1
        raise ValueError("L'entrée doit être un entier positif supérieur à 1.")
        
    commande=f"openssl prime {n}"
    try:
        # Exécution de la commande OpenSSL
        r= subprocess.run(commande,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
        #pour recupérer la sortie d'une commande
        resultat_openssl= r.stdout.decode('utf-8').strip() # strip() est utilisé pour éliminer les espaces superflus autour de la sortie

        # Vérification du résultat
        return "is prime" in resultat_openssl
    except FileNotFoundError:
        raise EnvironmentError("La commande 'openssl'  n'est pas disponible. Veuillez prendre le temps de l'installer.")
    except Exception as e:
        raise RuntimeError(f"Une erreur est survenue lors de l'exécution: {e}")
    
#print(is_prime(391))
