/* PROCEDURE TO TURN ON 2FA */

/* DROP PROCEDURE */
DROP PROCEDURE IF EXISTS UpdateTwoFa;

/*CREATE PROCEDURE */
DELIMITER //
CREATE PROCEDURE UpdateTwoFa(IN inUsername VARCHAR(60), IN inSecret VARCHAR(65))
BEGIN
	UPDATE passwords
	SET passwords.secret = inSecret
	WHERE passwords.username = inUsername;
END //
DELIMITER ;