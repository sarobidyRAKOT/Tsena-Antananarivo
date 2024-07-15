
<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Achat extends CI_Model {

    public function __construct() {
        parent::__construct();
    }

	public function get_all () {
        
        $req = "select
            a.achat_id,
            p.nom produit,
            p.prix prix_unit,
            a.qtt quantite,
            (p.prix * a.qtt) montant
        from achat a join produit p on p.produit_id = a.produit_id
        group by a.achat_id";
        $query = $this->db->query($req);

        return $query->result_array();
	}

    public function total () {
                
        $req = "select
            sum(l.montant) total
        from (
            select
                a.achat_id,
                p.nom produit,
                p.prix prix_unit,
                a.qtt quantite,
                (p.prix * a.qtt) montant
            from achat a join produit p on p.produit_id = a.produit_id
            group by a.achat_id
        ) l";
        $query = $this->db->query($req);

        return $query->result_array()[0];
    }

    public function get_byID ($id_produit) {
        $req = "SELECT * FROM achat WHERE achat_id = ".$id_produit;
        $query = $this->db->query($req);

        return $query->result_array()[0];
	}

    public function insert ($data) {
        $req = "INSERT INTO achat (produit_id, caisse_id, qtt, dt_achat) VALUES (%s, %d, %d, '%s')";    
        $req = sprintf($req, $data['produit_id'], $data['caisse_id'], $data['qtt'], $data['dt_achat']);

        $this->db->query($req);
    }

	public function get_lastId () : int {
		$req = "select sum(id_facture) id from achat group by id_facture";
        $query = $this->db->query($req);

		$ligne = $query->result_array();
			if ($ligne != null) {
			return $ligne[0]['id'];
		} else {
			return 0;
		}
	}
}
