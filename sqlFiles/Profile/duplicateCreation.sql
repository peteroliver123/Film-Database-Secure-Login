/* PROCEDURES TO GET DUPLICATES FILMS */

/* DROP PROCEDURES */
DROP PROCEDURE IF EXISTS PassThreeTableNames;
DROP PROCEDURE IF EXISTS PassTwoTableNames;

/* CREATE PROCEDURES */
DELIMITER //
CREATE PROCEDURE PassThreeTableNames(IN inMyTableName1 VARCHAR(20), IN inMyTableName2 VARCHAR(20), IN inMyTableName3 VARCHAR(20))
BEGIN
	SET @query = CONCAT('SELECT id, film_name, age_rating, location
	FROM ', inMyTableName1, ' t1, ', inMyTableName2, ' t2, ', inMyTableName3, ' t3
	WHERE t1.film_name = t2.film_name and t2.film_name = t3.film_name');
		PREPARE stmt FROM @query;
		EXECUTE stmt;
		DEALLOCATE PREPARE stmt;
END //

CREATE PROCEDURE PassTwoTableNames(IN inMyTableName1 VARCHAR(20), IN inMyTableName2 VARCHAR(20))
BEGIN
	SET @query = CONCAT('SELECT id, film_name, age_rating, location
	FROM ', inMyTableName1, ' t1, ', inMyTableName2, ' t2 
	WHERE t1.film_name = t2.film_name');
		PREPARE stmt FROM @query;
		EXECUTE stmt;
		DEALLOCATE PREPARE stmt;
END //
DELIMITER ;