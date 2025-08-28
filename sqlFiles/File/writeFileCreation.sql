/* PROCEDURES TO INSERT INTO USERS AND PASSWORDS */

/* DROP PROCEDURES */
DROP PROCEDURE IF EXISTS InsertUser;
DROP PROCEDURE IF EXISTS InsertPassword;

/* CREATE PROCEDURES */
DELIMITER //
CREATE PROCEDURE InsertUser(In inUsername VARCHAR(60), IN inDateCreated DATETIME(6), In inIsLocked BOOLEAN, IN inDateUnlock DATETIME(6), In inNumLockouts INT, IN inIsAdmin BOOLEAN, IN inFailedEntry Int)
BEGIN
	INSERT INTO users
	(username, date_created, is_locked, date_unlock, num_lockouts, is_admin, failed_entry)
	VALUES
	(inUsername, inDateCreated, inIsLocked, inDateUnlock, inNumLockouts, inIsAdmin, inFailedEntry);
END //

CREATE PROCEDURE InsertPassword(In inUsername VARCHAR(60), In inNewPassword VARCHAR(100), IN inSecret VARCHAR(65))
BEGIN
	INSERT INTO passwords
	(username, user_password, secret)
	VALUES
	(inUsername, inNewPassword, inSecret);
END //
DELIMITER ;