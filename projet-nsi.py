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
		right(90)
	up()


def point(x,y,c): # Cette fonction dessine un point
	goto(x,y)
	begin_fill()
	for i in range(4):
		forward(c)
		right(90)
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
	write("Joueur 1",
		align="center",
		font=("Arial",30,"bold"))

def joueurDeux(): # Texte Joueur 2
	goto(250,150) 
	write("Joueur 2",
		align="center",
		font=("Arial",30,"bold"))

def préparation(): # Cette fonction fait toute la préparation nécessaire au jeu :
	grandRectangle() # Trace le contour
	joueurUn()
	joueurDeux()
	carré(-355,140,210) # Carré du dé joueur 1
	carré(145,140,210) # Carré du dé joueur 2



# ----------------------------------------------------------------------------------------------------
# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ Fonctions ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
# ----------------------------------------------------------------------------------------------------



# ----------------------------------------------------------------------------------------------------
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ Ces fonctions créent les faces des dés avec leurs numéros respectifs ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ----------------------------------------------------------------------------------------------------


def dé1(x,y):
	"le dé avec le numéro 1"
	point(x+90,y+120,30)


def dé2(x,y):
	"le dé avec le numéro 2"
	point(x+150,y+180,30)
	point(x+30,y+60,30)


def dé3(x,y):
	"le dé avec le numéro 3"
	dé1(x,y)
	dé2(x,y)


def dé4(x,y):
	"le dé avec le numéro 4"
	dé2(x,y)
	point(x+30,y+180,30)
	point(x+150,y+60,30)


def dé5(x,y):
	"le dé avec le numéro 5"
	dé1(x,y)
	dé4(x,y)	


def dé6(x,y):
	"le dé avec le numéro 6"
	dé4(x,y)
	point(x+30,y+120,30)
	point(x+150,y+120,30)



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


joueur1 = input("Joueur 1 : Appuyez sur [entrer] pour lancer le dé :")
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


joueur2 = input("Joueur 2 : Appuyez sur [entrer] pour lancer le dé :")
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
	carré(-355,140,210) # Carré du dé joueur 1
	carré(145,140,210) # Carré du dé joueur 2

elif lancéJoueur1 > lancéJoueur2 : # Dans le cas ou le joueur 1 gagne
	goto(0,-180)
	write("Le joueur 1 gagne !",
		align="center",
		font=("Arial",50,"bold"))

	pencolor("green")
	joueurUn()
	carré(-355,140,210) # Carré du dé joueur 1

	pencolor("red")
	joueurDeux()
	carré(145,140,210) # Carré du dé joueur 2

else : # Dans le cas ou le joueur 2 gagne
	goto(0,-180)
	write("Le joueur 2 gagne !",
		align="center",
		font=("Arial",50,"bold"))

	pencolor("green")
	joueurDeux()
	carré(145,140,210) # Carré du dé joueur 2

	pencolor("red")
	joueurUn()
	carré(-355,140,210) # Carré du dé joueur 1



# ----------------------------------------------------------------------------------------------------
# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ Programme ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
# ----------------------------------------------------------------------------------------------------
