insert into admin(e_mail,mdp) values ('garage@gmail.com','admin');

insert into service(nom_service, durre, prix_service) values ('Reparation simple',60,150000),
                                                              ('Reparation standard',120,250000),
                                                              ('Reparation complexe',480,800000),
                                                              ('Entretient',150,300000);

insert into slot(nom_slot) values ('A'),
                                   ('B'),
                                   ('C');

insert into ouverture(ouverture,fermeture) values (8,18);