def egcd(a, b):
    """
    Algorithme d'Euclide étendu pour calculer le PGCD  de deux nombres,
    ainsi que les coefficients de la relation de Bézout.
    """
    x,y, u,v = 0,1, 1,0  # coefficients initiaux
    while a != 0:
        q, r = b//a, b%a  # quotient et reste
        m, n = x-u*q, y-v*q # mise à jour des coefficients
        b,a, x,y, u,v = a,r, u,v, m,n # mise à jour des variables
    gcd = b
    return gcd, x, y

def modinv(a, m):
    """
    Calcul de l'inverse modulaire de 'a' modulo 'm' en utilisant l'algorithme
    d'Euclide étendu. Si l'inverse n'existe pas, la fonction retourne 'None'.
    """
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        raise ValueError(f"L'inverse modulaire n'existe pas pour {a} et {m}.")
    return x % m # Retourne l'inverse modulaire
