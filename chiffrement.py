import rsa_key
import lpowmod

e, d, n=rsa_key.gen_rsa_keys(10) # Générer les clés RSA (taille de 10 chiffres pour p et q)

#Fonction de chiffrement
def encrypt(public_key: tuple[int,int], message: bytes) -> list[int]: # la clée public est un paramètre explicite
    e, n = public_key # tuple (e,n) pour gérer proprement la clée publique
    encrypted= []
    for b in message:
        encrypted.append(lpowmod.lpowmod(int(b),e,n))
    return encrypted
    
#Fonction de déchiffrement
def decrypt(private_key: tuple[int,int], encrypted_message:list[int]) -> bytes: # la clée privée est un paramètre explicite
    d, n = private_key # tuple (d,n) pour gérer proprement la clée privée
    decrypted=b""
    for b in encrypted_message:
        decrypted_byte = lpowmod.lpowmod(b, d , n)
        byte_size = (decrypted_byte.bit_lenght() + 7 // 8  # Taille en octets, la taille des octets déchiffrés est calculée dynamiquement avec bit_lenght
        decrypted += decrypted_byte.to_bytes(byte_size, "big")
    return decrypted
# Message à chiffrer
message = "bonjour" # le message "bonjour" sera chiffré en une liste de nombres

#Chiffrement et déchiffrement
public_key = (e,n)
private_key = (d,n)

encrypted_message = encrypt(public_key, message.encode("utf-8"))
decrypted_message = decrypt(private_key, ecrypted_message) # le déchiffrement permettra de retrouver le texte d'origine

print("Message initial: ", message)
print("Message chiffré: ", ecrypted_message)
print("Message déchiffré: ", decrypted_message.decode("utf-8"))



        
