
class Loyer_marchee :

    def __init__(self, id_marchee= None, id_loyer= None, daty= None, loyer_m2= None):

        self.id_marchee = id_marchee
        self.id_loyer = id_loyer
        self.daty = daty
        self.loyer_m2 = loyer_m2
        
        
    

    def get_loyer_by (self, id_marchee, mois, annee, udb) :

        loyer_marchee = None
        requete = """
            SELECT TOP 1
                l.id_marchee, l.id_loyer, l.daty, l.loyer
            FROM loyer AS l
            WHERE (Year(l.daty) < ? OR (Year(l.daty) <= ? AND Month(l.daty) <= ?))
            AND l.id_marchee = ?
            ORDER BY Year(l.daty) DESC, Month(l.daty) DESC;
        """
        params = (annee, annee, mois, id_marchee)

        data = udb.fetch_all(requete, params)

        # print (f"{data}")

        if data:
            # Si des données sont trouvées, créer l'objet Box
            id_marchee, id_loyer, daty, loyer = data[0]
            loyer_marchee = Loyer_marchee(id_marchee=id_marchee, id_loyer=id_loyer, daty=daty, loyer_m2=loyer)
            # id, px, py, longueur, largeur, nom, id_marchee, id_locataire = data[0]
            # box = Box(id, px, py, longueur, largeur, nom, id_marchee, id_locataire)
            
        else : raise Exception (f"PAS DE LOYER ASSOCIE A CETTE PERIODE {mois} - {annee}")

        return loyer_marchee

    



    def get_ttlLoyer (self, volume) :
        if self.loyer_m2 == None :
            return 0
        else : return volume * self.loyer_m2