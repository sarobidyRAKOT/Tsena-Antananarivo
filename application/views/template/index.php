<?php 

	$this->load->view("layout/head");
		if (!empty($login)) {
			$this->load->view($login);
		} else {
			$this->load->view('template/header');
			$this->load->view($content);
			$this->load->view('template/footer');
		}
	$this->load->view("layout/foot");
?>
