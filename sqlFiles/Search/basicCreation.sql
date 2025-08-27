/* CREATES SEARCH PROCEDURES THAT TAKE ONE PARAMETER */

/* DROP PROCEDURES */
DROP PROCEDURE IF EXISTS BasicNameSearch;
DROP PROCEDURE IF EXISTS BasicAgeSearch;
DROP PROCEDURE IF EXISTS BasicLocationSearch;
DROP PROCEDURE IF EXISTS BasicIdSearch;

/* CREATE PROCEDURES */
DELIMITER //
/* Search By Id */
CREATE PROCEDURE BasicIdSearch(IN inId INT)
BEGIN
	SELECT id, film_name, age_rating, location
	FROM attic a
	WHERE a.id = inId
	UNION ALL
	SELECT id, film_name, age_rating, location
	FROM kitchen k
	WHERE k.id = inId
	UNION ALL
	SELECT id, film_name, age_rating, location
	FROM lounge l
	where l.id = inId;
END //


/* Search By Name */
CREATE PROCEDURE BasicNameSearch(IN inFilmName VARCHAR(80))
BEGIN
	SELECT id, film_name, age_rating, location
	FROM attic a
	WHERE a.film_name = inFilmName
	UNION ALL
	SELECT id, film_name, age_rating, location
	FROM kitchen k
	WHERE k.film_name = inFilmName
    UNION ALL
	SELECT id, film_name, age_rating, location
	FROM lounge l
	where l.film_name = inFilmName;
END //


/* Search By Location */
CREATE PROCEDURE BasicLocationSearch(IN inLocationOne VARCHAR(20), IN inLocationTwo VARCHAR(20), IN inLocationThree VARCHAR(20))
BEGIN
	SELECT id, film_name, age_rating, location
	FROM attic a
	WHERE a.location IN (inLocationOne, inLocationTwo, inLocationThree)
	UNION ALL
	SELECT id, film_name, age_rating, location
	FROM kitchen k
	WHERE k.location IN (inLocationOne, inLocationTwo, inLocationThree)
	UNION ALL
	SELECT id, film_name, age_rating, location
	FROM lounge l
	where l.location IN (inLocationOne, inLocationTwo, inLocationThree);
END //


/* Search By Age */
CREATE PROCEDURE BasicAgeSearch(IN inAgeRatingOne VARCHAR(10), IN inAgeRatingTwo VARCHAR(10), 
IN inAgeRatingThree VARCHAR(10), IN inAgeRatingFour VARCHAR(10), IN inAgeRatingFive VARCHAR(10), 
IN inAgeRatingSix VARCHAR(10), IN inAgeRatingSeven VARCHAR(10))
BEGIN
	SELECT id, film_name, age_rating, location
	FROM attic a
	WHERE a.age_rating IN (inAgeRatingOne, inAgeRatingTwo, inAgeRatingThree, 
	inAgeRatingFour, inAgeRatingFive, inAgeRatingSix, inAgeRatingSeven)
	UNION ALL
	SELECT id, film_name, age_rating, location
	FROM kitchen k
	WHERE k.age_rating IN (inAgeRatingOne, inAgeRatingTwo, inAgeRatingThree, 
	inAgeRatingFour, inAgeRatingFive, inAgeRatingSix, inAgeRatingSeven)
	UNION ALL
	SELECT id, film_name, age_rating, location
	FROM lounge l
	where l.age_rating IN (inAgeRatingOne, inAgeRatingTwo, inAgeRatingThree, 
	inAgeRatingFour, inAgeRatingFive, inAgeRatingSix, inAgeRatingSeven);
END //
DELIMITER ;