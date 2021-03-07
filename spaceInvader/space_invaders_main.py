import pygame # importation de la librairie pygame
import sys # pour fermer correctement l'application
import space
import random
import math


### INITIALISATION ###
# lancement des modules inclus dans pygame
pygame.init() 

# création d'une fenêtre de 800 par 600
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders")

# chargement de l image de fond
fond = pygame.image.load('background.png')


# creation du joueur
player = space.Joueur()

# creation de la balle
tir = space.Balle(player)
tir.etat = "chargee"

# creation des ennemis
extra = space.Ennemi()
listeEnnemis = []
for indice in range(extra.NbEnnemis):
    listeEnnemis.append(space.Ennemi())



### BOUCLE DE JEU  ###
running = True # variable pour laisser la fenêtre ouverte

while running : # boucle infinie pour laisser la fenêtre ouverte
    # dessin du fond

    screen.blit(fond,(0,0))

    # vérifier si le joueur veut aller à droite ou à gauche
    if tir.etat == "chargee":
        if player.presser.get(pygame.K_RIGHT) and player.getPosition() < 737:  # on vérifie si la touche droite et activée + on vérifie la limite
            player.deplacerDroite() # on active la méthode pour déplacer a droite
        elif player.presser.get(pygame.K_LEFT) and player.getPosition() > 0:  # on vérifie si la touche gauche et activée + on vérifie la limite
            player.deplacerGauche()  # on active la méthode pour déplacer a gauche

    ### Gestion des événements  ###
    for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
        if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
            running = False # running est sur False
            sys.exit() # pour fermer correctement


       
       # gestion du clavier
        if event.type == pygame.KEYDOWN : # si une touche a été tapée
            player.presser[event.key] = True # touche activée

            if event.key == pygame.K_SPACE:  # espace pour tirer
                player.tirer()
                tir.etat = "tiree"

        elif event.type == pygame.KEYUP : # si une touche n'est plus tapée
            player.presser[event.key] = False # touche plus activée

    ### Actualisation de la scene ###

    # Gestions des collisions
    for extra in listeEnnemis:
        if tir.toucher(extra) :
            extra.disparaitre(tir)
            tir.depart = player.getPosition() + 16
            tir.hauteur = 470
            tir.etat = "chargee"
            player.score += 1


    # deplacement des objets
    tir.bouger(player)

    # dessins des objets
    screen.blit(tir.image, [tir.depart, tir.hauteur])  # appel de la fonction qui dessine le vaisseau du joueur
    screen.blit(player.image, (player.getPosition(), 500))  # dessine le joueur à la position donné

    # les ennemis
    for extra in listeEnnemis:
        extra.avancer()
        screen.blit(extra.image,[extra.depart, extra.hauteur])  # appel de la fonction qui dessine le vaisseau du joueur
        if player.vies(extra) <= 0 :
            print("Game Over")
            print("Votre score est de :", player.score,"points")
            running = False
            sys.exit()



    pygame.display.update() # pour mettre à jour l'écran