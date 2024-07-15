
create database super_marchee;
use super_marchee;

drop table achat;
drop table client;
drop table caisse;
drop table produit;

create table produit (
    produit_id int primary key auto_increment,
    nom varchar (50),
    prix double not null,
    quantite_stock int not null
); 

create table caisse (
    caisse_id int primary key auto_increment,
    nom varchar (50)
); 

create table achat (
    achat_id int primary key auto_increment,
	id_facture int not null,
    produit_id int not null, -- references
    caisse_id int not null, -- references
    qtt int not null,
    dt_achat date not null,
    foreign key (produit_id) references produit (produit_id),
    foreign key (caisse_id) references caisse (caisse_id)
); 

create table client (
    client_id int primary key auto_increment,
    nom varchar (50) not null,
    mdp varchar (10) not null
);


-- get liste achat
select
    a.achat_id,
    p.nom produit,
    p.prix prix_unit,
    a.qtt quantite,
    (p.prix * a.qtt) montant
from achat a join produit p on p.produit_id = a.produit_id
group by a.achat_id;

-- total 
select
    sum(l.montant) total
from (
    select
        a.achat_id,
        p.nom produit,
        p.prix prix_unit,
        a.qtt quantite,
        (p.prix * a.qtt) montant
    from achat a join produit p on p.produit_id = a.produit_id
    group by a.achat_id
) l;  

select sum(id_facture) id from achat group by id_facture;
