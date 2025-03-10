

from beans.Box import Box

class Contrat :

    def __init__(self, id_contrat=None, debut=None, fin=None, id_locataire=None, id_box=None, reglee=None):
        
        self.id_contrat = id_contrat
        self.debut = debut
        self.fin = fin
        self.id_locataire = id_locataire
        self.id_box = id_box
        self.reglee = reglee


    def construct_tableau (self, data) :

        liste = []
        for id_contrat, debut, fin, id_locataire, id_box, reglee in data :
            cd = Contrat (id_contrat, debut, fin, id_locataire, id_box, reglee)
            liste.append(cd)
        return liste 
    
    
    def construct (self, data) :
        if data : # si data n'est pas vide ![]
            id_contrat, debut, fin, id_locataire, id_box, reglee = data[0]
            return Contrat (id_contrat, debut, fin, id_locataire, id_box, reglee)
        else : return None

    


    def get_by (self, id_locataire, id_box, udb) :
        
        # CONTRAT PLUS ANCIENT NON REGLEE 
        requete = """
            SELECT TOP 1
                c.*
            FROM contrats AS c
            WHERE c.id_locataire = ? AND id_box = ?
            AND reglee = False
            ORDER BY debut ASC
        """
        params = (id_locataire, id_box)
        data = udb.fetch_all (requete, params)
        contrat = self.construct (data)
        return contrat



    def get_allBY (self, id_locataire, udb) :

        requete = """
            SELECT
                c.*
            FROM contrats AS c
            WHERE c.id_locataire = ?
        """
        params = (id_locataire)

        data = udb.fetch_all (requete, params)

        contrats = self.construct_tableau (data)
        return contrats

    


    def cheack_contrat (self, id_locataire, id_box, mois, annee, udb) :
        
        # CHEACH SANS TENIR COMPTE DU JOUR, SEULEMENT LE MOIS ET L'ANNEE
        contrat = None
        requete = """
            SELECT 
                c.*
            FROM contrats AS c
            WHERE c.id_locataire = ?
            AND c.id_box = ?
            AND DateSerial(?, ?, 15) BETWEEN DateSerial(Year(c.debut), Month(c.debut), 1)  AND DateSerial(Year(c.fin), Month(c.fin) + 1, 0);
        """

        params = (id_locataire, id_box, annee, mois)

        data = udb.fetch_all (requete, params)

        if data :  # si contrat valide
            id_contrat, debut, fin, id_locataire, id_box, reglee = data[0]
            contrat = Contrat(id_contrat, debut, fin, id_locataire, id_box, reglee)
        # else : return False
        
        # for id_contrat, debut, fin, id_locataire, id_box in data :
        #     contrat = Contrat (id_contrat, debut, fin, id_locataire, id_box)
        #     contrats.append (contrat)

        return contrat
    


    def update_reglee (self, id_contrat, udb) :

        requete = "UPDATE contrats SET reglee = True WHERE id_contrat = ?"
        params = (id_contrat)
        udb.insert_query (requete, params)




    def premier_contrat (self, id_locataire, mois, annee, udb) :
        
        requete = """
            SELECT 
                c.*
            FROM contrats AS c
            WHERE c.id_locataire = ?
            AND c.debut <= DateSerial(?, ? + 1, 0);
        """

        params = (id_locataire, annee, mois)
        data = udb.fetch_all (requete, params)

        if data : return True # si contrat valide
        else : return False
        

    def plus_ancienNONreglee_par (self, id_locataire, udb):

        contrat = None
        requete = """
            SELECT TOP 1 * 
            FROM contrats 
            WHERE id_locataire = ?
            AND reglee = False
            ORDER BY debut ASC
        """
        params = (id_locataire)  # Assurer que params est un tuple
        data = udb.fetch_all(requete, params)

        if data : 
            id_contrat, debut, fin, id_locataire, id_box, reglee = data[0]
            contrat = Contrat(id_contrat, debut, fin, id_locataire, id_box, reglee)

        # for id_contrat, debut, fin, id_locataire, id_box, reglee in data :

        return contrat


    def get_boxsLocataire (self, udb, id_locataire) :

        """ UTILISER POUR L'AFFICHAGE """
        requete = """
            SELECT DISTINCT
                b.*
            FROM contrats AS c
            INNER JOIN box AS b ON c.id_box = b.id_box
            WHERE c.id_locataire = ?
        """
        params = (id_locataire)

        data = udb.fetch_all (requete, params)
        boxs = Box.construct_tableau(Box, data)
        return boxs