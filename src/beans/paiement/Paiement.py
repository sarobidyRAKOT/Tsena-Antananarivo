from beans.paiement.Paiement_detail import Paiement_detail
from beans.Loyer_box import Loyer_box
from beans.Tarif import Tarif
from beans.paiement.Exercice  import Exercice
from datetime import datetime
from beans.paiement.Histo_paiement import Histo_paiement
from dateutil.relativedelta import relativedelta # type: ignore

class Paiement :
    def __init__(self) :
        pass



    def create_paiement(self, udb, id_box, dmois, fmois, dannee, fannee):
        loyer_box = Loyer_box(id_box=id_box).get_loyer_byID(udb)
        requete = "INSERT INTO paiement (mois, annee, montant, id_box, payee) VALUES (?, ?, ?, ?, ?)"
        for mois in range(dmois, fmois + 1):
            for annee in range(dannee, fannee + 1):
                tarif = None
                if self.cheack(udb, id_box, mois, annee) :
                    print (f"EFA MIS PAIEMENT {mois} {annee}")
                else :
                    tarif = Tarif(loyer_box.id_marchee, mois, annee)
                    tarif.get_tarif(udb)
                    # print (f"ATO CREATE PAIEMENT {loyer_box.loyer_m2} x {loyer_box.volume} = {loyer_box.get_ttlLoyer()} tarif = {tarif.get_montant(loyer_box.get_ttlLoyer())}")
                    montant = tarif.get_montant(loyer_box.get_ttlLoyer())
                    params = (mois, annee, montant, id_box, False)
                    udb.insert_query(requete, params)
            # end for annee
        # end for mois
    # end def create paiement
    


    # INSERTION PAIEMENT ...

    def cheack (self, udb, id_box, mois, annee) : 
        # VERIFIE LE LE PAIEMENT EST DEJA LA ENREGISTER ...

        requete = "SELECT * FROM paiement WHERE mois = ? AND annee = ? AND id_box = ?"
        params = (mois, annee, id_box)
        data = udb.fetch_all (requete, params)
        # print(f"{data}")
        if data : return True
        else : return False
    # end def chech PAIEMENT ...

    def update_payee (self, udb, id_paiement) :
        requete = "UPDATE paiement SET payee = True WHERE id_paiement = ?"
        params = (id_paiement)
        udb.insert_query (requete, params)


    def paiement (self, udb, id_box, mois, annee, date_paiement, montant) :
        
        # pf : paiement farany
        pf = Paiement_detail().get_paiement_farany(udb, id_box)
        if pf is None : 
        #     # mbl tss paiement mintsy
        #     # INSERTION PAIEMENT JUQUE MOIS TENENINY
            print ("TSY MISY")
            e  = Exercice().get_exercice(udb)
            self.create_paiement(udb, id_box, e.mois, mois, e.annee, annee)
            pf = Paiement_detail().get_paiement_farany(udb, id_box)
            
        d_farany = datetime(pf.annee, pf.mois, 1)
        d_periode = datetime (annee, mois, 1)
        # print (f"tonga {d_farany} {d_periode}")
        # # and if : 
        if d_farany > d_periode : print ("PERIODE DEJA PAYEE")
        else : # manao paiement na dia misy reste aza (vole mihoatra)
            self.traite_paiement(udb, id_box, montant, date_paiement)


    def traite_paiement (self, udb, id_box, montant, date_paiement) :
            
        non_payees = Paiement_detail().get_allApayee (udb, id_box)
        reste = montant
        for non_payee in non_payees : 
            reste = reste - non_payee.reste
            a_payee = 0
            tapitra = False
            
            if reste > 0 :
                a_payee = non_payee.reste
                self.update_payee(udb, non_payee.id_paiement)
            elif reste == 0 : 
                a_payee = non_payee.reste
                tapitra = True
                self.update_payee(udb, non_payee.id_paiement)
            else : 
                a_payee = non_payee.reste + reste
                tapitra = True
            Histo_paiement(date_paiement, a_payee, non_payee.id_paiement).insert(udb)
            if tapitra : break
        # end BOUCLE FOR ... 

        if reste > 0 :
            index = len(non_payees) - 1 # index farany non payee
            n = non_payees[index]
            d1 = datetime(year=n.annee, month=n.mois, day=1) + relativedelta(month=2)
            d2 = datetime(year=n.annee, month=n.mois, day=1) + relativedelta(month=5)
            
            print (f"{reste} {d1} {d2}")
            self.create_paiement(udb, id_box, d1.month, d2.month, d1.year, d2.year)
            self.traite_paiement(udb, id_box, reste, date_paiement)

            