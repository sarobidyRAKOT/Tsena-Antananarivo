

class Tarif :
    def __init__(self, id_marchee, mois, annee):

        self.id_marchee = id_marchee
        self.mois = mois
        self.annee = annee
        self.tarif = 0 # pourcentage (negatif ou positif)


    def get_tarif (self, udb) :
        requete = """
            SELECT 
                IIf(tarif IS NULL, 0, tarif) AS t
            FROM tarif 
            WHERE id_marchee = ? 
            AND ? BETWEEN MONTH(debut_periode) AND MONTH(fin_periode)
            AND ? BETWEEN YEAR(debut_periode) AND YEAR(fin_periode)
        """
        params = (self.id_marchee, self.mois, self.annee)
        data = udb.fetch_all (requete, params)
        # print(f"{data}")
        
        if data is not None :
            for t in data : self.tarif = t[0]
    

    def get_montant(self, montant):
        if self.tarif is None:
            self.tarif = 0
        tarif_calcule = (montant * self.tarif) / 100
        return montant + tarif_calcule