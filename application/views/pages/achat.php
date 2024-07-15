
<?php if (count($listeAchat) > 0) { ?>
<div class="content_2">
    <table>
        <tr>
            <th>produit</th>
            <th>prix_unit</th>
            <th>quantite</th>
            <th>montant</th>
        </tr>
        
        <?php for ($i=0; $i < count($listeAchat); $i++) { ?>
        <tr>
            <td><?php echo $listeAchat[$i]['produit']; ?></td>
            <td><?php echo $listeAchat[$i]['prix_unit']; ?></td>
            <td><?php echo $listeAchat[$i]['quantite']; ?></td>
            <td><?php echo $listeAchat[$i]['montant']; ?></td>
        </tr>
        <?php } ?>
    </table>
    <p class="total">total : <?php echo $total['total']; ?></p>
</div>
<?php } ?>
