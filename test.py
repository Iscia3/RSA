import json

dico={"key1":[1,2,3,4],
      "key2":2,} #la virgule a la fin ne sert a rien 
print(dico["key1"])

chaine = json.dumps(dico)
print(chaine)
print(json.loads(chaine))
