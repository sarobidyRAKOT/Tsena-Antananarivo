

<div class="content_1">
    <h1><?php echo $caisse['nom']; ?></h1>

    <form action="<?php echo base_url('CTRL_achat/ajouter_panier') ?>" method="post">
        <p class="input input_first">
            <select name="produit">
                <option value="">Choisir produit</option>
                <?php for ($i=0; $i < count($produits); $i++) { ?>
                <option value="<?php echo $produits[$i]['produit_id']; ?>"><?php echo $produits[$i]['nom']; ?></option>
                <?php } ?>
            </select>
        </p>
        <p class="input">
            <input type="number" name="qtt" placeholder="Quantité">
        </p>
        <p class="input btn_valid">
            <input class="valid" type="submit" value="Valider">
        </p>
    </form>
</div>

