from beans.Marchee import Marchee
from beans.Box import Box

class Carte :


    def __init__(self):
        self.marchees = []
        self.boxs = []

    
    def get_carte (self, udb, mois, annee) :

        self.marchees = Marchee().get_all(udb)
        self.boxs = Box.get_allDetail(Box, udb, mois, annee)
    
