
class Exercice :
    def __init__(self, id_exercice=None, date=None, mois=None, annee=None) :
        self.id_exercice = id_exercice
        self.date = date
        self.mois = mois
        self.annee = annee

    def get_exercice (self, udb) :
        
        requete = "SELECT TOP 1 id_exercice, daty, MONTH(daty) AS mois, YEAR(daty) AS annee FROM exercice "      
        data = udb.fetch_all (requete)

        exercice = None
        for id_exercice, date, mois, annee in data :
            exercice = Exercice(id_exercice, date, mois, annee)

        return exercice
