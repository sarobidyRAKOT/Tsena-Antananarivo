from beans.Contrats.Contrat import Contrat
from datetime import datetime


class Contrat_detail (Contrat) :

    def __init__(self, id_contrat=None, debut=None, fin=None, id_locataire=None, id_box=None, reglee=None, annee=None, mois=None) :
        
        # """ CONTRAT NON REGLEE AVEC LE PERIODE PAYEE FARANY """
        super().__init__(id_contrat, debut, fin, id_locataire, id_box, reglee)
        self.mois = mois
        self.annee = annee
    
    def construct_tableau (self, data) :

        liste = []
        for id_contrat, debut, fin, id_locataire, id_box, reglee, annee, mois in data :
            cd = Contrat_detail(id_contrat, debut, fin, id_locataire, id_box, reglee, annee, mois)
            liste.append(cd)

        return liste 
    

    def construct (self, data) :
        if data : # si data n'est pas vide ![]
            id_contrat, debut, fin, id_locataire, id_box, reglee, annee, mois = data[0]
            return Contrat_detail(id_contrat, debut, fin, id_locataire, id_box, reglee, annee, mois)
            
        else : return None




    def cheack_paiementFarany (self, udb) :

        requete = """
            SELECT *
            FROM paiement_contrat_farany
            WHERE id_locataire = ? AND id_box = ? AND id_contrat = ?
            AND annee = ? AND mois = ?
        """
        
        params = (self.id_locataire, self.id_box, self.id_contrat, self.fin.year, self.fin.month)
        data = udb.fetch_all (requete, params)
        # print (params)
        if data : return True
        else : return False



    def getAll_paiementFarany (self, id_locataire, udb) :
        
        """ RECUPERER TOUS LES CONTRAT PAR LOCATAIRE """
        requete = """
            SELECT *
            FROM paiement_contrat_farany
            WHERE id_locataire = ?
        """
        params = (id_locataire)

        data = udb.fetch_all (requete, params)
        contrats = self.construct_tableau (data)

        return contrats
