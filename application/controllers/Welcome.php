<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Welcome extends CI_Controller {


    public function __construct() {
        parent::__construct();
    }

	public function index () {
		$data = array(
			'content' => 'pages/insertion_client',
			'error' => false
		);
		$this->load->view('index', $data);
	}

	public function se_connecter () {
		$data = array(
			'content' => 'pages/connect_client',
			'error' => false
		);
		$this->load->view('index', $data);
	}

}

?>
