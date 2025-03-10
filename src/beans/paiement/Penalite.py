
class Penalite :

    def __init__(self, id_penalite=None, penalite=None, decalage=None) :
        self.id_penalite = id_penalite
        self.penalite = penalite
        self.decalage = decalage



    def get_ (self, udb) :
        
        p = None
        requete = """
            SELECT TOP 1 
                *
            FROM penalite 
        """
        data = udb.fetch_all(requete)

        if data :
            id_penalite, penalite, decalage = data[0]
            p = Penalite (id_penalite, penalite, decalage)
        else : p = Penalite ()

        return p


    def _penalite (self) :
        """ GETTER penalité """
        if self.penalite is None:
            return 0
        return self.penalite
    
    def _decalage(self) :
        """ GETTER decalage """
        if self.decalage is None:
            return 1
        return self.decalage
    
    def __repr__(self):
        return f"decalage : {self._decalage()} penalite : {self._penalite()}"