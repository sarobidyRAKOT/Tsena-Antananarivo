
SELECT id_box, MAX(mois) AS dernier_mois, MAX(annee) AS derniere_annee FROM paiement_detail WHERE id_box = ? GROUP BY id_box;


SELECT 
    p.id_paiement, 
    p.montant AS montant, 
    p.mois, 
    p.annee, 
    p.id_box, 
    IIf(IsNull(tp.montant),0,tp.montant) AS payees, 
    IIf(tp.montant Is Null,p.montant,p.montant-tp.montant) AS reste
FROM paiement AS p 
LEFT JOIN ttl_payee AS tp ON p.id_paiement = tp.id_paiement
WHERE 

