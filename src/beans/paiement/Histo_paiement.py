
class Histo_paiement :
    

    def __init__(self, date_paiement, montant, id_paiement):
        self.date_paiement = date_paiement
        self.montant = montant
        self.id_paiement = id_paiement


    def insert (self, udb) :
        requete = "INSERT INTO histo_paiement (date_paiement, montant, id_paiement) VALUES (?, ?, ?)"
        params = (self.date_paiement, self.montant, self.id_paiement)
        # r = f"{requete}{params}"
        # print(r)
        udb.insert_query (requete, params)