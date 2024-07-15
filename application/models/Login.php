
<?php
defined('BASEPATH') OR exit('No direct script access allowed');

    class Login extends CI_Model {

        public function __construct() {
            parent::__construct();
        }

        private function cheack ($user, $mdp) {
            $req = "SELECT * FROM client WHERE nom = '".$user."' and mdp = '".$mdp."'";
            $query = $this->db->query($req);

            return $query->result_array();
        }

        public function connect () : bool {

			
            $user = $this->session->userdata('user');
            $mdp = $this->session->userdata('mdp');
            $valid = false;

            $client = $this->cheack($user, $mdp);
            if (count($client) > 0) {
                $valid = true;
            }
            
            return $valid;
        }

        // public function get_byID ($id_produit) {
        //     $req = "SELECT * FROM produit WHERE produit_id = ".$id_produit;
        //     $query = $this->db->query($req);

        //     return $query->result_array()[0];
        // }
    }
?>
