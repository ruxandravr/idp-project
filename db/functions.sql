use bd;

delimiter //

DROP FUNCTION IF EXISTS cel_mai_vandut_produs;
CREATE FUNCTION cel_mai_vandut_produs() RETURNS VARCHAR(255)
BEGIN
    DECLARE id VARCHAR(10);
    DECLARE nume_produs VARCHAR(255);

    SELECT id_produs into id from tranzactii group by id_produs order by count(id_produs) desc limit 1;
    if SUBSTRING(id, 1, 1) = "b" then
            SELECT nume into nume_produs from bauturi where id_produs = id;
        else
            SELECT nume into nume_produs from mancare where id_produs = id;
        end if;
    RETURN nume_produs;
END//

DROP FUNCTION IF EXISTS castig_total_data;
CREATE FUNCTION castig_total_data(datac DATE) RETURNS int
BEGIN
    DECLARE suma int;
    SET suma = 0;
    SELECT sum(pret) into suma from tranzactii where data = datac;
    RETURN suma;
END//

DROP FUNCTION IF EXISTS castig_total_luna;
CREATE FUNCTION castig_total_luna(luna int) RETURNS int
BEGIN
    DECLARE suma int;
    SET suma = 0;
    SELECT sum(pret) into suma from tranzactii where extract(month from data) = luna;
    RETURN suma;
END//


delimiter ;