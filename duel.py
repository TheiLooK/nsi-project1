# ─────────────────────────────────────────────────────────────────────────────────────────────────────────────
# ─██████████████─████████████████───██████████████─────────██████─██████████████─██████████████────████████───
# ─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─────────██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██────██░░░░██───
# ─██░░██████░░██─██░░████████░░██───██░░██████░░██─────────██░░██─██░░██████████─██████░░██████────████░░██───
# ─██░░██──██░░██─██░░██────██░░██───██░░██──██░░██─────────██░░██─██░░██─────────────██░░██──────────██░░██───
# ─██░░██████░░██─██░░████████░░██───██░░██──██░░██─────────██░░██─██░░██████████─────██░░██──────────██░░██───
# ─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░██──██░░██─────────██░░██─██░░░░░░░░░░██─────██░░██──────────██░░██───
# ─██░░██████████─██░░██████░░████───██░░██──██░░██─██████──██░░██─██░░██████████─────██░░██──────────██░░██───
# ─██░░██─────────██░░██──██░░██─────██░░██──██░░██─██░░██──██░░██─██░░██─────────────██░░██──────────██░░██───
# ─██░░██─────────██░░██──██░░██████─██░░██████░░██─██░░██████░░██─██░░██████████─────██░░██────────████░░████─
# ─██░░██─────────██░░██──██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─────██░░██────────██░░░░░░██─
# ─██████─────────██████──██████████─██████████████─██████████████─██████████████─────██████────────██████████─
# ─────────────────────────────────────────────────────────────────────────────────────────────────────────────
#  ____   __                                    _   _      
# |___ \  \_\                                  | | (_)     
#   __) | ___ _ __ ___   ___   _ __   __ _ _ __| |_ _  ___ 
#  |__ < / _ \ '_ ` _ \ / _ \ | '_ \ / _` | '__| __| |/ _ \
#  ___) |  __/ | | | | |  __/ | |_) | (_| | |  | |_| |  __/
# |____/ \___|_| |_| |_|\___| | .__/ \__,_|_|   \__|_|\___|
#                             | |                          
#                             |_|                          

from turtle import*
from random import randint
setup(1100,500)
speed("fastest")
hideturtle()
up()



# ----------------------------------------------------------------------------------------------------
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ Fonctions ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ----------------------------------------------------------------------------------------------------


def carré(x,y,c): # Cette fonction fait le carré qui trace les contours du dé
	goto(x,y)
	down()
	for i in range(4):
		forward(c)
		left(90)
	up()


def point(x,y,c): # Cette fonction dessine un point
	begin_fill()
	carré(x,y,c)
	end_fill()


def lanceDé(): # Cette fonction lance le dé et renvoi le numéro sur lequel il tombe
	n = randint(1,6)
	return n

def grandRectangle(): # Cette fonction fait un grand carré  pour définir la zone ou l'on va afficher les informations
	goto(-500,-200) # En bas à gauche
	down()
	goto(500,-200) # En haut à gauche
	goto(500,200) # En haut à droite
	goto(-500,200) # En bas à droite
	goto(-500,-200) # En bas à gauche (retour au point de départ)
	up()

def joueurUn(): # Texte Joueur 1
	goto(-250,150) 
	write(joueur1,
		align="center",
		font=("Arial",30,"bold"))

def joueurDeux(): # Texte Joueur 2
	goto(250,150) 
	write(joueur2,
		align="center",
		font=("Arial",30,"bold"))

def préparation(): # Cette fonction fait toute la préparation nécessaire au jeu :
	grandRectangle() # Trace le contour
	carré(-355,-70,210) # Carré du dé joueur 1
	carré(145,-70,210) # Carré du dé joueur 2



# ----------------------------------------------------------------------------------------------------
# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ Fonctions ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
# ----------------------------------------------------------------------------------------------------



# ----------------------------------------------------------------------------------------------------
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ Ces fonctions créent les faces des dés avec leurs numéros respectifs ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ----------------------------------------------------------------------------------------------------


def dé1(x,y):
	"le dé avec le numéro 1"
	point(x+90,y+90,30)


def dé2(x,y):
	"le dé avec le numéro 2"
	point(x+150,y+150,30)
	point(x+30,y+30,30)


def dé3(x,y):
	"le dé avec le numéro 3"
	dé1(x,y)
	dé2(x,y)


def dé4(x,y):
	"le dé avec le numéro 4"
	dé2(x,y)
	point(x+30,y+150,30)
	point(x+150,y+30,30)


def dé5(x,y):
	"le dé avec le numéro 5"
	dé1(x,y)
	dé4(x,y)	


def dé6(x,y):
	"le dé avec le numéro 6"
	dé4(x,y)
	point(x+30,y+90,30)
	point(x+150,y+90,30)



