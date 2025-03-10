from beans.paiement.Paiement_detail import Paiement_detail
from beans.Loyer_marchee import Loyer_marchee
from beans.Tarif import Tarif
from datetime import datetime
from beans.paiement.Histo_paiement import Histo_paiement
from dateutil.relativedelta import relativedelta # type: ignore
from beans.Contrats.Contrat import Contrat
from beans.Contrats.Contrat_detail import Contrat_detail
from beans.paiement.Penalite import Penalite
from beans.Box import Box
import calendar

class Paiement :

    def __init__(self, udb) :
        self.udb = udb
        self.penalite = Penalite().get_ (self.udb)
        pass



    # def create_paiement(self, id_contrat, id_locataire, id_box, dmois, fmois, dannee, fannee) :
    #     """ CREATION PAIEMENT POUR CONTRAT """
    #     # loyer_box = Loyer_box(id_contrat).get_loyer_byID(udb)

    #     # contrats = Contrat().get_allBY (id_locataire, udb)
    #     box = Box().get_by(id_box, self.udb)
    #     requete = "INSERT INTO paiement (mois, annee, montant_du, id_contrat, payee, date_echeance) VALUES (?, ?, ?, ?, ?, ?)"
    #     p = False
    #     pas_contrat = False


    #     for annee in range(dannee, fannee + 1):
    #         stop_loops = False
    #         # TRAITEMENT DU PERIODE PAIEMENT (changement année)
    #         if annee == dannee : mois_debut = dmois
    #         else : mois_debut = 1
    #         if annee == fannee : mois_fin = fmois
    #         else : mois_fin = 12

    #         for mois in range(mois_debut, mois_fin + 1) :

    #             """ PERIODE mois - annee (INCREMENTER) """
    #             # if Contrat().cheack_contrat(id_locataire= id_locataire, id_box=id_box, mois=mois, annee=annee, udb=self.udb) :
    #             #     pas_contrat = True # verifier s'il y a de contrat a cette periode (CONTRAT TAPITRA)
    #             #     break
                
    #             # p = True
    #         #     if self.cheack(id_box, mois, annee):
    #         #         print(f"EFA MIS PAIEMENT {mois} {annee}")
    #         #     else:
    #         #         # print (f"{mois} {annee}")
    #         #         contrat = Contrat().cheack_contrat(id_locataire, id_box, mois, annee, self.udb)
    #         #         if contrat is not None :
    #         #             tarif = Tarif(box.id_marchee, mois, annee)
    #         #             tarif.get_tarif(self.udb)
    #         #             date_echeance = self.date_echeance (annee, mois)
    #         #             loyer = Loyer_marchee().get_loyer_by (box.id_marchee, mois, annee, self.udb)

    #         #             l = loyer.get_ttlLoyer(box.get_volume())
    #         #             montant_du = tarif.get_montant(l)
    #         #             params = (mois, annee, montant_du, contrat.id_contrat, False, date_echeance)
    #         #             self.udb.insert_query(requete, params)
    #         #         else:
    #         #             stop_loops = True
    #         #             break
    #         # if stop_loops:
    #         #     break
    #         if pas_contrat : break
    #         # end for mois
    #     # end for annee
    # # end def create paiement
    #     # if not p : print ("PAS DE CONTRAT")

    def create_paiement (self, requete, id_locataire, periode_mois, periode_annee) :

        contrats = Contrat_detail().getAll_paiementFarany (id_locataire, self.udb)

        for  contrat  in contrats : 
            annee = contrat.annee
            mois = contrat.mois
            insert = False

            if annee is None and mois is None :
                mois = contrat.debut.month
                annee = contrat.debut.year
                insert = True
            else : 
                if self.est_payee(contrat.id_contrat, mois, annee) : 
                    # Si c'est deja payee
                    pp = datetime(annee, mois, 1)
                    p = pp + relativedelta(months=1)
                    mois = p.month
                    annee = p.year
                    insert = True
                # end -- if
            # end -- else

            # print (f"{mois} {annee} id_contrat : {contrat.id_contrat}")
            periode = datetime (year=periode_annee, month=periode_mois, day=1)
            p_contrat = datetime (year=annee, month=mois, day=1)

            if Contrat_detail.cheack_paiementFarany(contrat, self.udb) : 
                Contrat.update_reglee(Contrat, contrat.id_contrat, self.udb)
            if insert and p_contrat < periode and Contrat.cheack_contrat(Contrat, contrat.id_locataire, contrat.id_box, mois, annee, self.udb) :
                # print (f"OUI {p_contrat}")
                self.insert_paiment(requete, mois, annee, False, contrat.id_box, contrat.id_contrat)
            # end if
        # end for
        contrats.clear()




    def paiement (self, id_locataire, id_box, mois, annee, date_paiement, montant) :
        
        """ FONCTION APPELLER POUR EFFECTUER DES PAIEMENT """
        # print (f"{id_locataire} {id_box}")
        # pf : paiement farany
        
        if Contrat.premier_contrat(Contrat, id_locataire, mois, annee, self.udb) is False :
            # POUR VERIFIER SI LE LOCATAIRE AVANT LA PARIODE QU'IL VEUX PAYER
            raise Exception(f"LE LOCATAIRE N'AVAIT MEME PAS DE CONTRAT AVANT  {mois}-{annee}, PAS DE PAIEMENT ___________")
        c = Contrat().get_by (id_locataire, id_box, self.udb)
        if c is None : raise Exception (f"Il n'y a pas de contrat a reglee a cette periode ___ box [{id_box}] - locataire [{id_locataire}] periode [mois:{mois} annee:{annee}], reste montant : {montant}")
        else : 
            if self.est_payee(c.id_contrat, mois, annee) : raise Exception (f"Ce loyer est deja payee ___ box:{id_box}, locataire:{id_locataire} periode [mois:{mois} annee:{annee}]")
        # end -- else

        requete = "INSERT INTO paiement (mois, annee, montant_du, id_contrat, payee, date_echeance) VALUES (?, ?, ?, ?, ?, ?)"
        paiement_detail = Paiement_detail()

        self.create_paiement (requete, id_locataire, mois, annee)
        non_payees = paiement_detail.get_allNON_payee_par (id_locataire=id_locataire, udb=self.udb)
        
        if not non_payees : 
            # print (f"tu peux payee la periode {mois} {annee}")
            contrat = Contrat().get_by (id_locataire, id_box, self.udb)
            self.insert_paiment(requete, mois, annee, False, contrat.id_box, contrat.id_contrat)
            non_payees = paiement_detail.get_allNON_payee (id_locataire, id_box, self.udb)
        # else : 
        #     print ("payee d'abord trosa")

        # pd = Paiement_detail(non_payees[0])
        # # # print (f"{non_payees[0]}")
        # if self.est_payee(pd.id_contrat, pd.mois, pd.annee) : 
        #     raise Exception (f"Ce periode est deja payee")
        self.traite_paiement (non_payees, date_paiement, montant, id_locataire, id_box, mois, annee)
        
        # RECUPERATION PAIEMENT FARANY (par locataire sans tenir compte du box)
        # pf = Paiement_detail().dernier_NONreglee (id_locataire=id_locataire, udb=self.udb)
        # if pf is None :
        # #     # mbl tss paiement mintsy (TOKONY LE ENCIENT CONTRAT NO PAYER-NY)
        # #     # INSERTION PAIEMENT POUR LE PLUS ANCIENT CONTRAT NON REGLEE
        #     # print ("TSY MISY")
        #     # e  = Exercice().get_exercice(self.udb)
        #     # print (f"{contrat.debut}")
        #     contrat = Contrat().plus_ancienNONreglee_par(id_locataire, self.udb) 

        #     # self.create_paiement(id_locataire, contrat.id_box, contrat.debut.month, contrat.fin.month, contrat.debut.year, contrat.fin.year)
        #     # pf = Paiement_detail().dernier_NONreglee (id_locataire=id_locataire, udb=self.udb)

            
        # d_farany = datetime(pf.annee, pf.mois, 1) # Periode non reglée farany
        # d_periode = datetime (annee, mois, 1) # periode limit paiement


        # # print (f"{d_farany} {d_periode}")
        # # # print (f"tonga {d_farany} {d_periode}")
        # # # # and if : 
        # if d_farany > d_periode : raise Exception (f"PAIEMENT DEJA REGLEE, DERNIER PERIODE NON REGLEE mois: {d_farany.month} annee: {d_farany.year}")
        # else : pass
        # else : # manao paiement na dia misy reste aza (vole mihoatra)
        #     self.traite_paiement(id_locataire, id_box, montant, date_paiement)
        # #     pass


    def traite_paiement (self, non_payees, date_paiement, montant, id_locataire, id_box, mois, annee) :
        
        # liste_nonPayees = list (non_payees)
        # print (f"taille du tableau {len(non_payees)} {date_paiement} {montant}")

        reste = montant

        for non_payee in non_payees : 
        # non_payees = Paiement_detail().get_allApayee (self.udb, id_locataire, id_box)
        # print (self.penalite)
        # print ("\n")
        # for non_payee in non_payees : 
        #     print ("\n")
            
            # TRAITEMENT DU PENALITE ...
            decalage = self.decalage______ (non_payee.date_echeance, date_paiement)
            print (decalage)
            penalite = (decalage / self.penalite._decalage()) * self.penalite._penalite() # pourcentage
            montant_penalite = (non_payee.reste * penalite) / 100
            
            # print (non_payee)
            non_payee.reste += montant_penalite
            # print (non_payee)

            # print (f"- {reste} {non_payee.reste} {montant_penalite}\n")
            reste = reste - non_payee.reste
            a_payee = 0
            tapitra = False
            update = False
            
            if reste > 0 :
                a_payee = non_payee.reste
                update = True
            elif reste == 0 : 
                a_payee = non_payee.reste
                update = True 
                tapitra = True # tapitr satry tss  reste tsony
            else : 
                a_payee = non_payee.reste + reste
                tapitra = True # tapitra satry tss vola tsony
            
            a_payee = a_payee - montant_penalite
            Histo_paiement(date_paiement, a_payee, non_payee.id_paiement, montant_penalite).insert(self.udb)
            
            if update : self.update_payee(non_payee.id_paiement)
            if tapitra : break
        # end BOUCLE FOR ... 

        if reste > 0 : 
            index = len(non_payees) - 1 # index farany non payee
            non_payee = non_payees[index]
            # d2 = datetime(year=n.annee, month=n.mois, day=1) + relativedelta(month=5)
            # self.paiement(id_locataire, id_box, d2.mois, annee, date_paiement, reste)
            
            # print (f"{reste}")
            pa = datetime(year=non_payee.annee, month=non_payee.mois, day=1)
            next_p = pa + relativedelta(months=1)

            # print (f"{reste} - {pa} {next_p}")
            self.paiement (id_locataire, id_box, next_p.month, next_p.year, date_paiement, reste)

            # self.create_paiement(self.udb, id_box, d1.month, d2.month, d1.year, d2.year)
            # self.traite_paiement(self.udb, id_box, reste, date_paiement)





    # def  (self, date_echeance, date_paiement) :
    #     # Convertir les chaînes en objets datetime

    #     d_echeance = datetime.strptime(date_echeance, "%Y-%m-%d")
    #     d_paiement = datetime.strptime(date_paiement, "%Y-%m-%d")

    #     # Calculer la différence totale en jours
    #     dec_jours = abs((d_paiement - d_echeance).days)

    #     # Calculer la différence totale en années, mois et jours
    #     delta_relatif = relativedelta(d_paiement, d_echeance)

    #     dec_annees = abs(delta_relatif.years)
    #     dec_mois = dec_annees * 12 + abs(delta_relatif.months)  # Convertir en mois

    #     # return {
    #     #     "total_années": dec_annees,
    #     #     "dec_mois": dec_mois,
    #     #     "total_jours": dec_jours
    #     # }
    #     # return dec_jours
    #     return dec_mois
    #     # return dec_annees



    def date_echeance (self, annee, mois):
    # calendar.monthrange retourne un tuple (premier_jour, dernier_jour)
        _, dernier_jour = calendar.monthrange(annee, mois)
        return datetime(annee, mois, dernier_jour)



    # INSERTION PAIEMENT ...

    def cheack (self, id_contrat, mois, annee) : 

        # VERIFIE SI LE PAIEMENT EST DEJA LA ENREGISTER ...
        requete = "SELECT * FROM paiement WHERE mois = ? AND annee = ? AND id_contrat = ?"
        params = (mois, annee, id_contrat)
        data = self.udb.fetch_all (requete, params)
        # print(f"{data}")
        if data : return True
        else : return False

    def est_payee (self, id_contrat, mois, annee) :

        # Le requete retourne une ligne si le paiement est payee
        requete = """
            SELECT * 
            FROM paiement WHERE mois = ? AND annee = ? AND id_contrat = ?
            AND payee = True
        """
        params = (mois, annee, id_contrat)
        data = self.udb.fetch_all (requete, params)
        # print(f"{data}")
        if data : return True
        else : return False


    def insert_paiment (self, requete, mois, annee, payee, id_box, id_contrat) :

        """ INSERTION PAIEMENT """

        if self.cheack(id_contrat, mois, annee) :
            # VERIFIER S'IL Y A DEJA CETTE PAIEMENT
            print(f"EFA MIS PAIEMENT IO PERIODE IO mois: {mois} - annee: {annee}")
        else : 
            box = Box().get_by(id_box, self.udb)
            tarif = Tarif(box.id_marchee, mois, annee)
            tarif.get_tarif(self.udb)
            loyer = Loyer_marchee().get_loyer_by (box.id_marchee, mois, annee, self.udb)
            ttl_loyer = loyer.get_ttlLoyer (box.get_volume())
            
            montant_du = tarif.get_montant (ttl_loyer)
            date_echeance = self.date_echeance(annee, mois)

            params = (mois, annee, montant_du, id_contrat, payee, date_echeance)
            self.udb.insert_query(requete, params)
        # end -- if




    def update_payee (self, id_paiement) :
        requete = "UPDATE paiement SET payee = True WHERE id_paiement = ?"
        params = (id_paiement)
        self.udb.insert_query (requete, params)


    
    def decalage______ (self, date_echeance, date_paiement):

        # Vérifier si les dates sont déjà des objets datetime
        if isinstance(date_echeance, str) : d_echeance = datetime.strptime(date_echeance, "%Y-%m-%d")
        else : d_echeance = date_echeance
        if isinstance(date_paiement, str) : d_paiement = datetime.strptime(date_paiement, "%Y-%m-%d")
        else: d_paiement = date_paiement

        if d_echeance > d_paiement : return 0
        else :
            dec_jours = abs((d_paiement - d_echeance).days)
            delta_relatif = relativedelta(d_paiement, d_echeance)
            dec_annees = abs(delta_relatif.years)
            dec_mois = dec_annees * 12 + abs(delta_relatif.months)  # Convertir en mois

            return dec_mois
            # return dec_jours
            # return dec_annees
        # end -- else