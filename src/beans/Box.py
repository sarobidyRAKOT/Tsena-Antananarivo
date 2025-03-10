
class Box :


    def __init__ (self, id=None, x=None, y=None, longueur=None, largeur=None, nom=None, id_marchee=None) :
        self.id_box = id
        self.x = x
        self.y = y
        self.longueur = longueur
        self.largeur = largeur
        self.nom = nom
        self.id_marchee = id_marchee

        self.payee = None
        self.reste = None
        self.id_locataire = None



    def construct_tableau (self, data) :

        liste = []
        for id_box, px, py, longueur, largeur, nom, id_marchee in data :
            cd = Box (id_box, px, py, longueur, largeur, nom, id_marchee)
            liste.append(cd)
        return liste 
    


    def get_all (self, udb) :
        requete = "SELECT * FROM box"

        data = udb.fetch_all (requete)
        
        boxs = []
        for id, px, py, longueur, largeur, nom, id_marchee in data :
            box = Box (id, px, py, longueur, largeur, nom, id_marchee)
            boxs.append(box)
        return boxs


    def get_by(self, id_box, udb) :
        requete = "SELECT * FROM box WHERE id_box = ?"  # Limiter à une seule ligne
        params = (id_box)
        data = udb.fetch_all(requete, params)
        
        box = None
        if data:
            # Si des données sont trouvées, créer l'objet Box
            id, px, py, longueur, largeur, nom, id_marchee = data[0]
            box = Box(id, px, py, longueur, largeur, nom, id_marchee)
        
        return box  # Retourner None si aucune boîte n'est trouvée



    def get_allDetail (self, udb, mois, annee) :

        requete = """
        SELECT 
            b.*,
            d.id_locataire,
            d.reste,
            d.payee
        FROM box AS b LEFT JOIN (
            SELECT 
                c.id_box,
                c.id_locataire,
                IIf(IsNull(pd.mois), ?, pd.mois) AS mois,
                IIf(IsNull(pd.annee), ?, pd.annee) AS annee,
                IIf(IsNull(pd.reste), 0, pd.reste) AS reste,
                IIf(IsNull(pd.payee), 0, pd.payee) AS payee
            FROM (
                SELECT
                    id_contrat,
                    id_locataire,
                    id_box
                FROM contrats
                WHERE DateSerial(?, ?, 1) BETWEEN 
                DateSerial(Year(debut), Month(debut), 1)  
                AND DateSerial(Year(fin), Month(fin) + 1, 0)
            ) AS c LEFT JOIN (
                SELECT 
                    *
                FROM paiement_detail
                WHERE mois = ? AND annee = ?
            ) AS pd 
            ON c.id_contrat = pd.id_contrat    
        ) AS d ON b.id_box = d.id_box
        """

        params = (mois, annee, annee, mois, mois, annee)
        data = udb.fetch_all (requete, params)

        liste = []
        for id_box, px, py, longueur, largeur, nom, id_marchee, id_locataire, reste, payee in data :
            box = Box (id_box, px, py, longueur, largeur, nom, id_marchee)
            box.id_locataire = id_locataire
            box.reste = reste
            box.payee = payee

            liste.append(box)
        return liste 
    
    #     # print (f"{data}")        
    #     boxs = []
    #     for id, px, py, longueur, largeur, nom, id_marchee, id_locataire, reste, montant in data :
    #         box = Box (id, px, py, longueur, largeur, nom, id_marchee, id_locataire)
    #         box.reste = reste
    #         box.montant = montant
    #         if reste is None or reste > 0 :
    #             # print (f"payee {id}")
    #             # box.payee = False
    #             pass
    #         else : box.payee = True

    #         boxs.append(box)
    #     return boxs

    def draw (self, canvas, echelle) :
        x1 = (self.x) * echelle
        y1 = (self.y) * echelle
        width = (self.longueur + self.x) * echelle
        height = (self.largeur + self.y) * echelle

        montant_du = self.reste + self.payee
        center_x = (x1 + width)/2
        center_y = (y1 + height)/2 
        text_y = y1 - 10
        canvas.create_text(center_x, text_y, text=self.nom, font=("Consolas", 8, "bold"), fill="black")

        if self.id_locataire is None : canvas.create_rectangle(x1, y1, width, height, fill="grey", outline="black", width=1)
        else :
            if montant_du == 0 :
                canvas.create_rectangle(x1, y1, width, height, fill="red", outline="black", width=1)
                # return
            else :
                pp = ((montant_du - self.reste) * 100) / montant_du  # Pourcentage payé
                xp = int((pp * (width - x1)) / 100)  # Largeur de la partie payée
                xn = x1 + xp  # Coordonnée x de la fin de la partie payée
                canvas.create_rectangle(x1, y1, xn, height, fill="green", outline="black", width=1)  # Payé
                if xn != width : canvas.create_rectangle(xn, y1, width, height, fill="red", outline="black", width=1)    # Restant
            canvas.create_text(center_x, center_y, text=self.id_locataire, font=("Consolas", 8, "bold"), fill="black")

        

    def draw__ (self, canvas, echelle):
        x1 = (self.x) * echelle
        y1 = (self.y) * echelle
        x2 = (self.longueur + self.x) * echelle # Largeur totale du rectangle
        y2 = (self.largeur + self.y) * echelle  # Hauteur totale du rectangle

        if self.montant is not None and self.reste is not None :
            pp = ((self.montant - self.reste) * 100) / self.montant  # Pourcentage payé
            xp = int((pp * (x2 - x1)) / 100)  # Largeur de la partie payée
            xn = x1 + xp  # Coordonnée x de la fin de la partie payée
            canvas.create_rectangle(x1, y1, xn, y2, fill="green", outline="black", width=1)  # Payé
            if xn != x2 : canvas.create_rectangle(xn, y1, x2, y2, fill="red", outline="black", width=1)    # Restant

        else : canvas.create_rectangle(x1, y1, x2, y2, fill="red", outline="black", width=1)    # Restant
        # print(f"{x1} {x_paid}")
        # print(f"{x_paid} {x2}")

        # Dessin des rectangles
        # if x_paid != x2 : 

        # Positionnement du texte au centre du rectangle
        center_x = (x1 + x2) / 2
        center_y = y1 - 5  # Légèrement au-dessus du rectangle
        canvas.create_text(center_x, center_y, text=self.nom, font=("Consolas", 8, "bold"), fill="blue")

    
    # def draw (self, canvas) :
    #     x1 = self.x
    #     y1 = self.y
    #     x2 = self.longueur + self.x # width
    #     y2 = self.largeur + self.y # height

    #     pp = ((self.montant - self.reste) * 100) / self.montant # pourcentage payee

    #     xp = int ((pp * x2) / 100)
    #     xn = x2 - xp
        
    #     print (f"{x1} {xp+x1}")
    #     print (f"{x1 + xp} {xn}")
    #     canvas.create_rectangle(x1, y1, xp, y2, fill="green", outline="black", width = 1)
    #     # canvas.create_rectangle(x1, y1, x2, y2, outline="black", width = 1)
    #     canvas.create_rectangle(x1+xp, y1, xn, y2, fill="red", outline="black", width = 1)
    #     center_x = (x1 + x2) / 2
    #     center_y = y1 - 5
    #     canvas.create_text(center_x, center_y, text=self.nom, font=("Consolas", 8, "bold"), fill="blue")
    
    
    def green_draw (self, canvas) :
        x1 = self.x
        y1 = self.y
        x2 = self.longueur + self.x # width
        y2 = self.largeur + self.y # height




        canvas.create_rectangle(x1, y1, x2, y2, fill="green", outline="black", width = 1)
        center_x = (x1 + x2) / 2
        center_y = y1 - 5
        canvas.create_text(center_x, center_y, text=self.nom, font=("Consolas", 8, "bold"), fill="blue")
    
    def red_draw (self, canvas) :
        x1 = self.x
        y1 = self.y
        x2 = self.longueur + self.x
        y2 = self.largeur + self.y
        canvas.create_rectangle(x1, y1, x2, y2, fill="red", outline="black", width = 1)
        center_x = (x1 + x2) / 2
        center_y = y1 - 5
        canvas.create_text(center_x, center_y, text=self.nom, font=("Consolas", 8, "bold"), fill="blue")


    def __repr__(self):
        return f"{self.id_box} {self.nom}"
    
    def get_volume (self) :
        return self.largeur * self.longueur