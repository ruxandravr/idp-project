use bd;

delimiter //

-- proceduri pentru bauturi
DROP PROCEDURE IF EXISTS inserare_bauturi;
CREATE PROCEDURE inserare_bauturi(IN nume VARCHAR(255), IN pret INT)
    BEGIN
        DECLARE last_id VARCHAR(255);
        DECLARE new_id int;
        DECLARE id VARCHAR(10);
        SELECT SUBSTRING(id_produs, 2) INTO last_id from bauturi order by cast(substring(id_produs,2) as unsigned) desc LIMIT 1;
        SET new_id = 1 + cast(last_id as unsigned);
        SET id = CONCAT('b', convert(new_id, char));
        INSERT INTO bauturi VALUES(id, nume, pret);
    END//

DROP PROCEDURE IF EXISTS selectare_bauturi;
CREATE PROCEDURE selectare_bauturi()
    BEGIN
        SELECT * FROM bauturi;
    END//


DROP PROCEDURE IF EXISTS stergere_bauturi;
CREATE PROCEDURE stergere_bauturi(IN id VARCHAR(10))
    BEGIN
        DELETE FROM bauturi WHERE id_produs = id;
    END//


DROP PROCEDURE IF EXISTS modificare_bauturi_nume;
CREATE PROCEDURE modificare_bauturi_nume(IN id VARCHAR(10), IN new_nume VARCHAR(255))
    BEGIN
        UPDATE bauturi SET nume = new_nume WHERE id_produs = id;
    END//

DROP PROCEDURE IF EXISTS modificare_bauturi_pret;
CREATE PROCEDURE modificare_bauturi_pret(IN id VARCHAR(10), IN new_pret INT)
    BEGIN
        UPDATE bauturi SET pret = new_pret WHERE id_produs = id;
    END//

-- proceduri pentru mancare
DROP PROCEDURE IF EXISTS inserare_mancare;
CREATE PROCEDURE inserare_mancare(IN nume VARCHAR(255), IN pret INT)
    BEGIN
        DECLARE last_id VARCHAR(255);
        DECLARE new_id int;
        DECLARE id VARCHAR(10);
        SELECT SUBSTRING(id_produs, 2) INTO last_id from mancare order by cast(substring(id_produs,2) as unsigned) desc LIMIT 1;
        SET new_id = 1 + cast(last_id as unsigned);
        SET id = CONCAT('m', convert(new_id, char));
        INSERT INTO mancare VALUES(id, nume, pret);
    END//


DROP PROCEDURE IF EXISTS selectare_mancare;
CREATE PROCEDURE selectare_mancare()
    BEGIN
        SELECT * FROM mancare;
    END//

DROP PROCEDURE IF EXISTS stergere_mancare;
CREATE PROCEDURE stergere_mancare(IN id VARCHAR(10))
    BEGIN
        DELETE FROM mancare WHERE id_produs = id;
    END//

DROP PROCEDURE IF EXISTS modificare_mancare_nume;
CREATE PROCEDURE modificare_mancare_nume(IN id VARCHAR(10), IN new_nume VARCHAR(255))
    BEGIN
        UPDATE mancare SET nume = new_nume WHERE id_produs = id;
    END//

DROP PROCEDURE IF EXISTS modificare_mancare_pret;
CREATE PROCEDURE modificare_mancare_pret(IN id VARCHAR(10), IN new_pret INT)
    BEGIN
        UPDATE mancare SET pret = new_pret WHERE id_produs = id;
    END//

-- proceduri pentru inventar
DROP PROCEDURE IF EXISTS inserare_inventar;
CREATE PROCEDURE inserare_inventar(IN furnizor VARCHAR(255), IN nume VARCHAR(255), IN cantitate INT)
    BEGIN
        DECLARE last_id VARCHAR(255);
        DECLARE new_id int;
        DECLARE id VARCHAR(10);
        SELECT SUBSTRING(id_materie_prima, 2) INTO last_id from inventar order by cast(substring(id_materie_prima,2) as unsigned) desc LIMIT 1;
        SET new_id = 1 + cast(last_id as unsigned);
        SET id = CONCAT('p', convert(new_id, char));
        INSERT INTO inventar VALUES(id, furnizor, nume, cantitate);
    END//


DROP PROCEDURE IF EXISTS selectare_inventar;
CREATE PROCEDURE selectare_inventar()
    BEGIN
        SELECT * FROM inventar;
    END//

DROP PROCEDURE IF EXISTS stergere_inventar;
CREATE PROCEDURE stergere_inventar(IN id VARCHAR(10))
    BEGIN
        DELETE FROM inventar WHERE id_materie_prima = id;
    END//


