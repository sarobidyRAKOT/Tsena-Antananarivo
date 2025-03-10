import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Canvas
from beans.Carte import Carte
from beans.Box import Box
from tkcalendar import DateEntry
from beans.paiement.Paiement import Paiement
from beans.Locataire import Locataire

# INTERFACE AFFICHAGE
class TK_interface :
    def __init__(self, root, udb):
        self.root = root
        self.udb = udb
        self.echelle = 50

        self.root.title("Tsena Antananarivo")
        self.initialize_screen(root)
        
        # DEBUT GET DATA UTIL
        # boxs = Box().get_all(self.udb)
        # contrats = Contrat().config(self.udb)

        self.locataires = self.data_locataires ()
        self.mois = self.data_mois ()
        self.annees = self.data_annees ()

        # inputs ...
        self.combo_locataire = None
        self.combo_box = None
        self.combo_annee = None
        self.combo_mois = None
        self.input_annee = None
        self.input_mois = None
        self.locataire_var = None
        self.box_var = None
        # _____

        # FIN GET DAT UTIL
        

        tk.Label(root, text="PAIEMENT LOYER", font=("", 10, "bold")).grid(row=0, column=0, columnspan=2, pady=20)
        self.aff_paiement (root=root)

# DEBUT FONCTION GET DATA

    def data_locataires (self) :
        locataires = {}

        locs = Locataire().get_All(self.udb)

        for locataire in locs :
            locataires[f"{locataire.id_locataire} - {locataire.nom}"] = locataire.config_boxs()
        
        return locataires
    # fin def data locataires

    def data_mois (self) :
        return {
            '01' : "Janvier",
            '02' : "Février",
            '03' : "Mars",
            '04' : "Avril",
            '05' : "Mai",
            '06' : "Juin",
            '07' : "Juillet",
            '08' : "Août",
            '09' : "Septembre",
            '10' : "Octobre",
            '11' : "Novembre",
            '12' : "Décembre"
        }
    
    def data_annees (self) : 
        return {
            "2024",
            "2025"
        }
# FIN FONCTION GET DATA



# FONCTION POUR LES TRAITEMENTS

    def traite_paiement (self):
        mois = self.combo_mois.get()
        annee = self.combo_annee.get()
        box = self.box_var.get()
        locataire = self.locataire_var.get()
        date_paiement = self.date_paiement.get()
        montant = self.montant.get()


        if self.valid_text(locataire) : messagebox.showinfo("Erreur", "LOCATAIRE VIDE")
        elif self.valid_text(box) : messagebox.showinfo("Erreur", "BOX VIDE")
        elif self.valid_text(mois) : messagebox.showinfo("Erreur", "MOIS VIDE")
        elif self.valid_text(annee) : messagebox.showinfo("Erreur", "ANNEES VIDE")
        elif self.valid_text(date_paiement) : messagebox.showinfo("Erreur", "DATE PAIEMENT VIDE")
        elif self.valid_text(montant): messagebox.showinfo("Erreur", "MONTANT VIDE")
        else :
            # print(f"{locataire} {box} {mois} {annee} {date_paiement} {montant}")
            self.paiement(locataire, box, mois, annee, date_paiement, montant) # traitement du paiement


    def paiement (self, locataire, box, mois, annee, date_paiement, montant) :
        id_box = int (box.split(" - ")[0])
        id_locataire = int (locataire.split(" - ")[0])
        mois = int (mois.split(" - ")[0])
        annee = int(annee)
        montant = float (montant) # vola payee
        # print ("TONGA")
        # print (f"ATO {id_box} {mois} {annee} {date_paiement} {montant}")
        paiement = Paiement(self.udb)
        # print (f"{id_box} {id_locataire}")
        try :
            paiement.paiement(id_locataire=id_locataire, id_box=id_box, mois=mois, annee=annee, date_paiement=date_paiement, montant=montant)
        except Exception as e : 
            print (f"{e}")



    def get_carte (self, canvas, mois, annee) :
        carte = Carte()
        mois = int (mois.split(" - ")[0])
        annee = int(annee)
        carte.get_carte(self.udb, mois = mois, annee = annee)

        # CREATION DE LA CARTE (AFFICHAGE)
        for marchee in carte.marchees : marchee.draw(canvas, self.echelle)
        for box in carte.boxs : box.draw(canvas, self.echelle)
            # if box.payee : box.green_draw(canvas)
            # else : box.red_draw(canvas)
            # marchee.draw(canvas)

    def valid_text (self, texte) : 
        return not texte or texte.strip() == ""

