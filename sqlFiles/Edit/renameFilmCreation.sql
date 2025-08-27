/* PROCEDURE TO RENAME FILM */

/* DROP PROCEDRURE */
DROP PROCEDURE IF EXISTS RenameFilm;

/* CREATE PROCEDURE */
DELIMITER //
CREATE PROCEDURE RenameFilm(IN inFilmName VARCHAR(80), IN inId INT, IN inLocation VARCHAR(20), IN inNewName VARCHAR(80))
BEGIN

DECLARE atticRenamed INT DEFAULT 0;
DECLARE kitchenRenamed INT DEFAULT 0;
DECLARE loungeRenamed INT DEFAULT 0;
DECLARE total INT DEFAULT 0;
    
UPDATE attic
SET attic.filmName = inNewName
WHERE attic.location = inLocation AND (attic.film_name = inFilmName or attic.id = inId);
SET atticRenamed = ROW_COUNT();

UPDATE kitchen
SET kitchen.filmName = inNewName
WHERE kitchen.location = inLocation AND (kitchen.film_name = inFilmName or kitchen.id = inId);
SET kitchenRenamed = ROW_COUNT();

UPDATE lounge
SET lounge.filmName = inNewName
WHERE lounge.location = inLocation AND (lounge.film_name = inFilmName or lounge.id = inId);
SET loungeRenamed = ROW_COUNT();
SET total = atticRenamed + kitchenRenamed + loungeRenamed;

SELECT total AS message;
END //
DELIMITER ;