import subprocess

def is_prime(n):
    commande="openssl prime"
    r= subprocess.run(commande+str(" ")+str(n),shell=True, stdout=subprocess.PIPE) 
    #pour recupérer la sortie d'une commande
    resultat_openssl= r.stdout.decode('utf-8')
    
    if "not" in resultat_openssl:
        return False
    else : 
        return True
    
#print(is_prime(391))
