import random

def mot_facile(x):
  y = []
  for i in x:
    if len(i) == 4:
      y = y + [i]
  return y

def mot_moyen(x):
  y = []
  for i in x:
    if len(i) == 6:
      y = y + [i]
  return y

def mot_difficile(x):
  y = []
  for i in x:
    if len(i) == 8:
      y = y + [i]
  return y

def choix_de_la_difficulte():
  boucle = True
  while boucle :
    print("choisissez la difficulté :")
    print("1 = facile")
    print("2 = moyen")
    print("3 = dur")
    x = int(input(" : "))
    print("")
    if x == 1:
      print("#"*10," ","le mode selectionné est facile\n")
      boucle = False
    elif x == 2:
      print("#"*10," ","le mode selectionné est moyen\n")
      boucle = False
    elif x == 3:
      print("#"*10," ","le mode selectionné est dur\n")
      boucle = False
    else :
      print("merci de renseigner la bonne valeur")
  return x

def un_pendue():
  print("\n","#"*25)
  print("")
  print("")
  print("")
  print("")
  print("/")
  print("#"*25)
def deux_pendue():
  print("\n","#"*25)
  print("")
  print("")
  print("")
  print("")
  print("/ \ ")
  print("#"*25)
def trois_pendue():
  print("\n","#"*25)
  print("")
  print("")
  print("")
  print(" |")
  print("/ \ ")
  print("#"*25)
def quatre_pendue():
  print("\n","#"*25)
  print("")
  print("")
  print("--")
  print("  |")
  print(" / \ ")
  print("#"*25)
def cinq_pendue():
  print("\n","#"*25)
  print("")
  print("")
  print("-- --")
  print("  |")
  print(" / \ ")
  print("#"*25)
def six_pendue():
  print("\n","#"*25)
  print("")
  print(" ( )")
  print("-- --")
  print("  |")
  print(" / \ ")
  print("#"*25)
def sept_pendue():
  print("\n","#"*25)
  print("  |")
  print(" (X)")
  print("-- --")
  print("  |")
  print(" / \ ")
  print("#"*25)

def actualise_statut(x):
  if x == 0:
    return
  elif x == 1:
    un_pendue()
  elif x == 2:
    deux_pendue()
  elif x == 3:
    trois_pendue()
  elif x == 4:
    quatre_pendue()
  elif x == 5:
    cinq_pendue()
  elif x == 6:
    six_pendue()
  else:
    sept_pendue()
    return 1

def recherche_lettre(x,y):
  cpt = 0
  R = []
  for i in x:
    if i == y:
      print("trouvé sur l'index",cpt)
      R = R + [cpt]
      cpt = cpt + 1
  return R


def convertir_en_liste(x):
  y = []
  for i in x:
    y = y + [i]
  return y

def convertir_en_chaine(x):
  R = ""
  for i in x:
    R = R + i
  return R

def affichage_mot_cache(x):
  for i in x:
    print(i,"",end = "")

def acualisation_mot_cache(x,y,z):
  #Z = mot cache ["_","_","_"]
  #y = la lettre donné
  #x = mot a trouve ["s","a","l"]
  mot_a_trouve_listee = x
  mot_cache_liste = convertir_en_liste(z)
  cpt = 0
  for i in x:
    if i == y:
      mot_cache_liste[cpt] = x[cpt]
    cpt = cpt +1

  return convertir_en_chaine(mot_cache_liste)

####################################################################

liste = ["test","fils","salutt","bonjou","abdiquer","zerotais"]

R = True
mot_a_trouver = []
verif_len = True
nb_erreur = 0

choix = choix_de_la_difficulte()

if choix == 1:
  liste_facile = mot_facile(liste)
  mot_a_trouver = liste_facile[random.randint(0,len(liste_facile)-1)]

elif choix == 2:
  liste_moyen = mot_moyen(liste)
  mot_a_trouver = liste_moyen[random.randint(0,len(liste_moyen)-1)]

else:
  liste_difficile = mot_difficile(liste)
  mot_a_trouver = liste_difficile[random.randint(0,len(liste_difficile)-1)]

mot_cache = "".join(["_"]*len(mot_a_trouver))
mot_cache2 = mot_cache
affichage_mot_cache(mot_cache)
print(mot_a_trouver)


while R:
  
  lettre = input("\n\nMerci de renseigner une lettre\n : ")
  print("")
  verif_len = True
  while verif_len:
    if len(lettre) > 1:
      print("trooop long")
      lettre = input("\n\nMerci de renseigner une lettre\n : ")
      print("")

    else: 
      verif_len = False
  
  mot_cache = acualisation_mot_cache(mot_a_trouver,lettre,mot_cache)
  
  affichage_mot_cache(mot_cache)
  # Verification si c'est une bonne reponse

  if mot_cache == mot_cache2:
    nb_erreur = nb_erreur + 1
    print("Mauvaise reponse :(((((")
  
  mot_cache2 = mot_cache

  if actualise_statut(nb_erreur) == 1:
    R = False
    print("VOUS AVEZ PERDUUUUUEEEE")
    print("#"*30,"\n","#"*30)
  elif mot_cache == mot_a_trouver:
    print("VOUS AVEZ TROUVEEEEEEEE")
    print("#"*30,"\n","#"*30)
    R = False
