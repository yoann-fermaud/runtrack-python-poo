class Joueur:
    def __init__(self, nom, numero, position, nb_buts, nb_passe_d, carton_jaune, carton_rouge):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.nb_buts, self.nb_passe_d = nb_buts, nb_passe_d
        self.carton_jaune, self.carton_rouge = carton_jaune, carton_rouge

    def marquer_but(self):
        self.nb_buts += 1
        return self.nb_buts

    def effectuer_passe_decisive(self):
        self.nb_passe_d += 1
        return self.nb_passe_d

    def recevoir_carton_jaune(self):
        self.carton_jaune += 1
        return self.carton_jaune

    def recevoir_carton_rouge(self):
        self.carton_rouge += 1
        return self.carton_rouge

    def afficher_statistiques(self):
        print(f"______________________________"
              f"\nNom: {self.nom}"
              f"\nNuméro: {self.numero}"
              f"\nPosition: {self.position}"
              f"\nNombre de buts: {self.nb_buts}"
              f"\nNombre de passes décisives: {self.nb_passe_d}"
              f"\nNombre de carton jaune: {self.carton_jaune}"
              f"\nNombre de carton rouge: {self.carton_rouge}")


class Equipe:
    def __init__(self, nom, joueurs):
        self.nom = nom
        self.joueurs = joueurs

    def ajouter_joueur(self, joueur):
        if joueur not in self.joueurs:
            self.joueurs.append(joueur)

    def afficher_statistiques_joueurs(self):
        for joueur in self.joueurs:
            joueur.afficher_statistiques()

    def mettre_a_jour_statistiques_joueurs(self):
        print("\nMise à jour des statistiques")
        self.afficher_statistiques_joueurs()


# Composition équipe numéro 1
joueur_00 = Joueur("Yoann", 1, "Gardien", 0, 0, 0, 0)
joueur_01 = Joueur("Zoé", 5, "Libéro", 0, 0, 0, 0)
joueur_02 = Joueur("Lucas", 11, "Attaquant", 0, 0, 0, 0)
joueur_03 = Joueur("Gauthier", 12, "Remplaçant", 0, 0, 0, 0)

# Composition équipe numéro 2
joueur_04 = Joueur("Nathan", 1, "Gardien", 0, 0, 0, 0)
joueur_05 = Joueur("Clément", 5, "Libéro", 0, 0, 0, 0)
joueur_06 = Joueur("Elie", 11, "Attaquant", 0, 0, 0, 0)
joueur_07 = Joueur("Léo", 12, "Remplaçant", 0, 0, 0, 0)

# Création des deux équipes
equipe_00 = Equipe("Equipe 0", [joueur_00, joueur_01, joueur_02])
equipe_01 = Equipe("Equipe 1", [joueur_04, joueur_05, joueur_06, joueur_07])

# Appelle des méthodes d'une équipe pour effectuer un "match"
equipe_00.afficher_statistiques_joueurs()
equipe_00.ajouter_joueur(joueur_03)

joueur_01.effectuer_passe_decisive()
joueur_02.marquer_but()

joueur_01.recevoir_carton_jaune()
joueur_01.recevoir_carton_rouge()

equipe_00.mettre_a_jour_statistiques_joueurs()
