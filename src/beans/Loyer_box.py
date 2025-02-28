
class Loyer_box :

    def __init__(self, id_box, id_marchee=None, volume=None, loyer_m2 = None):
        self.id_box = id_box

        self.volume = volume
        self.id_marchee = id_marchee
        self.loyer_m2 = loyer_m2
        
        
    
    def get_loyer_byID (self, udb) :
        requete = "SELECT * FROM loyer_box WHERE id_box = ?"
        params = (self.id_box)
        data = udb.fetch_all (requete, params)
        # print (f"ato {data}")

        loyer_box = None
        for id_marchee, id_box, volume, loyer_m2 in data :
            loyer_box = Loyer_box(id_box, id_marchee, volume, loyer_m2)

        return loyer_box
    
    def get_ttlLoyer (self) :
        if self.volume == None or self.loyer_m2 == None :
            return 0
        else : return self.volume * self.loyer_m2