# ----------------------------------------------------------------------------------------------------
# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ Ces fonctions créent les faces des dés avec leurs numéros respectifs ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
# ----------------------------------------------------------------------------------------------------



# ----------------------------------------------------------------------------------------------------
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ Programme ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ----------------------------------------------------------------------------------------------------


préparation()
#       _                               __ 
#      | |                             /_ |
#      | | ___  _   _  ___ _   _ _ __   | |
#  _   | |/ _ \| | | |/ _ \ | | | '__|  | |
# | |__| | (_) | |_| |  __/ |_| | |     | |
#  \____/ \___/ \__,_|\___|\__,_|_|     |_|
# Le joueur 1 doit appuyer sur une touche pour lancer son dé


joueur1 = input("Entrez le nom du joueur 1 puis appuyez sur [entrer] pour lancer le dé : ")

while len(joueur1) > 16 : # Si le nom du joueur est trop long, il sera redemandé jusqu'à ce qu'il soit assez court
	joueur1 = input("Votre prénom est trop long, essayez un prénom plus court : ")


if joueur1 == "" or joueur1.count(" ") > 0 :
	joueur1 = "Joueur 1"

else :
	joueur1 = joueur1.capitalize()


joueurUn() # Texte Joueur 1
lancéJoueur1 = lanceDé()

x = -355
y = -70

if lancéJoueur1 == 1 :
	dé1(x,y)

elif lancéJoueur1 == 2 :
	dé2(x,y)

elif lancéJoueur1 == 3 :
	dé3(x,y)

elif lancéJoueur1 == 4 :
	dé4(x,y)

elif lancéJoueur1 == 5:
	dé5(x,y)

else :
	dé6(x,y)




#       _                               ___  
#      | |                             |__ \ 
#      | | ___  _   _  ___ _   _ _ __     ) |
#  _   | |/ _ \| | | |/ _ \ | | | '__|   / / 
# | |__| | (_) | |_| |  __/ |_| | |     / /_ 
#  \____/ \___/ \__,_|\___|\__,_|_|    |____|
# Le joueur 2 doit appuyer sur une touche pour lancer son dé


joueur2 = input("Entrez le nom du joueur 2 puis appuyez sur [entrer] pour lancer le dé : ")

while len(joueur2) > 16 : # Si le nom du joueur est trop long, il sera redemandé jusqu'à ce qu'il soit assez court
	joueur2 = input("Votre prénom est trop long, essayez un prénom plus court : ")


if joueur2 == "" or joueur2.count(" ") > 0 :
	joueur2 = "Joueur 2"

else :
	joueur2 = joueur2.capitalize()


joueurDeux() # Texte Joueur 2
lancéJoueur2 = lanceDé()

x = 145
y = -70

if lancéJoueur2 == 1 :
	dé1(x,y)

elif lancéJoueur2 == 2 :
	dé2(x,y)

elif lancéJoueur2 == 3 :
	dé3(x,y)

elif lancéJoueur2 == 4 :
	dé4(x,y)

elif lancéJoueur2 == 5:
	dé5(x,y)

else :
	dé6(x,y)



#   _____                               _   
#  / ____|                             | |  
# | |  __  __ _  __ _ _ __   __ _ _ __ | |_ 
# | | |_ |/ _` |/ _` | '_ \ / _` | '_ \| __|
# | |__| | (_| | (_| | | | | (_| | | | | |_ 
#  \_____|\__,_|\__, |_| |_|\__,_|_| |_|\__|
#                __/ |                      
#               |___/                       


if lancéJoueur1 == lancéJoueur2 : # Dans le cas ou c'est une égalité
	goto(0,-180)
	write("Match nul !",
		align="center",
		font=("Arial",50,"bold"))

	pencolor("orange")
	joueurUn()
	joueurDeux()
	carré(-355,-70,210) # Carré du dé joueur 1
	carré(145,-70,210) # Carré du dé joueur 2

elif lancéJoueur1 > lancéJoueur2 : # Dans le cas bou le joueur 1 gagne
	goto(0,-180)
	write(joueur1+" a gagné !",
		align="center",
		font=("Arial",40,"bold"))

	pencolor("green")
	joueurUn()
	carré(-355,-70,210) # Carré du dé joueur 1

	pencolor("red")
	joueurDeux()
	carré(145,-70,210) # Carré du dé joueur 2

else : # Dans le cas ou le joueur 2 gagne
	goto(0,-180)
	write(joueur2+" a gagné !",
		align="center",
		font=("Arial",40,"bold"))

	pencolor("green")
	joueurDeux()
	carré(145,-70,210) # Carré du dé joueur 2

	pencolor("red")
	joueurUn()
	carré(-355,-70,210) # Carré du dé joueur 1



# ----------------------------------------------------------------------------------------------------
# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ Programme ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
# ----------------------------------------------------------------------------------------------------
