
class Paiement_detail :

    def __init__(self, id_paiement=None, montant=None, mois=None, annee=None, payees=None, reste=None, id_box=None) :
        self.id_paiement = id_paiement
        self.montant = montant
        self.mois = mois
        self.annee = annee
        self.payees = payees
        self.reste = reste
        self.id_box = id_box


    def get_paiement_farany (self, udb, id_box) :

        paiement_farany = None
        # print (f"ATO paiement farany {id_box}")
        requete = "SELECT TOP 1 * FROM paiement_detail WHERE id_box = ? ORDER BY p.mois ASC, p.annee ASC"
        params = (id_box)
        data = udb.fetch_all (requete, params)

        for id_paiement, montant, mois, annee, id_box, payees, reste in data :
            paiement_farany = Paiement_detail(id_paiement, montant, mois, annee, payees, reste, id_box)
        
        return paiement_farany

    def get_allApayee (self, udb, id_box) :

        a_payee = []

        requete = "SELECT * FROM paiement_detail WHERE id_box = ? ORDER BY p.mois ASC, p.annee ASC"
        params = (id_box)
        data = udb.fetch_all (requete, params)

        for id_paiement, montant, mois, annee, id_box, payees, reste in data :
            ap = Paiement_detail(id_paiement, montant, mois, annee, payees, reste, id_box)
            a_payee.append(ap)
        
        return a_payee







