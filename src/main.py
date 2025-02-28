from udb.Util_DB import Util_DB
from beans.Locataire import Locataire
from interface.TK_interface import TK_interface
import tkinter as tk


db_path = r"D:/STADY/IT University/Semestre 4/RATTRAPAGE (Prog)/Tsena-Antananarivo/base/tsena.accdb"
udb = Util_DB(db_path)
udb.connect()

# # udb.execute_query("INSERT INTO locataire (nom, montant) VALUES (?, ?)", ("Dupont", 200))
# # locataires_data = udb.fetch_all("SELECT * FROM locataire")


# # for id_locataire, nom, montant in locataires_data : 
# #     locataire = Locataire (id_locataire=id_locataire, nom=nom, montant_loyer=montant)
# #     locataires.append(locataire)

# l = Locataire(None, "rasoa", 123)
# l.insert(udb)
# locataires = l.get_All(udb)

# for locataire in locataires:
#     print(locataire)

# # Fermer la connexion


    # Créer la fenêtre principale
root = tk.Tk()

# Créer une instance de l'application de paiement
app = TK_interface (root, udb)

# Lancer l'interface
root.mainloop()
udb.close()