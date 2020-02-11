# coding : utf-8
# Travail fait par Jessica Potsou

# Premièrement, je vais importer les outils csv, json et requests.
import csv
import json
import requests

# Deuxièmement je donne déjà un nom au fichier que je vais produire
fichier = "lobbying.csv"

# J'intègre le lien de l'api maison que je vais utiliser pour ce travail
apiMaison = "http://jhroy.ca/uqam/lobby.json"

# Je vais créer un entete pour que ma demande indique mes informations
entetes = {
    "User-Agent": "Jessica Potsou - requête envoyée dans le cadre d'un cours de journalisme de données",
    "From":"potsou.jessica@courrier.uqam.ca"
}

# Je vérifie si ma demande fonctionne avec les codes des deux prochains commentaires
# req = requests.get(apiMaison, headers=entetes)
# print (req)
# Ma demande fonctionne puisque j'ai eu le code de réponse [200]


#Je me fait une variable égale à zéro à laquelle j'utiliserai la fonction += plus tard pour l'augmenter de 1 à chaque fois que ça arrive
n = 0
#Je fais une liste vide à laquelle je vais ajouter mes informations plus tard
info = []

#Je dois ensuite faire une
for nb in range(0,72001):
    n += 1
    req = requests.get(apiMaison, headers=entetes)
    obj = req.json()
    #Avec les deux lignes suivantes j'ajoute les valeurs n et nb à ma liste
    info.append(n)
    info.append(nb)
    #Ensuite je fais mes conditions ainsi que les valeurs que je souhaite afficher lorsqu'elles sont remplis
    if "limat" in obj["registre"][0][1][0]["objet"]:
       l1 = {
           'num' : obj["registre"][0][0]["client_org_corp_num"],
           'nom' : obj["registre"][0][0]["fr_client_org_corp_nm"],
           'name' : obj["registre"][0][0]["en_client_org_corp_nm"],
           'date' : obj["registre"][0][0]["date_comm"],
           'sujet principal' : obj["registre"][0][1][0]["objet"],
           'sujet autre' : obj["registre"][0][1][0]["objet_autre"],
           'institution' : obj["registre"][0][2][0]["institution"],
       }
    elif "limat" in obj["registre"][0][1][1]["objet"]:
        l2 = {
            'num' : obj["registre"][0][0]["client_org_corp_num"],
            'nom' : obj["registre"][0][0]["fr_client_org_corp_nm"],
            'name' : obj["registre"][0][0]["en_client_org_corp_nm"],
            'date' : obj["registre"][0][0]["date_comm"],
            'sujet principal' : obj["registre"][0][1][1]["objet"],
            'sujet autre' : obj["registre"][0][1][1]["objet_autre"],
            'institution' : obj["registre"][0][2][0]["institution"],
        }
    elif "limat" in obj["registre"][0][1][2]["objet"]:
        l3 = {
            'num' : obj["registre"][0][0]["client_org_corp_num"],
            'nom' : obj["registre"][0][0]["fr_client_org_corp_nm"],
            'name' : obj["registre"][0][0]["en_client_org_corp_nm"],
            'date' : obj["registre"][0][0]["date_comm"],
            'sujet principal' : obj["registre"][0][1][2]["objet"],
            'sujet autre' : obj["registre"][0][1][2]["objet_autre"],
            'institution' : obj["registre"][0][2][0]["institution"],
        }
        #Je n'ai pas fait de condition avec la clé objet_autre puisqu'en général, c'est toujours la même chose que pour la clé objet
        #Avec les trois prochaine lignes de codes j'ajoute les valeurs de mes conditions à ma liste
        info.append(l1)
        info.append(l2)
        info.append(l3)

        #Avec les trois dernières lignes je procède à la création de mon fichier csv dans lequel je mets ma liste
        c1 = open(fichier, "a")
        c2 = csv.writer(c1)
        c2.writerow(info)
