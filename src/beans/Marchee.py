
class Marchee :

    def __init__ (self, id=None, x=None, y=None, width=None, height=None, nom=None) :
        self.id_marchee = id
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.nom = nom



    def get_all(self, udb):
        """Récupère toutes les données de la table 'marchee' et les retourne sous forme d'objets Marchee."""
        
        requete = "SELECT * FROM marchee"
        data = udb.fetch_all(requete)

        marchees = []
        
        for id_marchee, px, py, width, height, nom in data:
            marchee = Marchee(id_marchee, px, py, width, height, nom)
            marchees.append(marchee)

        return marchees




    def draw(self, canvas, echelle):
        
        """Dessine un rectangle représentant le marché et ajoute un label avec son nom au centre du rectangle."""
        x1 = (self.x) * echelle
        y1 = (self.y) * echelle
        x2 = (self.width + self.x) * echelle
        y2 = (self.height + self.y) * echelle

        # Dessine le rectangle
        canvas.create_rectangle(x1, y1, x2, y2, outline="black", width=1, fill="")

        # Calcul du centre du rectangle pour placer le texte
        center_x = (x1 + x2) / 2
        center_y = y1 + 10

        canvas.create_text(center_x, center_y, text=self.nom, font=("Consolas", 10, "bold"), fill="green")
