/* CREATES SEARCH PROCEDURES THAT TAKE FOUR PARAMETERS */

/* DROP PROCEDURE */
DROP PROCEDURE IF EXISTS IdNameLocationAgeSearch;

/* CREATE PROCEDURE */
DELIMITER //
/* Search by Id, Name, Location and Age */
CREATE PROCEDURE IdNameLocationAgeSearch(IN inId INT, IN inFilmName VARCHAR(64), IN inLocationOne VARCHAR(20), 
IN inLocationTwo VARCHAR(20), IN inLocationThree VARCHAR(20), IN inAgeRatingOne VARCHAR(10), 
IN inAgeRatingTwo VARCHAR(10), IN inAgeRatingThree VARCHAR(10), IN inAgeRatingFour VARCHAR(10), 
IN inAgeRatingFive VARCHAR(10), IN inAgeRatingSix VARCHAR(10), IN inAgeRatingSeven VARCHAR(10))
BEGIN
	SELECT id, film_name, age_rating, location
	FROM attic a
	WHERE a.age_rating IN (inAgeRatingOne, inAgeRatingTwo, inAgeRatingThree, 
		inAgeRatingFour, inAgeRatingFive, inAgeRatingSix, inAgeRatingSeven) AND 
		a.location IN (inLocationOne, inLocationTwo, inLocationThree) AND inFilmName = a.film_name AND inId = a.id
	UNION ALL
	SELECT id, film_name, age_rating, location
	FROM kitchen k
	WHERE k.age_rating IN (inAgeRatingOne, inAgeRatingTwo, inAgeRatingThree, 
		inAgeRatingFour, inAgeRatingFive, inAgeRatingSix, inAgeRatingSeven) AND 
		k.location IN (inLocationOne, inLocationTwo, inLocationThree) AND inFilmName = k.film_name AND inId = k.id
	UNION ALL
	SELECT id, film_name, age_rating, location
	FROM lounge l
	where l.age_rating IN (inAgeRatingOne, inAgeRatingTwo, inAgeRatingThree, 
		inAgeRatingFour, inAgeRatingFive, inAgeRatingSix, inAgeRatingSeven) AND 
		l.location IN (inLocationOne, inLocationTwo, inLocationThree) AND inFilmName = l.film_name AND inId = l.id;
END //
DELIMITER ;