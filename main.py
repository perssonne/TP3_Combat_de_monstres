#Créé le 02/10/23
#Créé par Enzo Sanchez Valero
#TP3(Combat de monstres)

# Importation des modules
import random
import time

# Définition fonction
def jeu():

    # Réinitialisation des variables
    niveau_vie = 20
    victoires = 0
    defaite = 0

    numero_adversaire = 1
    numero_combat = 1
    nb_victoire = 0
    nb_defaite = 0
    nb_victoire_consec = 0

    print('Bienvenue dans ce jeu de combat de monstres.')

    # Choix d'un pseudo
    nom=str(input('Quel sera le nom de votre avatar?'))
    print('Bonne chance',nom,'.')

    # Boucle while
    while True:
        # Boss
        if nb_victoire % 3 == 0:
            force_adversaire = random.randint(6, 11)
            time.sleep(1)
        # Adversaire normal
        else:
            force_adversaire = random.randint(1, 11)

        print('Vous tombez maintenant face à face avec un adversaire de difficulté',force_adversaire,'.')
        time.sleep(2)
        # Présentation des options
        print('')
        print('Voici vos options:')
        print(' 1 - Combattre cet adversaire '
              '\n 2 - Contourner cet adversaire et aller ouvrir une autre porte'
              '\n 3 - Afficher les règles du jeu '
              '\n 4 - Quitter la partie')
        time.sleep(2)
        # Choix d'une action
        choix=int(input('Que voulez vous faire?'))

        # Combat
        if choix == 1:
            # Informations sur l'état de l'avatar
            print('')
            print('',nom,'')
            time.sleep(2)
            print('Adversaire:',numero_adversaire,'')
            print('Force de l adversaire:',force_adversaire,'')
            print('Niveau de vie:',niveau_vie,'')
            print('Combat',numero_combat,':',nb_victoire,'victoires vs', nb_defaite,'défaites')
            print('')

            # Dés d'attaque
            premier_dé = random.randint(1, 6)
            second_dé = random.randint(1, 6)
            score_dé = premier_dé + second_dé
            time.sleep(3)
            print('Lancer du premier dé:', premier_dé,'')
            time.sleep(1)
            print('Lancer du second dé:', second_dé, '')
            time.sleep(1)
            print('Total:', score_dé,'')
            time.sleep(1)

            # En cas de victoire
            if score_dé > force_adversaire:
                print('Victoire!')
                # Mise à jour de l'état de l'avatar
                niveau_vie = niveau_vie + force_adversaire
                nb_victoire = nb_victoire + 1
                numero_combat = numero_combat + 1
                numero_adversaire = numero_adversaire + 1
                nb_victoire_consec = nb_victoire_consec + 1

                # Informations sur la progression de l'avatar
                time.sleep(2)
                print('')
                print('',nom,' \n Niveau de vie:',niveau_vie,' \n Nombre de victoires consécutives:',nb_victoire_consec,'')
                print('')
                time.sleep(2)

            # En cas de défaite
            elif score_dé <= force_adversaire:
                time.sleep(2)
                print('Défaite.')
                print('-',force_adversaire,'points de vie')
                print('')
                # Mise à jour de niveau de vie de l'avatar
                niveau_vie = niveau_vie - force_adversaire
                nb_victoire_consec = 0
                # En cas de Game Over
                if niveau_vie <= 0:
                    print('Niveau de vie:',niveau_vie,'')
                    print('La partie est terminée.')
                    print('Vous avez vaincu',nb_victoire,'monstre(s).')

                    # Sortie de la boucle
                    break
                # Si niveau de vie > 0 le jeu continue
                else:
                    # Mise à jour de l'état de l'avatar
                    combat_statut = defaite
                    nb_defaite = nb_defaite + 1
                    numero_combat = numero_combat + 1
                    numero_adversaire = numero_adversaire + 1
                    nb_victoire_consecutive = 0
                    True

        elif choix == 2:
            print('')
            print('Vous décidez de contourner ce monstre. \n -1 point de vie')
            print('')
            niveau_vie = niveau_vie - 1
            True

        elif choix == 3:
            print(''
                  '\n Règles du jeu:'
                  '\n Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.'
                  '\n Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire. '
                  '\n Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire. '
                  '\n Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire. La partie se termine lorsque les points de vie de l’usager tombent sous 0.'
                  '\n L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie'
                  '\n ')
            time.sleep(15)

            True

        elif choix == 4:
            time.sleep(1)
            print('')
            print('Merci et au revoir.')
            break

        else:
            print('')
            print('Erreur.'
                  '\nCeci n est pas une option.')
            break

jeu()

# Je pense que pour qu'il y ait deux monstres derrière chaque porte, on pourrait par exemple créer une deuxième
# variable force_adversaire. L'utilisateur pourrait alors soit les combattre les deux en même temps (il faudrait
# que le score_dé soit plus puissant que les deux force_adversaire combinée). Ou bien il devrait alors choisir
# lequel des deux il préfère combattre (en se basant sur son nom ou sur son apparence).