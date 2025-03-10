
class Paiement_detail :

    def __init__(self, id_paiement=None, mois=None, annee=None, payee=None, reste=None, id_box=None, id_locataire=None, id_contrat=None, date_echeance=None, debut=None) :
        self.id_paiement = id_paiement
        self.mois = mois
        self.annee = annee
        self.payee = payee
        self.reste = reste
        self.id_box = id_box
        self.id_locataire = id_locataire
        self.id_contrat = id_contrat
        self.date_echeance = date_echeance
        self.debut = debut


    
    def construct_tableau (self, data) :

        liste = []
        for id_paiement, mois, annee, payee, reste, id_contrat, id_locataire, id_box, date_echeance, debut in data :
            pd = Paiement_detail (id_paiement, mois, annee, payee, reste, id_box, id_locataire, id_contrat, date_echeance, debut)
            liste.append(pd)
        return liste 

    def construct (self, data) :
        if data : # si data n'est pas vide ![]
            id_paiement, mois, annee, payee, reste, id_contrat, id_locataire, id_box, date_echeance, debut = data[0]
            return Paiement_detail (id_paiement, mois, annee, payee, reste, id_box, id_locataire, id_contrat, date_echeance, debut)
        else : return None


    # def dernier_NONreglee (self, udb, id_locataire) :

    #     paiement_farany = None
    #     # print (f"ATO paiement farany {id_locataire}")
    #     requete = """
    #         SELECT TOP 1 *
    #         FROM paiement_detail p
    #         WHERE p.id_locataire = ? 
    #         ORDER BY p.annee ASC, p.mois ASC
    #     """
    #     params = (id_locataire)
    #     data = udb.fetch_all (requete, params)        

    #     if data:  # Vérifie si une ligne a été trouvée
    #         # print (f"{data}")
    #         id_paiement, montant_du, mois, annee, id_box, payee, reste, id_locataire, id_contrat, date_echeance = data[0]
    #         paiement_farany = Paiement_detail(id_paiement, montant_du, mois, annee, payee, reste, id_box, id_locataire, id_contrat, date_echeance)

    #     return paiement_farany



    def get_allNON_payee_par (self, id_locataire, udb) :


        requete = """
            SELECT 
                *
            FROM paiement_detail 
            WHERE id_locataire = ?
            AND reste <> 0
            ORDER BY annee ASC, mois ASC,
            debut ASC
        """
        params = (id_locataire)
        data = udb.fetch_all (requete, params)

        # print(f"{data}")
        non_payees = self.construct_tableau (data)
                
        return non_payees




    def get_allNON_payee (self, id_locataire, id_box, udb) :

        requete = """
            SELECT 
                *
            FROM paiement_detail 
            WHERE id_box = ? AND id_locataire = ?
            AND reste <> 0
            ORDER BY annee ASC, mois ASC,
            debut ASC
        """
        params = (id_box, id_locataire)
        data = udb.fetch_all (requete, params)

        # print(f"{data}")
        non_payees = self.construct_tableau (data)       
        
        return non_payees


    def __repr__(self):
        return f"- id_paiement: {self.id_paiement}\n- periode: {self.mois} {self.annee}\n- payee: {self.payee}\n- reste: {self.reste}\n- id_box: {self.id_box}\n- id_contrat: {self.id_contrat}\n- date echeance: {self.date_echeance}\n- id_locataire: {self.id_locataire}"