# FON FONCTION TRAITEMENTS

            
        # print(self.combo_box.get()+" "+self.combo_mois.get()+" "+self.combo_annee.get())
        # mois_texte = self.combo_mois.get()
        # mois_chiffre = [key for key, value in self.mois.items() if value == mois_texte][0]  # Trouve la clé du mois sélectionné
        # label_resultat.config(text=f"Mois sélectionné (numéro): {mois_chiffre}")
        # print(mois_texte)

    # INITIALISER LE FORMAT DU FENETRE ...

    

    def initialize_screen (self, root) :
        width = 350
        height = 400
        screen_width = root.winfo_screenwidth ()
        screen_height = root.winfo_screenheight ()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        # Définir la géométrie de la fenêtre
        root.geometry(f"{width}x{height}+{x}+{y}")

    def update_subcategories(self):
        # Efface les anciennes options
        self.box_var.set("")  # Réinitialise l'affichage
        menu = self.combo_box["menu"]
        menu.delete(0, "end")

        # Ajoute les nouvelles options
        selected_category = self.locataire_var.get()
        if selected_category in self.locataires:
            for sub in self.locataires[selected_category]:
                menu.add_command(label=sub, command=lambda value=sub: self.box_var.set(value))



    def aff_paiement (self, root) :

        self.locataire_var = tk.StringVar()
        self.box_var = tk.StringVar()


        # LOCATAIRES ...
        tk.Label(root, text="Locataire").grid(row=1, column=0, padx=30, pady=5)
        self.combo_locataire = tk.OptionMenu(root, self.locataire_var, *self.locataires.keys(), command=lambda _: self.update_subcategories())
        self.combo_locataire.config(width=15)
        self.combo_locataire.grid(row=1, column=1, padx=0, pady=5)

        # SELECT BOX ...
        tk.Label(root, text="Box").grid(row=2, column=0, padx=30, pady=5)
        self.combo_box = tk.OptionMenu(root, self.box_var, "")
        self.combo_box.config(width=15)
        self.combo_box.grid(row=2, column=1, padx=0, pady=5)

        # selected_box = tk.StringVar()
        # self.combo_box = ttk.Combobox(root, textvariable=selected_box, state="readonly")
        # self.combo_box['values'] = [f"{box.id_box} - {box.nom} [{box.longueur}x{box.largeur}]" for box in boxs]

        # SELECT MOIS ... 
        # tk.Label(root, text="Mois").grid(row=2, column=0, padx=30, pady=5)
        selected_mois = tk.StringVar()
        self.combo_mois = ttk.Combobox(root, textvariable=selected_mois, state="readonly", width=10 )
        self.combo_mois['values'] = [f"{key} - {value}" for key, value in self.mois.items()]
        self.combo_mois.grid(row=3, column=0, padx=0, pady=5)

        # SELECT ANNEE ... 
        # tk.Label(root, text="Année").grid(row=3, column=0, padx=30, pady=5)
        selected_annee = tk.StringVar()
        self.combo_annee = ttk.Combobox(root, textvariable=selected_annee, state="readonly")
        self.combo_annee['values'] = [f"{annee}" for annee in self.annees]
        self.combo_annee.grid(row=3, column=1, padx=0, pady=5)

        tk.Label(root, text="Date paiement").grid(row=4, column=0, padx=30, pady=5)
        self.date_paiement = DateEntry(root, background='darkblue', foreground='white', borderwidth=1, date_pattern='yyyy-mm-dd')
        self.date_paiement.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(root, text="Montant").grid(row=5, column=0, padx=30, pady=5)
        self.montant = tk.Entry(root, width=25)
        self.montant.grid(row=5, column=1, pady=5)

        # BOUTTON ... (voir carte et paiement)
        root.grid_columnconfigure(0, weight=1)  # Colonne vide à gauche
        root.grid_columnconfigure(1, weight=1)  # Colonne vide à droite

        button = tk.Button(root, text="Payer - enregistrer", command=self.traite_paiement)
        button.grid(row=6, column=0, columnspan=2, padx=20, pady=10)

        button = tk.Button(root, text="Voir carte", command=self.voir_carte)
        button.grid(row=7, column=0, columnspan=2, padx=20, pady=10)


    # fin fonction aff_paiemnt ...



    def process_payment(self):
        # Récupérer les informations saisies
        payment_method = self.payment_var.get()
        amount = self.amount_entry.get()

        # Vérifier que le montant est bien un nombre
        if not amount.isdigit():
            messagebox.showerror("Erreur", "Veuillez entrer un montant valide!")
            return

        amount = float(amount)

        # Afficher un message de confirmation
        messagebox.showinfo("Confirmation", f"Vous avez choisi de payer {amount}€ par {payment_method}.")

        # Réinitialiser le champ de saisie après paiement
        self.amount_entry.delete(0, tk.END)



    def voir_carte(self):

        # Masquer l'interface de paiement
        self.root.withdraw()

        # Créer la fenêtre [carte]
        self.carte_root = tk.Toplevel(self.root)
        self.carte_root.title("Carte TSENA")
        self.carte_root.attributes("-fullscreen", True)


        # Créer un cadre pour les sélecteurs et le bouton
        frame = tk.Frame(self.carte_root)
        frame.pack(pady=10)

        # Ajouter un sélecteur pour les mois
        tk.Label(frame, text="Mois:").pack(side=tk.LEFT, padx=10)
        self.input_mois = ttk.Combobox(frame, state="readonly")
        self.input_mois['values'] = [f"{key} - {value}" for key, value in self.mois.items()]
        self.input_mois.pack(side=tk.LEFT, padx=10)
        # Ajouter un sélecteur pour les années
        tk.Label(frame, text="Année:").pack(side=tk.LEFT, padx=10)
        self.input_annee = ttk.Combobox(frame, state="readonly")  # Par exemple, de 2020 à 2030
        self.input_annee['values'] = [f"{annee}" for annee in self.annees]
        self.input_annee.pack(side=tk.LEFT, padx=10)

        # Canvas pour dessiner la carte
        self.canvas = tk.Canvas(self.carte_root, bg="lightgray")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.voir_button = tk.Button(frame, text="Voir", command=lambda: self.afficher_carte(self.canvas))
        self.voir_button.pack(side=tk.LEFT, padx=10)

        self.back_button = tk.Button(self.carte_root, text="Interface paiement", command=self.back_to_payment)
        self.back_button.pack(pady=20)


    def afficher_carte(self, canvas):
        # FONCTION POUR AFFICHER LA CARTE AVEC PAIEMENT
        annee = self.input_annee.get()
        mois = self.input_mois.get()

        if self.valid_text(mois) or self.valid_text(annee) :
            pass
        else : 
            print (f"{mois} {annee}")   
            self.get_carte(canvas=canvas, mois=mois, annee=annee)




    def back_to_payment (self):
        # Masquer l'interface des rectangles
        self.carte_root.withdraw()
        # Afficher l'interface de paiement
        self.root.deiconify()