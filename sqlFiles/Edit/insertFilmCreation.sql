/* PROCEDURE TO INSERT FILM WITH HELPER */

/* DROP PROCEDURES */
DROP PROCEDURE IF EXISTS InsertFilm;
DROP PROCEDURE IF EXISTS CountIds;

/* CREATE PROCEDURES */
DELIMITER //
CREATE PROCEDURE InsertFilm(IN inId INT, IN inFilmName VARCHAR(80), IN inLocation VARCHAR(20), IN inAgeRating VARCHAR(10))
BEGIN
	SET @query = CONCAT('INSERT INTO ', inLocation, ' VALUES (', inId, ', ', QUOTE(inFilmName), ', ', QUOTE(inLocation), ', ', QUOTE(inAgeRating), ')');
		PREPARE stmt FROM @query;
		EXECUTE stmt;
		DEALLOCATE PREPARE stmt;
END //


CREATE PROCEDURE CountIds(IN inLocation Varchar(20))
BEGIN
	SELECT 
	(SELECT COUNT(*) FROM attic WHERE attic.location = inLocation) +
	(SELECT COUNT(*) FROM kitchen WHERE kitchen.location = inLocation) +
	(SELECT COUNT(*) FROM lounge WHERE lounge.location = inLocation) AS total;
END //

DELIMITER ;