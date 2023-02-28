class Commande:
    def __init__(self, num_commande, status):
        self.__num_commande = num_commande
        self.__status = status
        self.__plats = {}
        self.__prix_plats = {
            "Pizza trois frommages": 7.99,
            "Tacos 2 viandes": 9.99,
            "Coca-Cola": 1.99,
            "Ice-Tea": 1.99
        }
        self.__statut = "en cours"

    def ajouter_plat(self, nom_plat):
        if nom_plat in self.__prix_plats:
            self.__plats[nom_plat] = {"prix": self.__prix_plats[nom_plat], "status": self.__status}

    def __calculer_total(self):
        total = 0
        for plat in self.__plats.values():
            if plat["status"] == "en cours":
                total += plat["prix"]
        return total

    def __calculer_TVA(self):
        total = self.__calculer_total()
        TVA = format(total * 20 / 100, ".2f")
        print(f"TVA à payer: {TVA} euros\n")

    def afficher_commande(self):
        print(f"Commande numéro {self.__num_commande}")
        for nom_plat, plat in self.__plats.items():
            print(f"{nom_plat} : {plat['prix']} euros ({plat['status']})")
        print(f"Total : {self.__calculer_total()} euros (TVA incluse)")
        self.__calculer_TVA()


commande_01 = Commande(1, "en cours")
commande_01.ajouter_plat("Pizza trois frommages")
commande_01.ajouter_plat("Coca-Cola")
commande_01.afficher_commande()

commande_02 = Commande(2, "annulée")
commande_02.ajouter_plat("Tacos 2 viandes")
commande_02.ajouter_plat("Ice-Tea")
commande_02.afficher_commande()
