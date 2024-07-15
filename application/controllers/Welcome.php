<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Welcome extends CI_Controller {


    public function __construct() {
        parent::__construct();
		$this->load->model('Caisse');
		$this->load->model('Login');
    }

	public function login () {

		$data['login'] = 'pages/login';
		$this->load->view('template/index', $data);
	}

    public function page_acceuil () {
        $data['content'] = 'pages/acceuil';
        $data['caisses'] = $this->Caisse->get_all ();

        $this->load->view('template/index', $data);
    }
	
    public function session_caisse () {
		$caisse_id = $this->input->post('caisse');

		if (!empty($caisse_id)) {
			// misy ___
			$this->session->set_userdata('caisse_id', $caisse_id);

			redirect('CTRL_achat/ajouter_panier');
        } else {
            $this->page_acceuil();
        }
	}
 

    public function valid_login () {

        $user = $this->input->post('nom');
        $mdp = $this->input->post('mdp');

        if (!empty($user) && !empty($mdp)) {
            # misy daolo ...
            
            $array = array(
                'user' => $user,
                'mdp' => $mdp
            );
            $this->session->set_userdata($array); // session   
            if ($this->Login->connect ()) {
                $this->page_acceuil();
            } else {
                redirect('welcome/login');
            }
        } else { redirect('welcome/login'); }
    }
		
	public function test () {
        $this->load->view('pages/test');
	}
}
