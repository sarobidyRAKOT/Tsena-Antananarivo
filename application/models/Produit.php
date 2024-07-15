
<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Produit extends CI_Model {

    public function __construct() {
        parent::__construct();
    }

	public function get_all () {

        $query = $this->db->get('produit');
        return $query->result_array();
	}

    public function get_byID ($id_produit) {
        $req = "SELECT * FROM produit WHERE produit_id = ".$id_produit;
        $query = $this->db->query($req);

        return $query->result_array()[0];
	}
}
