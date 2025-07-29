/*DELETE PROCEDURES CREATION */
DELIMITER //
CREATE PROCEDURE deleteNamed(IN filmName Varchar(64), IN location Varchar(64))
BEGIN
IF location = 'attic' THEN
	DELETE FROM attic WHERE attic.name = filmName;
ELSEIF location = 'lounge' THEN
	DELETE FROM lounge WHERE lounge.name = filmName; 
ELSEIF location = 'kitchen' THEN
	DELETE FROM kitchen WHERE kitchen.name = filmName;
ELSE
	SELECT "Invalid Input!" AS message;
END IF;
END //

CREATE PROCEDURE deleteById(IN id Int, IN location Varchar(64))
BEGIN
IF location = 'attic' THEN
	DELETE FROM attic WHERE attic.idAttic = id;
ELSEIF location = 'lounge' THEN
	DELETE FROM lounge WHERE lounge.idLounge = id;
ELSEIF location = 'kitchen' THEN
	DELETE FROM kitchen WHERE kitchen.idKitchen = id;
ELSE
	SELECT "Invalid Input!" AS message;
END IF;
END //
DELIMITER ;