# from udb.Util_DB import Util_DB


class Locataire:
    
    
    def __init__ (self, id_locataire, nom, montant_loyer):
        self.id_locataire = id_locataire
        self.nom = nom
        self.montant_loyer = montant_loyer

    def __repr__ (self):
        return f"{self.id_locataire} {self.nom} {self.montant_loyer}"



    def get_All (self, udb) :
        locataires = []
        requete = "SELECT * FROM locataire"
        data = udb.fetch_all (requete)

        for id, nom, montant in data :
            locataire = Locataire (id, nom, montant)
            locataires.append(locataire)
        return locataires
    
    def insert (self, udb) :
        params = (self.nom, self.montant_loyer)
        requete = "INSERT INTO locataire (nom, montant) VALUES (?, ?)"
        udb.insert_query (requete, params)