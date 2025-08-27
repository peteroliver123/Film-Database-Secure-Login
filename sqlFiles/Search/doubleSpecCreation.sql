/* CREATES SEARCH PROCEDURES THAT TAKE TWO PARAMETERS */

/* DROP PROCEDURES */
DROP PROCEDURE IF EXISTS IdNameSearch;
DROP PROCEDURE IF EXISTS IdLocationSearch;
DROP PROCEDURE IF EXISTS IdAgeSearch;
DROP PROCEDURE IF EXISTS NameLocationSearch;
DROP PROCEDURE IF EXISTS NameAgeSearch;
DROP PROCEDURE IF EXISTS LocationAgeSearch;

/* CREATE PROCEDURES */
DELIMITER //
/* Search by Id and Name */
CREATE PROCEDURE IdNameSearch(IN inId INT, IN inFilmName VARCHAR(80))
BEGIN
	SELECT id, film_name, age_rating, location
	FROM attic a
	WHERE a.film_name = inFilmName AND a.id = inId
	UNION ALL
	SELECT id, film_name, age_rating, location
	FROM kitchen k
	WHERE k.film_name = inFilmName AND k.id = inId
    UNION ALL
	SELECT id, film_name, age_rating, location
	FROM lounge l
	where l.film_name = inFilmName AND l.id = inId;
END //


/* Search by Id and Location */
CREATE PROCEDURE IdLocationSearch(IN inId INT, IN inLocationOne VARCHAR(20), 
IN inLocationTwo VARCHAR(20), IN inLocationThree VARCHAR(20))
BEGIN
	SELECT id, film_name, age_rating, location
	FROM attic a
	WHERE a.location IN (inLocationOne, inLocationTwo, inLocationThree) AND a.id = inId
	UNION ALL
	SELECT id, film_name, age_rating, location
	FROM kitchen k
	WHERE k.location IN (inLocationOne, inLocationTwo, inLocationThree) AND k.id = inId
	UNION ALL
	SELECT id, film_name, age_rating, location
	FROM lounge l
	where l.location IN (inLocationOne, inLocationTwo, inLocationThree) AND l.id = inId;
END //


/* Search by ID and Age Rating */
CREATE PROCEDURE IdAgeSearch(IN inId INT, IN inAgeRatingOne VARCHAR(10), IN inAgeRatingTwo VARCHAR(10), 
IN inAgeRatingThree VARCHAR(10), IN inAgeRatingFour VARCHAR(10), IN inAgeRatingFive VARCHAR(10), 
IN inAgeRatingSix VARCHAR(10), IN inAgeRatingSeven VARCHAR(10))
BEGIN
	SELECT id, film_name, age_rating, location
	FROM attic a
	WHERE a.age_rating IN (inAgeRatingOne, inAgeRatingTwo, inAgeRatingThree, 
		inAgeRatingFour, inAgeRatingFive, inAgeRatingSix, inAgeRatingSeven) AND a.id = inId
	UNION ALL
	SELECT id, film_name, age_rating, location
	FROM kitchen k
	WHERE k.age_rating IN (inAgeRatingOne, inAgeRatingTwo, inAgeRatingThree, 
		inAgeRatingFour, inAgeRatingFive, inAgeRatingSix, inAgeRatingSeven) AND k.id = inId
	UNION ALL
	SELECT id, film_name, age_rating, location
	FROM lounge l
	where l.age_rating IN (inAgeRatingOne, inAgeRatingTwo, inAgeRatingThree, 
		inAgeRatingFour, inAgeRatingFive, inAgeRatingSix, inAgeRatingSeven) AND l.id = inId;
END //


