

from datetime import datetime
from dateutil.relativedelta import relativedelta


class Histo_paiement :
    

    def __init__(self, date_paiement, montant, id_paiement, penalite):
        self.date_paiement = date_paiement
        self.montant = montant
        self.id_paiement = id_paiement
        self.penalite = penalite


    def insert (self, udb) :

        # INSETION AVER
        requete = """
            INSERT INTO histo_paiement (date_paiement, montant, penalite, id_paiement) 
            VALUES (?, ?, ?, ?)
        """

        params = (self.date_paiement, self.montant, self.penalite, self.id_paiement)
        # print (f"{params}\n")
        # print(r)
        udb.insert_query (requete, params)

