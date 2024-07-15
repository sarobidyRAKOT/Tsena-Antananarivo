
<?php if (isset($panier) && count($panier) > 0) { ?> 
<!-- si panier n'est pas vide -->
<div class="content_2">
    <table>
        <tr>
            <th>produit</th>
            <th>caisse</th>
            <th>id achat</th>
            <th>prix_unit</th>
            <th>quantite</th>
        </tr>
        <?php for ($i=0; $i < count($panier); $i++) { ?>
        <tr>
            <td><?php echo $panier[$i]['nom']; ?></td>
            <td><?php echo $panier[$i]['caisse']; ?></td>
            <td><?php echo $panier[$i]['id_achat']; ?></td>
            <td><?php echo $panier[$i]['prix']; ?></td>
            <td><?php echo $panier[$i]['qte']; ?></td>
        </tr>
        <?php } ?>
    </table>
</div>
<?php } ?>