DROP PROCEDURE IF EXISTS modificare_inventar_nume;
CREATE PROCEDURE modificare_inventar_nume(IN id VARCHAR(10), IN new_nume VARCHAR(255))
    BEGIN
        UPDATE inventar SET nume = new_nume WHERE id_materie_prima = id;
    END//

DROP PROCEDURE IF EXISTS modificare_inventar_furnizor;
CREATE PROCEDURE modificare_inventar_furnizor(IN id VARCHAR(10), IN new_furnizor VARCHAR(255))
    BEGIN
        UPDATE inventar SET furnizor = new_furnizor WHERE id_materie_prima = id;
    END//

DROP PROCEDURE IF EXISTS modificare_inventar_cantitate;
CREATE PROCEDURE modificare_inventar_cantitate(IN id VARCHAR(10), IN new_cantitate VARCHAR(255))
    BEGIN
        UPDATE inventar SET cantitate = new_cantitate WHERE id_materie_prima = id;
    END//


-- proceduri pentru clienti
DROP PROCEDURE IF EXISTS inserare_clienti;
CREATE PROCEDURE inserare_clienti(IN nume VARCHAR(255), IN datac DATE, IN sold INT)
    BEGIN
        DECLARE last_id VARCHAR(255);
        DECLARE new_id int;
        DECLARE id VARCHAR(10);
        SELECT SUBSTRING(id_client, 2) INTO last_id from clienti order by cast(substring(id_client,2) as unsigned) desc LIMIT 1;
        SET new_id = 1 + cast(last_id as unsigned);
        SET id = CONCAT('c', convert(new_id, char));
        INSERT INTO clienti VALUES(id, nume, datac, sold);
    END//


DROP PROCEDURE IF EXISTS selectare_clienti;
CREATE PROCEDURE selectare_clienti()
    BEGIN
        SELECT * FROM clienti;
    END//

DROP PROCEDURE IF EXISTS stergere_clienti;
CREATE PROCEDURE stergere_clienti(IN id VARCHAR(10))
    BEGIN
        DELETE FROM clienti WHERE id_client = id;
    END//

DROP PROCEDURE IF EXISTS modificare_clienti_sold;
CREATE PROCEDURE modificare_clienti_sold(IN id VARCHAR(10), IN new_sold int)
    BEGIN
        UPDATE clienti SET sold = new_sold WHERE id_client = id;
    END//

-- proceduri pentru tranzactii
DROP PROCEDURE IF EXISTS inserare_tranzactii;
CREATE PROCEDURE inserare_tranzactii(IN id_tranzactie VARCHAR(10), IN id_produs VARCHAR(10), IN id_client VARCHAR(10), IN pret int)
    BEGIN
        INSERT INTO tranzactii VALUES(id_tranzactie, id_produs, id_client, pret, CURDATE());
    END//


DROP PROCEDURE IF EXISTS selectare_tranzactii;
CREATE PROCEDURE selectare_tranzactii()
    BEGIN
        SELECT * from tranzactii;
    END//


DROP PROCEDURE IF EXISTS cumparare_produs;
CREATE PROCEDURE cumparare_produs(IN id_tranzactie VARCHAR(10), IN produs VARCHAR(10),IN client VARCHAR(10))
    BEGIN
        DECLARE cost_produs int;
        DECLARE sold_client int;
        DECLARE sold_nou_client int;

        SELECT sold into sold_client from clienti where id_client = client;

        if SUBSTRING(produs, 1, 1) = "b" then
            SELECT pret into cost_produs from bauturi where id_produs = produs;
        else
            SELECT pret into cost_produs from mancare where id_produs = produs;
        end if;
        SET sold_nou_client = sold_client - cost_produs;
        UPDATE clienti set sold = sold_nou_client where id_client = client;
        INSERT into tranzactii VALUES(id_tranzactie, produs, client, cost_produs, CURDATE());

    END//

DROP PROCEDURE IF EXISTS bilant_zilnic;
CREATE PROCEDURE bilant_zilnic()
    BEGIN
       select data, sum(pret) castig from tranzactii group by data;
    END//

DROP PROCEDURE IF EXISTS top_produse;
CREATE PROCEDURE top_produse()
    BEGIN
       select id_produs, count(*) vanzari from tranzactii group by id_produs order by count(*) desc;
    END//

DROP PROCEDURE IF EXISTS selectare_backup_produse;
CREATE PROCEDURE selectare_backup_produse()
    BEGIN
        SELECT * FROM backup_produse;
    END//



delimiter ;


