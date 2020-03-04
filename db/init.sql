use bd;

CREATE TABLE IF NOT EXISTS bauturi (
  id_produs VARCHAR(10) NOT NULL,
  nume VARCHAR(255) NOT NULL,
  pret int NOT NULL,
  PRIMARY KEY (id_produs)
);

CREATE TABLE IF NOT EXISTS mancare (
  id_produs VARCHAR(10) NOT NULL,
  nume VARCHAR(255) NOT NULL,
  pret int NOT NULL,
  PRIMARY KEY (id_produs)
);

CREATE TABLE IF NOT EXISTS inventar (
  id_materie_prima VARCHAR(10) NOT NULL,
  furnizor VARCHAR(255) NOT NULL,
  nume VARCHAR(255) NOT NULL,
  cantitate int NOT NULL,
  PRIMARY KEY (id_materie_prima)
);

CREATE TABLE IF NOT EXISTS tranzactii (
  id_tranzactie VARCHAR(10) NOT NULL,
  id_produs VARCHAR(10) NOT NULL,
  id_client VARCHAR(10) NOT NULL,
  pret int NOT NULL,
  data DATE NOT NULL,
  PRIMARY KEY (id_tranzactie)
);

CREATE TABLE IF NOT EXISTS clienti (
  id_client VARCHAR(20) NOT NULL,
  nume VARCHAR(255) NOT NULL,
  data_nasterii DATE NOT NULL,
  sold int NOT NULL,
  PRIMARY KEY (id_client)
);

CREATE TABLE IF NOT EXISTS backup_produse(
  id_produs VARCHAR(10) NOT NULL,
  nume VARCHAR(255) NOT NULL,
  pret int NOT NULL,
  data TIMESTAMP NOT NULL,
  user VARCHAR(255),
  PRIMARY KEY (id_produs)
);


INSERT INTO bauturi (id_produs, nume, pret)
 VALUES
    ("b1", "Espresso", 12),
    ("b2", "Americano", 13),
    ("b3", "Flat White", 16),
    ("b4", "Pumpkin Spice Latte", 15),
    ("b5", "Hot Chocolate", 10),
    ("b6", "Chai Latte",13),
    ("b7", "Java Chip Frappuccino", 16),
    ("b8", "Caramel Frappe", 13),
    ("b9", "Blonde Roast", 14),
    ("b10", "Iced Caramel Macchiato", 12)
;

INSERT INTO mancare (id_produs, nume, pret)
 VALUES
    ("m1", "Sandvis Bacon", 12),
    ("m2", "Sandvis Omleta", 13),
    ("m3", "Salata Pui", 16),
    ("m4", "Bagheta Mozarella", 15),
    ("m5", "Tiramisu", 10),
    ("m6", "Ecler ciocolata",13),
    ("m7", "Ecler cafea", 16),
    ("m8", "Briosa ciocolata", 13),
    ("m9", "Croissant", 14),
    ("m10", "Tarta fructe", 12)
;


INSERT INTO inventar (id_materie_prima, furnizor, nume, cantitate)
 VALUES
    ("p1", "Impex SRL", "Cafea blonda", 1000),
    ("p2", "Impex SRL","Cafea neagra", 1000),
    ("p3", "Impex SRL","Lapte migdale", 2000),
    ("p4", "Impex SRL","Lapte cocos", 2000),
    ("p5", "Impex SRL","Lapte vaca", 2000),
    ("p6", "Impex SRL", "Zahar", 5000),
    ("p7", "Impex SRL","Frisca", 1000),
    ("p8", "Impex SRL","Aroma vanilie", 500),
    ("p9", "Impex SRL","Aroma cocos", 500),
    ("p10", "Impex SRL","Ceai", 1000),
    ("p11", "Impex SRL","Aroma ciocolata", 500)
;


INSERT INTO clienti (id_client, nume, data_nasterii, sold)
 VALUES
    ("c1", "Avram Ruxandra", "1997-08-11", 1000),
    ("c2", "Stochitoiu Radu", "1995-05-05", 900),
    ("c3", "Avram Teodora", "1993-01-01", 800),
    ("c4", "Avram Ion", "1960-01-14", 700),
    ("c5", "Avram Cici", "1962-09-04", 600)
;