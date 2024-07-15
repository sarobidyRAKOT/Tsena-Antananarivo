
<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Caisse extends CI_Model {

    public function __construct() {
        parent::__construct();
    }

	public function get_all () {

        $query = $this->db->get('caisse');
        return $query->result_array();
	}

    public function get_byID ($id_caisse) {
        $req = "SELECT * FROM caisse WHERE caisse_id = ".$id_caisse;
        $query = $this->db->query($req);

        return $query->result_array()[0];
	}
}
