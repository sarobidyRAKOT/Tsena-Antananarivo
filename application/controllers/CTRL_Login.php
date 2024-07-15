<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class CTRL_Login extends CI_Controller {

    public function __construct() {
        parent::__construct();
		$this->load->model('Login');
	}


	public function connect_client () {
		$matricule = $this->input->post("");
		$type = $this->input->post("");

		$resp = $this->Login->checkloginUser($matricule, $type);

		var_dump($resp);
	}

	public function insert_client () {
		$matricule = $this->input->post("matricule");
		$type = $this->input->post("type");
		$email = $this->input->post("email");

		$resp = $this->Login->inscription($email, $matricule, $type);

		if ($resp) {
			var_dump($resp);
		} else {
			$data = array(
				'content' => 'pages/insertion_client',
				'error' => true,
				'message' => 'insertion invalide'
			);
			$this->load->view('index', $data);
		}
	}
}

?>
