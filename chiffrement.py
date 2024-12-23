import rsa_key
import lpowmod

e, d, n=rsa_key.gen_rsa_keys(10)


def encrypt(public_key, message :bytes) -> list[int]:
    L=[]
    for b in message:
        L.append(lpowmod.lpowmod(int(b),e,n))
    return L

def decrypt(private_key, message_crypted:list[int]) -> bytes:
    result=b""
    for b in message_crypted:
      B=lpowmod.lpowmod(b,d,n)
      byte = B.to_bytes(1,"little")
      result+=byte
    return result

mot="bonjour"       
code=decrypt(d,encrypt(e,mot.encode("utf-8")))
print(code.decode("utf-8"))



        
