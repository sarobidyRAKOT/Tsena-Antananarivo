
import pyodbc

class Util_DB :
    def __init__ (self, db_path):
        """ INITIALISATION """
        self.db_path = db_path
        self.conn = None
        self.cursor = None

    def connect (self) :
        try :
            conn_str = f"DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={self.db_path}"
            self.conn = pyodbc.connect(conn_str)
            self.cursor = self.conn.cursor()
        except Exception as e :
            print (f"ERREUR DE CONNEXION {e}")


    def insert_query(self, query, params=None):
        """Exécute une requête SQL (SELECT, INSERT, UPDATE, DELETE)."""
        try:
            # self.cursor.execute("BEGIN TRANSACTION")
            # print("insert")
            if params:
                # Assurez-vous que les paramètres sont dans le bon ordre et correctement formatés
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.conn.commit()
            print("Requête exécutée avec succès")
        except Exception as e:
            self.conn.rollback()
            print(f"Erreur d'exécution de la requête : {e}")



        
    def fetch_all (self, query, params=None):
        # """Exécute une requête SELECT et retourne tous les résultats."""
        try:
            if params : self.cursor.execute(query, params)
            else : self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Erreur lors de la recuperation des donnees : {e}")
            return None


    def close (self) :
        if self.cursor : self.cursor.close()
        if self.conn : self.conn.close()