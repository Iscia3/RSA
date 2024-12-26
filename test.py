# En JSON, les clées et les chaînes sont toujours entourées de guillemets doubles("), alors que dans un dictionnaire Python, elles peuvent utiliser des guillemets simples(') ou doubles
import json

dico={"key1":[1,2,3,4],
      "key2":2,} #la virgule a la fin ne sert a rien 
print(dico["key1"])

chaine = json.dumps(dico) # json.dumps est utile pour écrire des données dans un fichier ou pour les envoyers à travers des réseaux
print(chaine)
print(json.loads(chaine)) # json.loads permet de lire des données JSON reçues sous forme de chaîne et de les transformer en objets Python (dictionnaire, listes,etc...)
