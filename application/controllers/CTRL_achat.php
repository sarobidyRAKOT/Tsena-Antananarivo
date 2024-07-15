<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class CTRL_achat extends CI_Controller {


    public function __construct() {
        parent::__construct();
		$this->load->model('Caisse');
		$this->load->model('Produit');
		$this->load->model('Achat');
    }


	public function produits () {

		if (!$this->session->has_userdata('list_achat')) {
			$this->session->set_userdata('list_achat', array());
		}

		$caisse_id = $this->session->userdata('caisse_id');
		// var_dump ($caisse_id);

		$data['content'] = 'pages/produits';
		$data['caisse'] = $this->Caisse->get_byID ($caisse_id);
		$data['produits'] = $this->Produit->get_all ();


		// $data['listeAchat'] = $this->Achat->get_all ();
		// $data['total'] = $this->Achat->total ();
		
		$this->load->view('template/index', $data);
	}
	
	public function ajouter_panier () {

		$caisse_id = 1;
		$produit_id = $this->input->post('produit');
		$qtt = $this->input->post('qtt');


		if (!empty($produit_id) &&
			!empty($qtt) && $qtt*(1) > 0) {
			// misy ___
			$dt_achat = date('Y-m-d');
			$data = array (
				'produit_id' => $produit_id,
				'caisse_id' => $caisse_id,
				'qtt' => $qtt,
				'dt_achat' => $dt_achat
			);

			$list_achat = $this->session->userdata('list_achat');
			if (!is_array($list_achat)) {
				$list_achat = array();
			}

			// Ajouter le nouvel achat au panier
			$list_achat[] = $data;

			// Sauvegarder le panier mis à jour dans la session
			$this->session->set_userdata('list_achat', $list_achat);
			redirect('CTRL_achat/produits');

        } else {
			redirect('CTRL_achat/produits');
		}
	}


	public function liste_achat () {

		// $caisse_id = $this->session->userdata('caisse_id');
		// var_dump ($caisse_id);

		$data['content'] = 'pages/achat';
		// $data['caisse'] = $this->Caisse->get_byID ($caisse_id);
		// $data['produits'] = $this->Produit->get_all ();

		$data['listeAchat'] = $this->Achat->get_all ();
		$data['total'] = $this->Achat->total ();
		
		$this->load->view('template/index', $data);

	}

	public function panier () {
		
		$panier = $this->session->userdata('list_achat');
		$caisse = $this->Caisse->get_byID ($this->session->userdata('caisse_id'));
		$id_achat = $this->Achat->get_lastId ();

		$produits = array();
		for ($i=0; $i < count($panier); $i++) { 
			$p = $this->Produit->get_byID ($panier[$i]['produit_id']);

			$produits[] = array(
				'nom' => $p['nom'],
				'id_achat' => $id_achat + 1,
				'prix' => $p['prix'],
				'qte' => $panier[$i]['qtt'],
				'caisse' => $caisse['nom']
			);
		}

		$data['content'] = 'pages/panier';
		$data['panier'] = $produits;

		$this->load->view('template/index', $data);


	}




	
}

