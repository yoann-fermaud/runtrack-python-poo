class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.tva = TVA

    def calculer_prix_TTC(self):
        return format(self.prixHT * (1 + (20 / 100)), ".2f")

    def modifier_nom_produit(self, nom):
        self.nom = nom
        return self.nom

    def modifier_prix_produit(self, prixHT):
        self.prixHT = prixHT
        return self.prixHT

    def afficher_nom(self):
        return self.nom

    def afficher_prix(self):
        return self.prixHT

    def afficher(self):
        return self.nom, self.calculer_prix_TTC(), self.tva


produit_01 = Produit("Switch", 291.66, 20)
produit_02 = Produit("PS4", 283.33, 20)

print("Avant changement de nom et de prix :")
print(f"Informations du produit '{produit_01.nom}', nom, prix, tva : ", produit_01.afficher())
print(f"Informations du produit '{produit_02.nom}', nom, prix, tva : ", produit_02.afficher())

produit_01.modifier_nom_produit("Switch Oled")
produit_01.modifier_prix_produit(299.99)
produit_02.modifier_nom_produit("PS4 Slim")
produit_02.modifier_prix_produit(289.99)

print("\nAprès changement de nom et de prixHT :")
print(f"Produit 1 : {produit_01.nom}, {produit_01.prixHT}")
print(f"Produit 2 : {produit_02.nom}, {produit_02.prixHT}")
print(f"Informations du produit '{produit_01.nom}', nom, prix, tva : ", produit_01.afficher())
print(f"Informations du produit '{produit_02.nom}', nom, prix, tva : ", produit_02.afficher())
