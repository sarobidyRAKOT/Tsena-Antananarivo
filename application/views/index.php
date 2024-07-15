<?php 

	$this->load->view("layout/head_");
		// if (!empty($login)) {
		// 	$this->load->view($login);
		// } else {
		// 	$this->load->view('template/header');
			$this->load->view($content);
		// 	$this->load->view('template/footer');
		// }
		// $this->load->view('pages/insertion_client');
	$this->load->view("layout/foot_");
?>
