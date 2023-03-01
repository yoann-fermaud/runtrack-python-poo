class CompteBancaire:
    def __init__(self, num_compte, nom, prenom, solde, decouvert):
        self.__num_compte = num_compte
        self.__nom, self.__prenom = nom, prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Numéro de compte: {self.__num_compte}"
              f"\nNom: {self.__nom}"
              f"\nPrénom: {self.__prenom}")

    def afficher_solde(self):
        print(f"Solde de M. {self.__nom} {self.__prenom}: {self.__solde}")

    def agios(self):
        if self.__solde < 0:
            #  Le nombre débiteur du premier découvert est de self.__solde * jours
            self.__solde += ((self.__solde * 10) * 20) / (365 * 100)
            print(self.__solde)

    def virement(self, beneficiaire, montant):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
            beneficiaire.__solde += montant
            print(f"Virement de {montant} euros de M. {self.__nom} {self.__prenom} "
                  f"vers le compte {beneficiaire.__nom} {beneficiaire.__prenom} éffectué")
        else:
            print("Votre solde est insuffisant, "
                  "veillez à ce que votre compte bancaire possède bien le montant sélectionné")

    def versement(self, montant):
        self.__solde += montant
        print(f"Après versement votre solde est de {self.__solde}, n°{self.__num_compte}")
        return self.__solde

    def retrait(self, montant: int):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
            print(f"Après retrait votre solde est de {self.__solde}, n°{self.__num_compte}")
            return self.__solde
        else:
            print("Votre solde est insuffisant, "
                  "veillez à ce que votre compte bancaire possède bien le montant sélectionné")


compte_00 = CompteBancaire("07072022", "Fermaud", "Yoann", 460, False)
compte_01 = CompteBancaire("07072222", "Fermaud", "Lucas", 460, True)
compte_00.afficher()
compte_01.afficher()

compte_00.versement(233)
compte_01.retrait(693)
compte_00.afficher_solde()
compte_01.afficher_solde()

compte_00.virement(compte_01, 433)
compte_00.afficher_solde()
compte_01.afficher_solde()
