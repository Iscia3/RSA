#cette méthode est moins coûteuse, car au lieu de calculer x**y directement puis de prendre le modulo, elle réduit l'exposant par division par 2 à chaque étape donc le coût est logarthmique par rapport à y. Elle est très utile pour les algorithmes cryptographiques comme rsa, car les exposants sont souvents très grands
def lpowmod(x, y, n):
    """
    Calcule de la puissance modulaire: (x**y)%n avec x, y et n entiers.
    Utilise l'exponentiation rapide pour une efficacité importante.
    Arguments:
    - x (int) : Base.
    - y (int) : Exposant ( non négatif ).
    - n (int) : Modulo ( strictement positif).
    Retourne:
    - int : Le résultat de (x**y)%n.
    """
    if y < 0 or n <= 0:
        raise ValueError("L'exposant doit être non négatif et le modulo strictement positif.")
        
    result = 1 # Initialisation du résultat
    x = x%n # Réduction initiale de x modulo n 
    while y>0:
        if y&1>0: # Vérifie si y est impair
            result = (result*x)%n # Multiplie le résultat par la base réduite
        y >>= 1 # Division entière de y par 2 ( décalage binaire ) 
        x = (x*x)%n # Mise à jour de la base  pour la prochaine itération
    return result
