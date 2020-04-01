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
  numar_card VARCHAR(16) NOT NULL,
  pret int NOT NULL,
  data DATE NOT NULL,
  PRIMARY KEY (id_tranzactie)
);

CREATE TABLE IF NOT EXISTS backup_produse(
  id_produs VARCHAR(10) NOT NULL,
  nume VARCHAR(255) NOT NULL,
  pret int NOT NULL,
  data TIMESTAMP NOT NULL,
  user VARCHAR(255),
  PRIMARY KEY (id_produs)
);

CREATE TABLE IF NOT EXISTS carduri (
  numar VARCHAR(16) NOT NULL,
  nume VARCHAR(255) NOT NULL,
  luna int NOT NULL,
  anul int NOT NULL,
  cvv int NOT NULL,
  sold int NOT NULL,
  PRIMARY KEY (numar)
);

CREATE TABLE IF NOT EXISTS administrator (
  id VARCHAR(20) NOT NULL,
  parola VARCHAR(20) NOT NULL,
  PRIMARY KEY (id)
);

INSERT INTO bauturi (id_produs, nume, pret)
 VALUES
    ("b1", "Blonde Roast", 14),
    ("b2", "Espresso", 12),
    ("b3", "Americano", 13),
    ("b4", "Flat White", 16),
    ("b5", "Caramel Frappe", 13),
    ("b6", "Iced Caramel Macchiato", 12),
    ("b7", "Java Chip Frappuccino", 16),
    ("b8", "Hot Chocolate", 10),
    ("b9", "Pumpkin Spice Latte", 15),
    ("b10", "Chai Latte",13)

;

INSERT INTO mancare (id_produs, nume, pret)
 VALUES
    ("m1", "Ham panini", 12),
    ("m2", "Tomato & mozarella sandwitch", 13),
    ("m3", "Protein Box", 16),
    ("m4", "Chicken wrap", 15),
    ("m5", "Butter croissant", 10),
    ("m6", "Red velvet loaf cake",13),
    ("m7", "Chocolate chip cookie", 16),
    ("m8", "Blueberry oat cake", 13),
    ("m9", "Glazed doughnut", 14),
    ("m10", "Chocolate brownie", 12)
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

INSERT INTO carduri(numar, nume, luna, anul, cvv, sold)
 VALUES
 ("1", "2", 3, 4, 5, 1000),
 ("2", "Mihai Popescu", 1, 2000, 123, 10),
 ("3", "Radu Dumitru", 1, 2000, 123, 10000),
 ("4", "Elena Teodora", 1, 2000, 123, 1000)
;

INSERT INTO administrator(id, parola)
 VALUES
 ("admin", "1234"),
 ("andra", "0000")
;