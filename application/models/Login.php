<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Login extends CI_Model {

    public function __construct() {
        parent::__construct();
        // Chargement de la base de données dans le constructeur
        $this->load->database();
    }

    public function checkloginUser($matricule, $type) {
        // Sélectionne les détails du client à partir de la base de données en fonction de son nom et son mot de passe
		
        $query = $this->db->query("SELECT id_client FROM client WHERE matricule = '$matricule' AND type_voiture = '$type'");
        
        // Vérifie s'il y a un résultat
        if ($query->num_rows() == 1) {
            // Retourne le premier résultat sous forme d'objet
            return $query->row();
        } else {
            // Si aucun résultat n'est trouvé, retourne null
            return null;
        }
    }

    public function checkloginAdmin($email, $mdp) {
        // Sélectionne les détails du client à partir de la base de données en fonction de son nom et son mot de passe
        $query = $this->db->query("SELECT id_admin FROM admin WHERE e_mail = '$email' AND mdp = '$mdp'");
        
        // Vérifie s'il y a un résultat
        if ($query->num_rows() == 1) {
            // Retourne le premier résultat sous forme d'objet
            return $query->row();
        } else {
            // Si aucun résultat n'est trouvé, retourne null
            return null;
        }
    }

    public function inscription($email, $matricule, $type) {
        // Données à insérer dans la table
        $data = array(
            'e_mail' => $email,
            'matricule' => $matricule,
            'type_voiture' => $type
        );
        // Insertion des données dans la table 'utilisateurs'

		if ($this->verifier_client($email, $matricule, $type)) {
			$this->db->insert('client', $data);
			// Vérification de l'insertion
	
			if ($this->db->affected_rows() > 0) {
				// Retourne l'ID de l'utilisateur nouvellement inséré
				return $this->db->insert_id();
			} else {
				// En cas d'échec de l'insertion
				return false; 
			}
		} else {
			return false;
		}

    }

	private function verifier_client ($email, $matricule, $type) {

        $query = $this->db->query("SELECT id_client FROM client WHERE e_mail = '$email' AND matricule = '$matricule' AND type_voiture = '$type'");		
		if ($query->num_rows() == 1) {
			return false;
		} else {
            return true;
        }
	}
    
}
