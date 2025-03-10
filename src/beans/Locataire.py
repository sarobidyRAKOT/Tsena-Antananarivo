# from udb.Util_DB import Util_DB
from beans.Contrats.Contrat import Contrat


class Locataire:
    
    
    def __init__ (self, id_locataire= None, nom= None):
        self.id_locataire = id_locataire
        self.nom = nom
        self.boxs = []

    def __repr__(self):
        return f"{self.id_locataire} {self.nom} - Boxes: {', '.join(str(box) for box in self.boxs) if self.boxs else 'Aucun'}"

    def config_boxs (self) :
        boxs = []
        for box in self.boxs : boxs.append(f"{box.id_box} - {box.nom}")
        return boxs



    def get_All (self, udb) :

        locataires = []
        requete = "SELECT * FROM locataire"
        data = udb.fetch_all (requete)

        for id, nom in data :
            locataire = Locataire (id, nom)
            locataire.boxs = Contrat().get_boxsLocataire(udb, id)
            
            locataires.append(locataire)
        return locataires
    

    def insert (self, udb) :

        params = ( self.nom )
        requete = "INSERT INTO locataire (nom) VALUES (?)"
        udb.insert_query (requete, params)