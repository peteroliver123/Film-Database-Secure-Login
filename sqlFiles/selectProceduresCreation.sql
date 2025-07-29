/*SEARCH PROCEDURES CREATION */
DELIMITER //
CREATE PROCEDURE getById(IN id Int, IN location Varchar(65))
BEGIN
IF location = 'attic' THEN
	SELECT * FROM attic WHERE attic.idAttic = id;
ELSEIF location = 'lounge' THEN
	SELECT * FROM lounge WHERE lounge.idLounge = id;
ELSEIF location = 'kitchen' THEN
	SELECT * FROM kitchen WHERE kitchen.idKitchen = id;
ELSE
	SELECT "Invalid Input!" as message;
END IF;
END //

CREATE PROCEDURE getByName(IN filmName Varchar(65), In location Varchar(65))
BEGIN
IF location = 'attic' THEN
	SELECT * FROM attic WHERE attic.name = filmName;
ELSEIF location = 'lounge' THEN
	SELECT * FROM lounge WHERE lounge.name = filmName;
ELSEIF location = 'kitchen' THEN
	SELECT * FROM kitchen WHERE kitchen.name = filmName;
ELSE
	SELECT "Invalid Input!" as message;
END IF;
END //
DELIMITER ;