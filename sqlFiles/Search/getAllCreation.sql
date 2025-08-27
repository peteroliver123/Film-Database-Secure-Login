/* CREATES SEARCH PROCEDURES THAT TAKE NO PARAMETERS */

/* DROP PROCEDURE */
DROP PROCEDURE IF EXISTS GetAll;

/* CREATE PROCEDURE */
DELIMITER //
/* Search to get all*/
CREATE PROCEDURE GetAll()
BEGIN
	SELECT id, film_name, age_rating, location
	FROM attic
	UNION ALL
	SELECT id, film_name, age_rating, location
	FROM kitchen
	UNION ALL
	SELECT id, film_name, age_rating, location
	FROM lounge;
END //
DELIMITER ;