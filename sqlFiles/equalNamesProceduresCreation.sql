/*EQUAL NAMES PROCEDURES CREATION*/
DELIMITER //
CREATE PROCEDURE passThreeTableNames(IN myTableName Varchar(64), IN myTableName2 Varchar(64), IN myTableName3 Varchar(64))
BEGIN
SET @query = CONCAT('SELECT *
FROM ', myTableName, ' t1, ', myTableName2, ' t2, ', myTableName3, ' t3
WHERE t1.name = t2.name and t2.name = t3.name');
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END //

CREATE PROCEDURE passTwoTableNames(IN myTableName Varchar(64), IN myTableName2 Varchar(64))
BEGIN
SET @query = CONCAT('SELECT *
FROM ', myTableName, ' t1, ', myTableName2, ' t2 
WHERE t1.name = t2.name');
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END //
DELIMITER ;