/* Search by Name and Location */
CREATE PROCEDURE NameLocationSearch(IN inFilmName VARCHAR(80), IN inLocationOne VARCHAR(20), IN inLocationTwo VARCHAR(20), IN inLocationThree VARCHAR(20))
BEGIN
	SELECT id, film_name, age_rating, location
	FROM attic a
	WHERE a.location IN (inLocationOne, inLocationTwo, inLocationThree) AND a.film_name = inFilmName
	UNION ALL
	SELECT id, film_name, age_rating, location
	FROM kitchen k
	WHERE k.location IN (inLocationOne, inLocationTwo, inLocationThree) AND k.film_name = inFilmName
	UNION ALL
	SELECT id, film_name, age_rating, location
	FROM lounge l
	where l.location IN (inLocationOne, inLocationTwo, inLocationThree) AND l.film_name = inFilmName;
END //


/* Search by Name and Age Rating */
CREATE PROCEDURE NameAgeSearch(IN inFilmName VARCHAR(80), IN inAgeRatingOne VARCHAR(10), 
IN inAgeRatingTwo VARCHAR(10), IN inAgeRatingThree VARCHAR(10), IN inAgeRatingFour VARCHAR(10), 
IN inAgeRatingFive VARCHAR(10), IN inAgeRatingSix VARCHAR(10), IN inAgeRatingSeven VARCHAR(10))
BEGIN
	SELECT id, film_name, age_rating, location
	FROM attic a
	WHERE a.age_rating IN (inAgeRatingOne, inAgeRatingTwo, inAgeRatingThree, 
	inAgeRatingFour, inAgeRatingFive, inAgeRatingSix, inAgeRatingSeven) AND a.film_name = inFilmName
	UNION ALL
	SELECT id, film_name, age_rating, location
	FROM kitchen k
	WHERE k.age_rating IN (inAgeRatingOne, inAgeRatingTwo, inAgeRatingThree, 
	inAgeRatingFour, inAgeRatingFive, inAgeRatingSix, inAgeRatingSeven) AND k.film_name = inFilmName
	UNION ALL
	SELECT id, film_name, age_rating, location
	FROM lounge l
	where l.age_rating IN (inAgeRatingOne, inAgeRatingTwo, inAgeRatingThree, 
	inAgeRatingFour, inAgeRatingFive, inAgeRatingSix, inAgeRatingSeven) AND l.film_name = inFilmName;
END //


/* Search by Location and Age Rating */
CREATE PROCEDURE LocationAgeSearch(IN inLocationOne VARCHAR(20), IN inLocationTwo VARCHAR(20), 
IN inLocationThree VARCHAR(20), IN inAgeRatingOne VARCHAR(10), IN inAgeRatingTwo VARCHAR(10), 
IN inAgeRatingThree VARCHAR(10), IN inAgeRatingFour VARCHAR(10), IN inAgeRatingFive VARCHAR(10), 
IN inAgeRatingSix VARCHAR(10), IN inAgeRatingSeven VARCHAR(10))
BEGIN
SELECT id, film_name, age_rating, location
FROM attic a
WHERE a.age_rating IN (inAgeRatingOne, inAgeRatingTwo, inAgeRatingThree, 
	inAgeRatingFour, inAgeRatingFive, inAgeRatingSix, inAgeRatingSeven) AND a.location IN (inLocationOne, inLocationTwo, inLocationThree)
UNION ALL
SELECT id, film_name, age_rating, location
FROM kitchen k
WHERE k.age_rating IN (inAgeRatingOne, inAgeRatingTwo, inAgeRatingThree, 
	inAgeRatingFour, inAgeRatingFive, inAgeRatingSix, inAgeRatingSeven) AND k.location IN (inLocationOne, inLocationTwo, inLocationThree)
UNION ALL
SELECT id, film_name, age_rating, location
FROM lounge l
where l.age_rating IN (inAgeRatingOne, inAgeRatingTwo, inAgeRatingThree, 
	inAgeRatingFour, inAgeRatingFive, inAgeRatingSix, inAgeRatingSeven) AND l.location IN (inLocationOne, inLocationTwo, inLocationThree);
END //
DELIMITER ;