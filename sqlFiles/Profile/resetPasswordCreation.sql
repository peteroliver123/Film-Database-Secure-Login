/* PROCEDURE TO RESET PASSWORD */

/* DROP PROCEDURE */
DROP PROCEDURE IF EXISTS ResetPassword;

/* CREATE PROCEDURE */
DELIMITER //
CREATE PROCEDURE ResetPassword(IN inUsername VARCHAR(60), IN inNewPassword VARCHAR(100))
BEGIN
	UPDATE passwords
	SET passwords.user_password = inNewPassword
	WHERE passwords.username = inUsername;
END //
DELIMITER ;