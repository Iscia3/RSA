import generer_prime as Gen
import euclide_etendu as EE

def gen_rsa_keys(length,e=65537):
    """
    Génère des clées RSA: clée publique(e,n) et clée privée (d,n).
    Arguments:
    -lenght (int) : Taille des nombres premiers en chiffres.
    -e (int) : Exposant public ( par défaut 65537 ).
    Retourne:
    -tuple: (e,d,n) avec e l'exposant public, d l'exposant privé et n le modulo
    """
    if lenght < 2:
        raise ValueError("La longueur des nombres premiers doit être au moins 2.") # vérifie que la longueur des nombres premiers est suffisante
     
    while True:
        # Générer deux nombres premiers p et q avec la fonction Gen.gen_prime
        p=int(Gen.gen_prime(length))
        q=int(Gen.gen_prime(length))

        # Eviter que p et q soient trop proches pour renforcer la sécurité
        if abs(p-q) < 10** (lenght - 1 ):
            continue
            
        n=p*q # paramètre RSA: produit des deux nombres premiers
        phi=(p-1)*(q-1) # paramètre RSA: fonction d'Euler qui calcule phi(n)

        # Vérifier que e est premier avec phi, 
        if EE.egcd(e,phi)[0] == 1:
            break
    
    # Calculer l'inverse modulaire de e modulo phi, qui est d
    d=EE.modinv(e,phi)
    if d is None:
        raise ValueError("Impossible de calculer l'inverse modulaire.") #vérifie si EE.modinv retourne une valeur valide pour éviter les erreurs lors de la génération des clées
        
    return(e,d,n)

print(gen_rsa_keys(3))


