

<!-- Affiher les listes de caisses -->
<div class="content_1">
    
    <h1>Caisses</h1>
    <form action="<?php echo base_url('welcome/session_caisse') ?>" method="post">
        <p class="input input_first">
            <select name="caisse">
                <option value="">Choisir caisse</option>
                <?php for ($i=0; $i < count($caisses); $i++) { ?>
                <option value="<?php echo $caisses[$i]['caisse_id']; ?>"><?php echo $caisses[$i]['nom']; ?></option>
                <?php } ?>
            </select>
        </p>
        <p class="input btn_valid">
            <input class="valid" type="submit" value="Valider">
        </p>
    </form>
</div>
