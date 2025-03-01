
class Box :


    def __init__ (self, id=None, x=None, y=None, longueur=None, largeur=None, nom=None, id_marchee=None, id_locataire=None) :
        self.id_box = id
        self.x = x
        self.y = y
        self.payee = False
        self.reste = None
        self.montant = None
        self.longueur = longueur
        self.largeur = largeur
        self.nom = nom
        self.id_locataire = id_locataire
        self.id_marchee = id_marchee


    def get_all (self, udb) :
        requete = "SELECT * FROM box"

        data = udb.fetch_all (requete)
        
        boxs = []
        for id, px, py, longueur, largeur, nom, id_marchee, id_locataire in data :
            box = Box (id, px, py, longueur, largeur, nom, id_marchee, id_locataire)
            boxs.append(box)
        return boxs


    def get_allDetail (self, udb, mois, annee) :

        requete = """
            SELECT 
                b.*, 
                ab.reste AS reste,
                ab.montant AS montant
            FROM box AS b
            LEFT JOIN (
                SELECT id_box, reste, montant
                    FROM all_box 
                WHERE mois = ? AND annee = ?
            ) AS ab 
            ON b.id_box = ab.id_box
        """
        params = (mois, annee)
        data = udb.fetch_all (requete, params)
        # print (f"{data}")        
        boxs = []
        for id, px, py, longueur, largeur, nom, id_marchee, id_locataire, reste, montant in data :
            box = Box (id, px, py, longueur, largeur, nom, id_marchee, id_locataire)
            box.reste = reste
            box.montant = montant
            if reste is None or reste > 0 :
                # print (f"payee {id}")
                # box.payee = False
                pass
            else : box.payee = True

            boxs.append(box)
        return boxs

    def draw(self, canvas):
        x1 = (self.x) * 100
        y1 = (self.y) * 100
        x2 = (self.longueur + self.x) * 100 # Largeur totale du rectangle
        y2 = (self.largeur + self.y) * 100  # Hauteur totale du rectangle

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