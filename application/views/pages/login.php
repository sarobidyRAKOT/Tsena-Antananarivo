
<!-- FORMULAIRE LOGIN -->
<div class="login">
    <h1>Se Connecter</h1>

    <form action="<?php echo base_url('welcome/valid_login') ?>" method="post">
        <p class="input input_first">
            <input type="text" placeholder="Nom d'utilisateur" name="nom" value="Rakoto">
        </p>
        <p class="input">
            <input type="password" placeholder="Mot de passe" name="mdp" value="rakoto">
        </p>
        <p class="input btn_valid">
            <input class="valid" type="submit" value="Connecter">
        </p>
    </form>

</div>   
