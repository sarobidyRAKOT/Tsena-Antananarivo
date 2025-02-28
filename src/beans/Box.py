
class Box :

    def __init__ (self, id=None, x=None, y=None, longueur=None, largeur=None, nom=None, id_marchee=None, id_locataire=None) :
        self.id_box = id
        self.x = x
        self.y = y
        self.payee = False
        self.reste = None
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
                ab.reste AS reste
            FROM box AS b
            LEFT JOIN (
                SELECT id_box, reste 
                    FROM all_box 
                WHERE mois = ? AND annee = ?
            ) AS ab 
            ON b.id_box = ab.id_box
        """
        params = (mois, annee)
        data = udb.fetch_all (requete, params)
        
        boxs = []
        for id, px, py, longueur, largeur, nom, id_marchee, id_locataire, reste in data :
            box = Box (id, px, py, longueur, largeur, nom, id_marchee, id_locataire)
            box.reste = reste
            if reste is None or reste > 0 :
                # print (f"payee {id}")
                # box.payee = False
                pass
            else : box.payee = True

            boxs.append(box)
        return boxs

    
    def green_draw (self, canvas) :
        x1 = self.x
        y1 = self.y
        x2 = self.longueur + self.x
        y2 = self.largeur + self.y
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