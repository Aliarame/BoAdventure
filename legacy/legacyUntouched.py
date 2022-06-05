#Importation des bibliothèques nécessaires
import pygame
from pygame.locals import *
from random import *

pygame.init()

#Création de la fenêtre
fenetre = pygame.display.set_mode((450, 450), RESIZABLE)

icone = pygame.image.load("bo.png")
pygame.display.set_icon(icone)

pygame.display.set_caption("Bo Adventure")

continuer = 1 # Permet de créer une boucle infini
pas = 0 # Nombre de pas quand nous commençons le jeu
nb = randrange(10,16) # Nombre aléatoire entre 10 et 15 permettant de définir le nombre de pas à faire avant d'entrer en combat
antagoniste = 100 # Nombre de points de vie de l'ordinateur
# Statistiques du héros 
protagoniste = 100 
attaque = 20 
attaquemagie = 15
soin = 35
parade = 25

# Création de l'image du héros ainsi que sa position caractérisé par un rectangle
bo = pygame.image.load("bo.png").convert_alpha()
position_perso = bo.get_rect()

# Permet de maintenir une touche enfoncée
pygame.key.set_repeat(200, 120)


while continuer : #Boucle principale du jeu
    menu = pygame.image.load("bomenu.jpg").convert() # Variable qui correspond à l'image du menu
    fenetre.blit(menu, (0,0)) # Colle cette image en haut à gauche
    
    pygame.display.flip() # Permet de rafraîchir la fenêtre et ainsi afficher l'image
    
    # Variables permettant de créer des boucles 
    continuer_jeu = 1
    continuer_menu = 1
    combat = 0
    
    while continuer_menu : # Boucle infini permettant de quitter le jeu ou le commencer
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE: # Quitte le jeu en fermant toutes les boucles
                pygame.quit()
                continuer_menu = 0
                continuer_jeu = 0
                continuer = 0
                combat = 0
            if event.type == MOUSEBUTTONUP :
                if event.button == 1 :
                    if event.pos[0] > 110 and event.pos[0] < 341 and event.pos[1] > 288 and event.pos[1] < 333 : # Lance le jeu
                        pygame.quit()
                        continuer_menu = 0
                        continuer_jeu = 0
                        continuer = 0
                        combat = 0
                        choix = 0
                    if event.pos[0] > 109 and event.pos[0] < 341 and event.pos[1] > 201 and event.pos[1] < 247 : # Quitte le jeu
                        continuer_menu = 0
                        
    while continuer_jeu : # Boucle activée une fois le jeu lancé 
        for event in pygame.event.get(): # Comptabilise tous les évenements possibles souris et clavier
            
            if event.type == QUIT : # Correspond à la croix en haut à droite d'une fenêtre
                pygame.quit()
                continuer_jeu = 0 
                continuer = 0
                
            elif event.type == KEYDOWN: # Si l'évenement se fait au clavier
                if event.key == K_ESCAPE: 
                    continuer_jeu = 0
                
                elif event.key == K_RIGHT: #droite
                    position_perso = position_perso.move(30,0) # Déplacement vers la droite du personnage de 30 pixel
                    pas = pas+1 # Ajoute + 1 aux pas
                elif event.key == K_LEFT: #gauche
                    position_perso = position_perso.move(-30,0)
                    pas = pas +1
                elif event.key == K_UP: #haut
                    position_perso = position_perso.move(0,-30)
                    pas = pas +1
                elif event.key == K_DOWN: #bas
                    position_perso = position_perso.move(0,30)
                    pas = pas +1
                    
        fond = pygame.image.load("bofondjeu.jpg").convert() #affichage du fond 
        fenetre.blit(fond, (0,0))
        fenetre.blit(bo, position_perso)
        pygame.display.flip()
        
        if pas >= nb : #début d'un combat lorsque le personnage fait entre 10 et 15 pas
            nb = randrange(10,16)
            print ("Un combat vient de commencer !")
            print('\x1b[6;31;40m' + 'Points de vie de Bo :', protagoniste,'                Points de vie de Ab :', antagoniste,''  + '\x1b[0m') #affichage des points de vie des combattants dans la cellule (en rouge)
            pas = 0
            combat = 1
            
        while combat : #boucle du combat
            
            for event in pygame.event.get():
                
                if event.type == QUIT :
                    pygame.quit()
                    continuer_jeu = 0
                    continuer = 0
                    combat = 0
                    
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        combat = 0
                        antagoniste = 100 
                        protagoniste = 100
                    
                elif event.type == MOUSEBUTTONUP :
                    if event.button == 1 :
                        if event.pos[0] > 6 and event.pos[0] < 138 and event.pos[1] > 306 and event.pos[1] < 339 : # Si on attaque il ce passe toutes ces actions
                            
                            chance = randrange(1, 8) #nombre aléatoire entre 1 et 7 pour créer une sorte de semi intelligence artificielle
                            if chance <= 3 :
                                protagoniste = protagoniste - 20 #si le chiffre est inférieur ou égal à 3 alors l'ennemi attaque
                                print ("Ab attaque mais Bo aussi !")
                            if chance == 4 or chance == 5 :
                                protagoniste = protagoniste - 15 #si le chiffre est 4 ou 5 l'ennemi utilise un sortilège 
                                print ("Ab utilise un sort de magie et Bo attaque !")
                            if chance == 6 and antagoniste == 100 : #si le chiffre est 6 et que l'ennemi a 100 points de vie alors il ne se soigne pas mais attaque à la place 
                                protagoniste = protagoniste - 20
                                print ("Ab attaque mais Bo aussi !")
                            if chance == 6 and antagoniste < 100 :# si le chiffre est 6 est que l'ennemi a moins de 100 points de vie alors il récupère 35 point de vie  mais n'excéde pas 100
                                antagoniste = antagoniste + 35 
                                print ("Ab se soigne mais Bo attaque !")
                                if antagoniste > 100 :
                                    antagoniste = 100
                            
                            antagoniste = antagoniste - attaque # Attaque du héros sur l'ordinateur
                            
                            if chance == 7 : #si le chiffre est 7 alors l'ennemi pare et le héros subit des dégats
                                antagoniste = antagoniste + attaque
                                protagoniste = protagoniste - 25
                                print ("Ab utilise une parade et bloque les dégats de Bo et l'attaque en retour !")
                            print('\x1b[6;31;40m' + 'Points de vie de Bo :', protagoniste,'                Points de vie de Ab :', antagoniste,''  + '\x1b[0m')
                            
                        if event.pos[0] > 6 and event.pos[0] < 138 and event.pos[1] > 341 and event.pos[1] < 374 : #Si on clique sur la magie une boucle se crée et permet de choisir entre 2 actions ou de revenir pour choisir une autre action
                            combatmagie = 1
                            while combatmagie : # Affiche une image par dessus pour choisir entre les 2 actions
                                menumagie = pygame.image.load("bomagie.jpg").convert()
                                magieretour = pygame.image.load("bomagieretour.jpg").convert()
                                fenetre.blit (menumagie,(6,306))
                                fenetre.blit (magieretour,(147,306))
                                pygame.display.flip()
                                for event in pygame.event.get():
                                    if event.type == QUIT :
                                        pygame.quit()
                                        continuer_jeu = 0
                                        continuer = 0
                                        combat = 0
                                        combatmagie = 0
                                        
                                    elif event.type == MOUSEBUTTONUP : 
                                        if event.button == 1 :
                                            if event.pos[0] > 6 and event.pos[0] < 138 and event.pos[1] > 306 and event.pos[1] < 339 : # Si on utilise un sortilège il ce passe plusieurs actions 
                                                
                                                chance = randrange(1, 8) #choisit un chiffre entre 1 et 7 
                                                if chance <= 3 : #si le chiffre est inférieur ou égal à 3 alors l'ennemi attaque normalement
                                                    protagoniste = protagoniste - 20
                                                    print ("Ab attaque et Bo utilise un sort de magie !")
                                                if chance == 4 or chance == 5 : #si le chiffre est égal à 4 ou 5 alors l'ennemi utilise un sort
                                                    protagoniste = protagoniste - 15
                                                    print ("Ab utilise un sort de magie et Bo aussi !")
                                                if chance == 6 and antagoniste == 100 :  #si le chiffre est 6 et que l'ennemi a 100 points de vie alors il attaque à la place 
                                                    protagoniste = protagoniste - 20
                                                    print ("Ab attaque et Bo utilise un sort de magie !")
                                                if chance ==6 and antagoniste < 100 :  #si le chiffre est 6 et que l'ennemi a moins de 100 point de vie alors il récupère 35 point de vie mais n'excéde pas 100
                                                    antagoniste = antagoniste + 35 
                                                    print ("Ab se soigne mais Bo utilise un sort de magie !")
                                                    if antagoniste > 100 :
                                                        antagoniste = 100
                                                    
                                                antagoniste = antagoniste - attaquemagie
                                                
                                                if chance == 7 : #si le chiffre est 7 alors l'ennemi pare mais la parade devient inéfficace car nous utilisons un sort
                                                    antagoniste = antagoniste 
                                                    protagoniste = protagoniste 
                                                    print ("Ab tente une parade mais Bo utilise un sort de magie !")
                                                print('\x1b[6;31;40m' + 'Points de vie de Bo :', protagoniste,'                Points de vie de Ab :', antagoniste,''  + '\x1b[0m')
                                                combatmagie = 0
                                            
                                            if event.pos[0] > 6 and event.pos[0] < 138 and event.pos[1] > 341 and event.pos[1] < 374 : # Si on se soigne alors il ce passe plusieurs actions
                                                if protagoniste > 65 :
                                                    protagoniste = 100
                                                if protagoniste <= 65 :
                                                    protagoniste = protagoniste + soin
                                                
                                                chance = randrange(1, 8) #choisit un chiffre entre 1 et 7 
                                                if chance <= 3 : #si le chiffre est inférieur ou égal à 3 alors l'ennemi attaque
                                                    protagoniste = protagoniste - 20
                                                    print ("Bo se soigne mais Ab attaque !")
                                                if chance == 4 or chance == 5 : #si le chiffre est égal à 4 ou 5 alors l'ennemi utilise un sort
                                                    protagoniste = protagoniste - 15
                                                    print ("Bo se soigne mais Ab utilise un sort de magie !")
                                                if chance == 6 and antagoniste == 100 :  #si le chiffre est 6 et que l'ennemi a 100 points de vie alors il attaque à la place 
                                                    protagoniste = protagoniste - 20
                                                    print ("Bo se soigne mais Ab attaque !")
                                                if chance == 6 and antagoniste < 100 : #i le chiffre est 6 et que l'ennemi a moins de 100 point de vie alors il récupère 35 point de vie mais n'excéde pas 100
                                                    antagoniste = antagoniste + 35
                                                    print ("Bo se soigne et Ab aussi !")
                                                    if antagoniste > 100 :
                                                        antagoniste = 100
                                                if chance == 7 : #si le chiffre est 7 alors l'ennemi pare mais la parade devient inéfficace car nous nous soignons
                                                    antagoniste = antagoniste 
                                                    protagoniste = protagoniste
                                                    print ("Ab tente une parade mais Bo ne fait que se soigner !")
                                                    
                                                print('\x1b[6;31;40m' + 'Points de vie de Bo :', protagoniste,'                Points de vie de Ab :', antagoniste,''  + '\x1b[0m')
                                                combatmagie = 0
                                                    
                                            if event.pos[0] > 147 and event.pos[0] < 180 and event.pos[1] > 306 and event.pos[1] < 339 :
                                                combatmagie = 0
                                        
                                    
                            
                        if event.pos[0] > 6 and event.pos[0] < 138 and event.pos[1] > 376 and event.pos[1] < 409 : #Si on tente une parade il ce passe plusieurs actions
                            
                            chance = randrange(1, 8) #choisit un chiffre entre 1 et 7
                            if chance <= 3 :
                                antagoniste = antagoniste - parade #si le chiffre est inférieur ou égal à 3 alors l'ennemi attaque mais prend les dégâts car nous nous parons
                                print ("Ab attaque mais Bo pare le coup et rend les dégats à l'adversaire !")
                            if chance == 4 or chance == 5 : #si le chiffre est égal à 4 ou 5 alors l'ennemi utilise un sort et passe à traves la parade
                                protagoniste = protagoniste - 15
                                print ("Ab utilise un sort de magie et Bo se prépare à parer mais ne bloque pas le sort de magie et prend les dégats")
                            if chance == 6 and antagoniste == 100 :  #si le chiffre est 6 et que l'ennemi a 100 points de vie alors il attaque à la place mais prend des dégâts car nous nous parons 
                                antagoniste = antagoniste - parade
                                print ("Ab attaque mais Bo pare le coup et rend les dégats à l'adversaire !")
                            if chance == 6 and antagoniste < 100 :#i le chiffre est 6 et que l'ennemi a moins de 100 point de vie alors il récupère 35 point de vie mais n'excéde pas 100
                                antagoniste = antagoniste + 35
                                print ("Bo se prépare à parer mais Ab se soigne, la parade échoue !")
                                if antagoniste > 100 :
                                    antagoniste = 100
                            if chance == 7 : #si le chiffre est 7 alors l'ennemi pare alors il ne ce passe rien
                                antagoniste = antagoniste 
                                protagoniste = protagoniste 
                                print ("Ab se prépare à parer mais Bo aussi, rien ne ce passe !")
                                
                            print('\x1b[6;31;40m' + 'Points de vie de Bo :', protagoniste,'                Points de vie de Ab :', antagoniste,''  + '\x1b[0m')
                            
                        if event.pos[0] > 6 and event.pos[0] < 138 and event.pos[1] > 411 and event.pos[1] < 444 : #Si on tente de s'enfuir
                            print("Bo tente de s'enfuir...")
                            
                            chancedefuite = randrange(1, 5) #chiffre aléatoire entre 1 et 4 pour savoir si la fuite est possible
                            if chancedefuite <=3 :# Si le chiffre se situe en dessous de 3 alors la fuite réussi donc on ferme la boucle de combat et on remet les points de vie à 100 pour le prochain combat
                                print("et réussi !")
                                continuer_jeu = 1
                                combat = 0
                                antagoniste = 100
                                protagoniste = 100
                                
                            elif chancedefuite == 4 :# Si le chiffre est 4 alors la fuite est un échec et le héros subit des dégâts 
                                chance = randrange(1,6)
                                if chance <= 3 :
                                    protagoniste = protagoniste - 20
                                    print ("Mais il échoue ! Ab l'attaque alors !")
                                if chance == 4 or chance == 5 :
                                    protagoniste = protagoniste - 15
                                    print ("Mais il échoue ! Ab utilise alors un sort de magie !")
                                
                                print('\x1b[6;31;40m' + 'Points de vie de Bo :', protagoniste,'                Points de vie de Ab :', antagoniste,''  + '\x1b[0m')
                                
            pv1 = pygame.image.load("bopv1.jpg").convert() #différentes images des barres de vie
            pv2 = pygame.image.load("bopv2.jpg").convert()    
            pv3 = pygame.image.load("bopv3.jpg").convert()
            pv4 = pygame.image.load("bopv4.jpg").convert()
            pv5 = pygame.image.load("bopv5.jpg").convert()
                                    
            if antagoniste <= 0 : #si l'ennemi n'as plus de vie, fin du combat et le héros gagne un niveau
                print ("Bo gagne le combat et gagne un niveau !")
                combat = 0
                antagoniste = 100
                protagoniste = 100
                attaque = attaque + 1
                attaquemagie = attaquemagie + 1
                soin = soin + 1
                parade = parade + 1
                
            if protagoniste <= 0 : #si le héros n'as plus de vie, fin du combat
                print ("Bo perd le combat !")
                combat = 0
                antagoniste = 100
                protagoniste = 100
                  # les images de fond pour le combat
            menucombat = pygame.image.load("bofondcombat.jpg").convert() 
            fenetre.blit (menucombat, (0,0))
            bogen = pygame.image.load("bo.png").convert_alpha()
            fenetre.blit (bogen, (60,180))
            boanta = pygame.image.load("boanta.png").convert_alpha()
            fenetre.blit (boanta, (330,150))
            
            if antagoniste > 80 and antagoniste <= 100: #affichage des différentes barres de vie selon celle de l'ennemi
                fenetre.blit (pv1,(328,395))
            if antagoniste > 60 and antagoniste <= 80 :
                fenetre.blit (pv2,(328,395))
            if antagoniste > 40 and antagoniste <= 60 :
                fenetre.blit (pv3,(328,395))
            if antagoniste > 0 and antagoniste <= 40 :
                fenetre.blit (pv4,(328,395))
            if antagoniste == 0 :
                fenetre.blit (pv5,(328,395))
                
            if protagoniste > 80 and protagoniste <= 100: #affichage des différentes barres de vie selon celle du héros
                fenetre.blit (pv1,(328,350))
            if protagoniste > 60 and protagoniste <= 80 :
                fenetre.blit (pv2,(328,350))
            if protagoniste > 40 and protagoniste <= 60 :
                fenetre.blit (pv3,(328,350))
            if protagoniste > 0 and protagoniste <= 40 :
                fenetre.blit (pv4,(328,350))
            if protagoniste == 0 :
                fenetre.blit (pv5,(328,350))
                
            pygame.display.flip() #Rafraîchissement de la fenêtre pour afficher les images