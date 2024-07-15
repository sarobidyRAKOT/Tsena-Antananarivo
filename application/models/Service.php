<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Service extends CI_Model {

    public function __construct() {
        parent::__construct();
        // Chargement de la base de données dans le constructeur
        $this->load->database();
    }

    public function insert_service($nom_service, $durre, $prix_service) {
        // Données à insérer dans la table
        $data = array(
            'nom_service' => $nom_service,
            'durre' => $durre,
            'prix_service' => $prix_service
        );
        // Insertion des données dans la table 'utilisateurs'
        $this->db->insert('service', $data);
        // Vérification de l'insertion
        if ($this->db->affected_rows() > 0) {
            // Retourne l'ID de l'utilisateur nouvellement inséré
            return $this->db->insert_id();
        } else {
            // En cas d'échec de l'insertion
            return false;
        }
    }
    
}