#Créé le 02/10/23
#Créé par Enzo Sanchez Valero
#TP3(Combat de monstres)

import random
import time

def jeu():

    niveau_vie = 20
    victoires = 0
    defaite = 0
    jeu()

    print('Bienvenue dans ce jeu de combat de monstres.')
    nom=str(input('Quel sera le nom de votre avatar?'))
    print('Bonne chance',nom,'.')

    while True:
        force_adversaire = random.randint(1,5)
        print('Vous tombez face à face avec un adversaire de difficulté:',force_adversaire,'')
        time.sleep(0,3)
        print('Que voulez-vous faire ?')
        choix=int(input('1 - Combattre cet adversaire \n 2 - Contourner cet adversaire et aller ouvrir une autre porte  \n 3 - Afficher les règles du jeu  \n 4 - Quitter la partie')

        if choix == 1:
            print('',nom,'')
            time.sleep(0,1)
            print('Adversaire:',numero_adversaire,'')
            print('Force de l adversaire:',force_adversaire,'')
            print('Niveau de vie:',niveau_vie,'')
            print('Combat',numero_combat,':',nb_victoire,'victoires vs', nb_defaite,'défaites')

            score_dé = random.randint(1,6)
            time.sleep(0,2)
            print('Lancer du dé:',score_dé,'')

            if score_dé > force_adversaire:
                print('Victoire!')
                niveau_vie = niveau_vie + force_adversaire
                time.sleep(0,2)
                print('',nom,' \n Niveau de vie:',niveau_vie,' \n Nombre de victoires consécutives:',nb_victoire_consec,'')
                True

            elif score_dé < force_adversaire:
                print('Défaite.')
                niveau_vie = niveau_vie - force_adversaire
                if niveau_vie <= 0:
                    print('Niveau de vie:',niveau_vie,'')
                    print('La partie est terminée.')
                    print('Vous avez vaincu',nombre_victoire,'monstre(s).')
                    break
                else:
                    True


        elif choix == 2:
            print('Vous décidez de contourner ce monstre. \n -1 vie')
            niveau_vie = niveau_vie - 1
            True

        elif choix == 3:
            print('Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.'
                  'Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire. '
                  'Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire. '
                  'Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire. La partie se termine lorsque les points de vie de l’usager tombent sous 0.'
                  'L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie')
            True

        else choix == 4:
            print('Merci et au revoir.')
            break

jeu()