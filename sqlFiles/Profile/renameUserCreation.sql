/* PROCEDURE TO RENAME USER */

/* DROP PROCEDURE */
DROP PROCEDURE IF EXISTS RenameUser;

/* CREATE PROCEDURE */
DELIMITER //
CREATE PROCEDURE RenameUser(IN inOldName VARCHAR(60), IN inNewName VARCHAR(60))
BEGIN
	UPDATE users
	SET username = inNewName
	WHERE username = inOldName;

	UPDATE passwords
	SET username = inNewName
	WHERE username = inOldName;
END //
DELIMITER ;