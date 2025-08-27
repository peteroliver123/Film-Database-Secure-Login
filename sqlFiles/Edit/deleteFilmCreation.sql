/* CREATES PROCEDURE TO DELETE A FILM */

/* DROP PROCEDURE */
DROP PROCEDURE IF EXISTS DeleteFilm;

/* CREATE PROCEDURE */
DELIMITER //
CREATE PROCEDURE DeleteFilm(IN inId INT, IN inFilmName VARCHAR(80), IN inLocation VARCHAR(20))
BEGIN

	DECLARE deletedFromAttic INT DEFAULT 0;
	DECLARE deletedFromKitchen INT DEFAULT 0;
	DECLARE deletedFromLounge INT DEFAULT 0;
	DECLARE deletedTotal INT DEFAULT 0;

	DELETE FROM attic
	WHERE attic.location = inLocation AND (attic.film_name = inFilmName OR attic.id = inId);
	SET deletedFromAttic = ROW_COUNT();

	DELETE FROM kitchen
	WHERE kitchen.location = inLocation AND (kitchen.film_name = inFilmName OR kitchen.id = inId);
	SET deletedFromKitchen = ROW_COUNT();

	DELETE FROM lounge
	WHERE lounge.location = inLocation AND (lounge.film_name = inFilmName OR lounge.id = inId);
	SET deletedFromLounge = ROW_COUNT();

	SET deletedTotal = deletedFromAttic + deletedFromKitchen + deletedFromLounge;

	SELECT total AS message;
    
END //
DELIMITER ;