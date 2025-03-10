from udb.Util_DB import Util_DB
from interface.TK_interface import TK_interface
from beans.Contrats.Contrat_detail import Contrat_detail
import tkinter as tk


db_path = r"./base/tsena.accdb"
udb = Util_DB(db_path)
udb.connect()


# Créer la fenêtre principale
root = tk.Tk()
# Créer une instance de l'application de paiement
app = TK_interface (root, udb)
# Lancer l'interface
root.mainloop()
udb.close()

# Contrat_detail().getAll_by (9, udb)



# # # udb.execute_query("INSERT INTO locataire (nom, montant) VALUES (?, ?)", ("Dupont", 200))
# # # locataires_data = udb.fetch_all("SELECT * FROM locataire")

# # contrats = Locataire().config_data (udb)
# # print (contrats)
# # # for id_locataire, nom, montant in locataires_data : 
# # #     locataire = Locataire (id_locataire=id_locataire, nom=nom, montant_loyer=montant)
# # #     locataires.append(locataire)

# # l = Locataire(None, "rasoa", 123)
# # l.insert(udb)
# # locataires = l.get_All(udb)

# # for locataire in locataires:
# #     print(locataire)

# # # Fermer la connexion

# # locs = Locataire().get_All(udb)

# # locataires = config_data (udb)

# # def config_data (udb) : 



# # print(contrats)
# # for loc in locs :
# #     print (loc)



# # import tkinter as tk

# # Données de dépendance
# # categories = {
# #     "Fruits": ["Pomme", "Banane", "Orange"],
# #     "Légumes": ["Carotte", "Tomate", "Brocoli"],
# #     "Boissons": ["Eau", "Jus", "Café"]
# # }

# # def update_subcategories(*args):
# #     # Efface les anciennes options
# #     subcategory_var.set("")  # Réinitialise l'affichage
# #     menu = subcategory_menu["menu"]
# #     menu.delete(0, "end")

# #     # Ajoute les nouvelles options
# #     selected_category = category_var.get()
# #     if selected_category in categories:
# #         for sub in categories[selected_category]:
# #             menu.add_command(label=sub, command=lambda value=sub: subcategory_var.set(value))

# # # Création de la fenêtre principale
# # root = tk.Tk()
# # root.title("Formulaire dynamique")

# # # Définition des variables Tkinter
# # category_var = tk.StringVar()
# # subcategory_var = tk.StringVar()

# # # Liste déroulante pour la catégorie
# # tk.Label(root, text="Catégorie:").pack(pady=5)
# # category_menu = tk.OptionMenu(root, category_var, *categories.keys(), command=lambda _: update_subcategories())
# # category_menu.pack()

# # # Liste déroulante pour la sous-catégorie
# # tk.Label(root, text="Sous-Catégorie:").pack(pady=5)
# # subcategory_menu = tk.OptionMenu(root, subcategory_var, "")
# # subcategory_menu.pack()

# # # Lancement de l'interface
# # root.mainloop()


# from datetime import datetime, timedelta

# class Paiement:
#     def __init__(self, montant, date_limite):
#         self.montant = montant
#         self.date_limite = date_limite  # Date limite du paiement
#         self.date_paiement = None  # Date à laquelle la tranche est payée
#         self.pénalité = 0

#     def payer(self, date_paiement):
#         self.date_paiement = date_paiement
#         if self.date_paiement > self.date_limite:
#             self.calculer_penalite()

#     def calculer_penalite(self):
#         # Exemple de pénalité : 1% par jour de retard
#         nb_jours_retard = (self.date_paiement - self.date_limite).days
#         if nb_jours_retard > 0:
#             self.pénalité = 0.01 * nb_jours_retard * self.montant  # 1% par jour de retard
#         else:
#             self.pénalité = 0

#     def total_a_payer(self):
#         return self.montant + self.pénalité

#     def __repr__(self):
#         return f"Montant: {self.montant}€, Date limite: {self.date_limite}, Date paiement: {self.date_paiement}, Pénalité: {self.pénalité}€"

# class PaiementLoyer:
#     def __init__(self, loyer_total, date_limite_paiement, nb_tranches):
#         self.loyer_total = loyer_total
#         self.date_limite_paiement = date_limite_paiement
#         self.nb_tranches = nb_tranches
#         self.tranches = self.creer_tranches()

#     def creer_tranches(self):
#         montant_tranche = self.loyer_total / self.nb_tranches
#         tranches = []
#         for i in range(self.nb_tranches):
#             date_limite_tranche = self.date_limite_paiement + timedelta(days=i * 10)  # Par exemple, 10 jours entre chaque tranche
#             tranches.append(Paiement(montant_tranche, date_limite_tranche))
#         return tranches

#     def payer_tranche(self, index_tranche, date_paiement):
#         if 0 <= index_tranche < len(self.tranches):
#             self.tranches[index_tranche].payer(date_paiement)

#     def montant_total(self):
#         return sum([tranche.total_a_payer() for tranche in self.tranches])

#     def __repr__(self):
#         return "\n".join([str(tranche) for tranche in self.tranches])

# # Exemple d'utilisation
# date_limite_paiement = datetime(2025, 3, 1)  # Date limite pour le paiement total du loyer
# loyer = PaiementLoyer(1200, date_limite_paiement, 3)  # 1200€ en 3 tranches

# # Afficher les tranches et leurs dates limites
# print(loyer)

# # Paiement de la première tranche en retard
# loyer.payer_tranche(0, datetime(2025, 3, 5))  # Paiement avec 4 jours de retard
# loyer.payer_tranche(1, datetime(2025, 3, 2))  # Paiement à temps pour la deuxième tranche
# loyer.payer_tranche(2, datetime(2025, 3, 10))  # Paiement avec 9 jours de retard

# # Afficher l'état des paiements avec pénalités
# print("\nAprès paiement des tranches avec pénalités:")
# print(loyer)

# # Afficher le montant total à payer
# print(f"\nMontant total à payer avec pénalités: {loyer.montant_total()}€")
