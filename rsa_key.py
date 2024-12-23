import generer_prime as Gen
import euclide_etendu as EE

def gen_rsa_keys(length,e=65537):
    
     
    while True:
        p=int(Gen.gen_prime(length))
        q=int(Gen.gen_prime(length))
        n=p*q
        phi=(p-1)*(q-1)
        if EE.egcd(e,phi)[0] == 1:
            break

    d=EE.modinv(e,phi)
    return(e,d,n)

print(gen_rsa_keys(3))


