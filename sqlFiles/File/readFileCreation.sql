/* PROCEDURES TO READ USERS AND PASSWORDS */

/* DROP PROCEDURES */
DROP PROCEDURE IF EXISTS ReadUsers;
DROP PROCEDURE IF EXISTS ReadPasswords;

/* CREATE PROCEDURES */
DELIMITER //
CREATE PROCEDURE ReadUsers(IN inUsername VARCHAR(60))
BEGIN
	SELECT *
	FROM users u
	WHERE u.username = inUsername;
END //

CREATE PROCEDURE ReadPasswords(IN inUsername VARCHAR(60))
BEGIN
	SELECT p.user_password, p.secret
	FROM passwords p
	WHERE p.username = inUsername;
END //
DELIMITER ;
