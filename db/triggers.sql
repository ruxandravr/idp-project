use bd;

CREATE TRIGGER before_bauturi_delete
    BEFORE DELETE ON bauturi
    FOR EACH ROW
    INSERT INTO backup_produse
    SET id_produs = OLD.id_produs,
        nume = OLD.nume,
        pret = OLD.pret,
        data = CURRENT_TIMESTAMP,
        user = CURRENT_USER();


CREATE TRIGGER before_mancare_delete
    BEFORE DELETE ON mancare
    FOR EACH ROW
    INSERT INTO backup_produse
    SET id_produs = OLD.id_produs,
        nume = OLD.nume,
        pret = OLD.pret,
        data = CURRENT_TIMESTAMP,
        user = CURRENT_USER();