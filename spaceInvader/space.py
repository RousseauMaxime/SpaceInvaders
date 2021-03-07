import pygame  # necessaire pour charger les images et les sons
import random
import math

class Joueur(pygame.sprite.Sprite):  # classe pour créer le vaisseau du joueur
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('vaisseau.png')
        self.position = 350
        self.presser = {}
        self.vie = 1
        self.score = 0

    def vies(self, extra): #méthode pour définir le game over
        if extra.hauteur >= 500 :
            self.vie -= 1
        return self.vie



    def tirer(self): # méthode tirer pour utiliser les balles
        balle = Balle(self)



    def getPosition(self): # méthode pour connaitre la position de x
        return self.position

    def deplacerDroite(self): # on déplace le personnage a +1 pixel de sa position actuelle
        self.position += 0.5
        return self.position

    def deplacerGauche(self): # on déplace le personnage a -1 pixel de sa position actuelle
        self.position -= 0.5
        return self.position




class Balle(pygame.sprite.Sprite): # classe pour créer la balle tirée par le vaisseau
    def __init__(self, player):
        super().__init__()
        self.image = pygame.image.load('balle.png')
        self.depart = player.getPosition() + 16
        self.hauteur = 470
        self.etat = ("chargee", "tiree")

    def toucher(self, extra):  # méthode pour savoir si on a toucher l'ennemi (besoin d'import math)
        p = math.sqrt(math.pow(extra.depart - self.depart, 2) + (math.pow(extra.hauteur - self.hauteur, 2)))
        if p < 26: return True
        else : return False





    def bouger(self, player):  # méthode permettant de faire bouger / de replacer la balle
        if self.etat == "chargee" :
            self.depart = player.getPosition() + 16
        if self.etat == "tiree" :
            self.hauteur -= 2.5
        if self.hauteur == 0 :
            self.hauteur = 470
            self.depart = player.getPosition() + 16
            self.etat = "chargee"
        return self.hauteur






class Ennemi(pygame.sprite.Sprite):  # class ennemis permettant d'initialiser les extraterrestres
    def __init__(self):  # définition de leur caractérisitques / attributs
        super().__init__()
        self.image = pygame.image.load("invader2.png")
        self.depart = random.randint(0,737)
        self.hauteur = random.randint(-500,0)
        self.vitesse = 0.1
        self.NbEnnemis = 4
        self.vie = 1


    def avancer(self): #méthode pour faire avancer les ennemis en fonction de leur vitesse
        self.hauteur += self.vitesse

    def disparaitre(self, tir): # méthode pour faire dispawn et spawn les ennemis
        if tir.toucher(self) is True :
            self.vie -= 1
        if self.vie <= 0 :
            self.depart = random.randint(0, 737)
            self.hauteur = random.randint(-500, 0)
