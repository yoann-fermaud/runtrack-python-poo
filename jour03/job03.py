class Tache:
    def __init__(self, titre, description, status):
        self.titre = titre
        self.description = description
        self.status = status  # à faire ou termimer


class ListDeTaches:
    def __init__(self, tache):
        self.taches = tache

    def ajouter_tache(self, tache):
        if tache not in self.taches:
            self.taches.append(tache)

    def supprimer_tache(self, tache):
        if tache in self.taches:
            self.taches.remove(tache)

    def marquer_comme_finie(self, tache):
        if tache.status == "à faire":
            tache.status = "terminer"
        else:
            print(f"Tache [{tache.titre}] déjà terminer.")

    def filtre_liste(self):
        print("\nTache 'à faire':")
        for tache in self.taches:
            if tache.status == "à faire":
                print(f"[{tache.titre}]")

    def afficher_liste(self):
        print("Liste de taches:")
        for tache in self.taches:
            print(f"[{tache.titre}] {tache.description} ({tache.status});")


tache_00 = Tache("Train", "Prendre un ticket", "à faire")
tache_01 = Tache("Docteur", "Prendre un rendez-vous", "à faire")
tache_02 = Tache("Restaurant", "Réserver une table", "à faire")
tache_03 = Tache("Anniversaire", "Prendre un cadeau", "à faire")

list_tache = ListDeTaches([tache_00, tache_01, tache_02])

list_tache.ajouter_tache(tache_03)

list_tache.marquer_comme_finie(tache_02)
list_tache.marquer_comme_finie(tache_03)

list_tache.supprimer_tache(tache_02)

list_tache.afficher_liste()
list_tache.filtre_liste()
