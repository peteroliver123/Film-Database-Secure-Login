CREATE DATABASE  IF NOT EXISTS `record_boxes` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `record_boxes`;
-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: record_boxes
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `attic`
--

DROP TABLE IF EXISTS `attic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attic` (
  `id` int NOT NULL AUTO_INCREMENT,
  `film_name` varchar(80) NOT NULL,
  `location` varchar(20) NOT NULL,
  `age_rating` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `check_attic` CHECK (((`age_rating` in (_utf8mb4'U',_utf8mb4'PG',_utf8mb4'12',_utf8mb4'12A',_utf8mb4'15',_utf8mb4'18',_utf8mb4'BLANK')) and (`location` = _utf8mb4'attic')))
) ENGINE=InnoDB AUTO_INCREMENT=200 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attic`
--

LOCK TABLES `attic` WRITE;
/*!40000 ALTER TABLE `attic` DISABLE KEYS */;
INSERT INTO `attic` VALUES (1,'U571','attic','12'),(2,'The A-Team','attic','12A'),(3,'The Addams Family','attic','PG'),(4,'Where Eagles Dare','attic','PG'),(5,'Knight and Day','attic','12A'),(6,'Bridget Jones\'s Diary','attic','15'),(7,'Spiderman 2','attic','PG'),(8,'Superman: The Movie','attic','PG'),(9,'Star Trek','attic','12A'),(10,'Godzilla','attic','12'),(11,'Zulu Dawn','attic','15'),(12,'The Mummy - Tomb of the Dragon Emperor','attic','12'),(13,'Nativity','attic','U'),(14,'Grinch','attic','PG'),(15,'The Sound of Music','attic','U'),(16,'Four Christmases','attic','12A'),(17,'Escape to Victory','attic','PG'),(18,'Zulu','attic','PG'),(19,'Gremlins','attic','12A'),(20,'Love Actually','attic','15'),(21,'Clash of the Titans','attic','12A'),(22,'Moon','attic','15'),(23,'The Chronicles of Narnia: Prince Caspian','attic','PG'),(24,'The Secret of Kells','attic','PG'),(25,'Prince of Persia','attic','12A'),(26,'Hairspray','attic','PG'),(27,'Mary Poppins','attic','U'),(28,'Robin Hood','attic','BLANK'),(29,'Wonder Woman','attic','12A'),(30,'Charlotte\'s Web','attic','U'),(31,'Pirates of the Caribbean: At World\'s End','attic','12A'),(32,'Old Dogs','attic','PG'),(33,'Junebug','attic','15'),(34,'Mannequin','attic','PG'),(35,'Only You','attic','PG'),(36,'Hulk','attic','12A'),(37,'Pearl Harbour','attic','12'),(38,'Pirates of the Caribbean: The Curse of the Black Pearl','attic','12A'),(39,'The Time Machine','attic','PG'),(40,'The Last Boy Scout','attic','18'),(41,'X-men','attic','12'),(42,'Robin Hood Prince of Thieves','attic','12'),(43,'My Dog Skip','attic','PG'),(44,'Splice','attic','15'),(45,'Star Trek','attic','BLANK'),(46,'Transformers','attic','12A'),(47,'Liar Liar','attic','PG'),(48,'Waterloo Road','attic','BLANK'),(49,'Blue Streak','attic','12'),(50,'The Great Escape','attic','PG'),(51,'Meet Dave','attic','PG'),(52,'Lethal Weapon','attic','18'),(53,'Black Beauty','attic','U'),(54,'Attack on the Iron Coast','attic','PG'),(55,'The Fox and the Hound','attic','U'),(56,'Apollo 13','attic','PG'),(57,'Gallipoli','attic','PG'),(58,'Kelly\'s Heroes','attic','PG'),(59,'The Goonies','attic','PG'),(60,'Wonka','attic','PG'),(61,'Fantasia','attic','U'),(62,'Star Wars: Attack of the Clones','attic','PG'),(63,'633 Squadron','attic','PG'),(64,'Spartacus','attic','PG'),(65,'Flight of the Doves','attic','U'),(66,'Megamind','attic','PG'),(67,'Midway','attic','PG'),(68,'Flash Gordon','attic','PG'),(69,'Die Another Day','attic','12A'),(70,'Legend','attic','PG'),(71,'Shrek Forever After','attic','U'),(72,'Batman Begins','attic','12A'),(73,'The Blind Side','attic','12A'),(74,'Doc Hollywood','attic','PG'),(75,'Fantastic Four: Rise of the Silver Surfer','attic','PG'),(76,'The Heartbreak Kid','attic','15'),(77,'Kingdom of Heaven','attic','15'),(78,'The Twilight Saga: New Moon','attic','12A'),(79,'Eagle Eye','attic','12A'),(80,'The Chronicles of Narnia: The Lion, The Witch and the Wardrobe','attic','PG'),(81,'Avengers Assemble','attic','12A'),(82,'Force 10 from Naverone','attic','PG'),(83,'Bambi','attic','U'),(84,'Jack Reacher','attic','12A'),(85,'Cast Away','attic','12'),(86,'Trojan Horse','attic','BLANK'),(87,'Mysterious Island','attic','BLANK'),(88,'California Man','attic','PG'),(89,'Tobruk','attic','PG'),(90,'Multiplicity','attic','12'),(91,'City of Ember','attic','PG'),(92,'The Break Up','attic','12A'),(93,'She\'s All That','attic','12'),(94,'Byzantium','attic','15'),(95,'Taken 2','attic','12A'),(96,'The Date','attic','BLANK'),(97,'Master and Commander: The Far Side of the World','attic','12A'),(98,'Goldeneye','attic','12'),(99,'The Twilight Saga: Breaking Dawn Part 1','attic','12A'),(100,'Wrath of the Titans','attic','12A'),(101,'The Twilight Saga: Breaking Dawn Part 2','attic','12A'),(102,'The Man in the Iron Mask','attic','12'),(103,'Mirror Mirror','attic','PG'),(104,'The Spy  Who Loved Me','attic','PG'),(105,'The Mummy Returns','attic','12'),(106,'Hulk','attic','12A'),(107,'Deep Impact','attic','12'),(108,'The Longest Day','attic','U'),(109,'17 Again','attic','12A'),(110,'The Day the Earth Stood Still','attic','BLANK'),(111,'Goldfinger','attic','PG'),(112,'Gravity','attic','12A'),(113,'Transformers: Revenge of the Fallen','attic','12A'),(114,'Captain Phillips','attic','12A'),(115,'War of the Buttons','attic','PG'),(116,'Space Chimps','attic','U'),(117,'Legally Blonde','attic','PG'),(118,'Von Ryan\'s Express','attic','PG'),(119,'Private Peaceful','attic','12A'),(120,'Overboard','attic','PG'),(121,'Star Trek: Wrath of Khan','attic','PG'),(122,'Imagine That','attic','PG'),(123,'Bend it like Beckham','attic','12A'),(124,'Clear and Present Danger','attic','12'),(125,'The Spy Next Door','attic','PG'),(126,'The Scorpion King','attic','12A'),(127,'Quantum Solace','attic','12A'),(128,'Uncle Buck','attic','12'),(129,'Step Up','attic','PG'),(130,'The Hunger Games: Catching Fire','attic','12A'),(131,'Under Siege','attic','15'),(132,'The Legend of Hercules (2014)','attic','12A'),(133,'Universal Soldier','attic','15'),(134,'The Purge','attic','15'),(135,'Presumed Innocent','attic','15'),(136,'Transcendence','attic','12A'),(137,'Firefox','attic','PG'),(138,'Penguins','attic','BLANK'),(139,'The Devil\'s Advocate','attic','18'),(140,'Star Trek: Into Darkness','attic','12A'),(141,'West Side Story','attic','U'),(142,'The Love Punch','attic','12A'),(143,'The Commitments','attic','15'),(144,'Teen Wolf','attic','PG'),(145,'The Net','attic','12'),(146,'Tir Na N¢g','attic','U'),(147,'The Producers','attic','12A'),(148,'E. T. the Extra-Terrestrial','attic','U'),(149,'Monsters University','attic','U'),(150,'White House Down','attic','12A'),(151,'Speed','attic','15'),(152,'A Million Ways to Die in the West','attic','15'),(153,'Ryan\'s Daughter','attic','15'),(154,'Cowboys & Aliens','attic','12A'),(155,'High Rise','attic','15'),(156,'Guardians of the Galaxy','attic','12A'),(157,'Patriot Games','attic','15'),(158,'Miss Congeniality','attic','12'),(159,'The Place Beyond','attic','BLANK'),(160,'The Maze Runner','attic','12A'),(161,'2001: A Space Odyssey','attic','U'),(162,'Inception','attic','12A'),(163,'Four Weddings and a Funeral','attic','15'),(164,'Ever After: A Cinderella Story','attic','PG'),(165,'Platoon','attic','18'),(166,'Mission Impossible: Rogue Nation','attic','12A'),(167,'Reservoir Dogs','attic','18'),(168,'Circle of Friends','attic','15'),(169,'The Way Way Back','attic','12A'),(170,'Wild Wild West','attic','12'),(171,'The Peanuts Movie','attic','U'),(172,'Lucy (2014)','attic','15'),(173,'Lucy (2014)','attic','15'),(174,'Mr. Holmes','attic','PG'),(175,'Postcards from the Edge','attic','15'),(176,'Maze Runner: The Scorch Trials','attic','12A'),(177,'They Shall Not Grow Old','attic','15'),(178,'Enemy of the State','attic','15'),(179,'Changing Lanes','attic','15'),(180,'Heat','attic','15'),(181,'Behind Enemy Lines','attic','12A'),(182,'What Happens in Vegas','attic','12A'),(183,'In the Line of Fire','attic','15'),(184,'Romeo & Juliet (2013)','attic','12A'),(185,'Miss Peregrine\'s Home for Peculiar Children','attic','12A'),(186,'Mission Impossible: Fallout','attic','12A'),(187,'John Wick','attic','15'),(188,'A United Kingdom','attic','12A'),(189,'Blade Runner 2049','attic','15'),(190,'A Few Good Men','attic','15'),(191,'King Lear (1983)','attic','15'),(192,'Wall Street','attic','15'),(193,'American Graffiti','attic','PG'),(194,'Tombstone','attic','15'),(195,'Sliding Doors','attic','15'),(196,'The Bidding Room','attic','BLANK'),(197,'Con Air','attic','18');
/*!40000 ALTER TABLE `attic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kitchen`
--

DROP TABLE IF EXISTS `kitchen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kitchen` (
  `id` int NOT NULL AUTO_INCREMENT,
  `film_name` varchar(80) NOT NULL,
  `location` varchar(20) NOT NULL,
  `age_rating` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `check_kitchen` CHECK (((`age_rating` in (_utf8mb4'U',_utf8mb4'PG',_utf8mb4'12',_utf8mb4'12A',_utf8mb4'15',_utf8mb4'18',_utf8mb4'BLANK')) and (`location` = _utf8mb4'kitchen')))
) ENGINE=InnoDB AUTO_INCREMENT=287 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kitchen`
--

LOCK TABLES `kitchen` WRITE;
/*!40000 ALTER TABLE `kitchen` DISABLE KEYS */;
INSERT INTO `kitchen` VALUES (1,'Scorpion King','kitchen','12'),(2,'Ordinary Criminal','kitchen','15'),(3,'The Hunt For Red October','kitchen','PG'),(4,'The Mummy','kitchen','12'),(5,'Battleship','kitchen','12'),(6,'Dark Knight Rises','kitchen','12A'),(7,'Clash of the Titans (2010)','kitchen','12A'),(8,'Men In Black 2','kitchen','PG'),(9,'Spiderman 3','kitchen','12A'),(10,'Fracture','kitchen','15'),(11,'Secret of My Success','kitchen','PG'),(12,'I Robot','kitchen','12'),(13,'We Were Soldiers','kitchen','15'),(14,'Blame it On The Bell Boy','kitchen','12'),(15,'The Dark Knight','kitchen','12A'),(16,'Life With Mikey','kitchen','PG'),(17,'10 Things I Hate About You','kitchen','12'),(18,'The Three Musketeers (2011)','kitchen','12A'),(19,'Clockwise','kitchen','PG'),(20,'Willy Wonka and The Chocolate Factory','kitchen','U'),(21,'Tomorrow Never Dies','kitchen','12'),(22,'The Four Feathers (2002)','kitchen','12A'),(23,'The Change Up','kitchen','15'),(24,'Waking Ned','kitchen','12'),(25,'Shane','kitchen','U'),(26,'The Amazing Spiderman','kitchen','12A'),(27,'Its a Wonderful Life','kitchen','U'),(28,'Man of Steel','kitchen','12A'),(29,'Iron Man 3','kitchen','12A'),(30,'Elysium','kitchen','15'),(31,'The Pianist','kitchen','15'),(32,'The Boy in the Striped Pyjamas','kitchen','12A'),(33,'The Mechanic','kitchen','15'),(34,'True Grit','kitchen','15'),(35,'Anzio','kitchen','15'),(36,'Matt Damon','kitchen','15'),(37,'Ransom','kitchen','15'),(38,'Ender\'s Game','kitchen','12A'),(39,'Marley and Me','kitchen','PG'),(40,'Mars Attacks','kitchen','15'),(41,'Unknown','kitchen','15'),(42,'Arnold Schwarzeneger','kitchen','15'),(43,'Robin Hood: Prince of Thieves','kitchen','15'),(44,'Sleepers','kitchen','15'),(45,'Just Married','kitchen','12A'),(46,'Evolution','kitchen','15'),(47,'Transformers: Dark Side of the Moon','kitchen','15'),(48,'Sabotage','kitchen','12A'),(49,'Escape Plan','kitchen','15'),(50,'Red 2','kitchen','15'),(51,'Soloman Kane','kitchen','15'),(52,'Vice Versa','kitchen','15'),(53,'Six Days, Seven Nights','kitchen','12'),(54,'Cloud Atlas','kitchen','PG'),(55,'LA Confidential','kitchen','15'),(56,'Now You See Me','kitchen','18'),(57,'Revolutionary Road','kitchen','15'),(58,'Magic','kitchen','15'),(59,'This is 40','kitchen','15'),(60,'Baby Mama','kitchen','15'),(61,'Solitary Man','kitchen','15'),(62,'Fracture','kitchen','15'),(63,'Percy Jackson: Sea of Monsters','kitchen','15'),(64,'The Lion King','kitchen','PG'),(65,'Thor','kitchen','12A'),(66,'The Bourne Identity','kitchen','12A'),(67,'Wonderlust','kitchen','15'),(68,'Last Vegas','kitchen','15'),(69,'Viki Cristina Bar','kitchen','15'),(70,'Captain America: The First Avenger','kitchen','12A'),(71,'A Good Year','kitchen','12A'),(72,'The Wolf of Wall Street','kitchen','15'),(73,'Noah','kitchen','18'),(74,'See No Evil Hear No Evil','kitchen','12A'),(75,'Morning Glory','kitchen','12'),(76,'Bruce Almighty','kitchen','12A'),(77,'Bullet','kitchen','15'),(78,'The Mask','kitchen','12'),(79,'Divergent','kitchen','15'),(80,'Von Ryan\'s Express','kitchen','15'),(81,'Wanted','kitchen','15'),(82,'47 Ronin','kitchen','15'),(83,'The Last Days on Mars','kitchen','12A'),(84,'Escape to Athena','kitchen','15'),(85,'The Adjustment Bureau','kitchen','15'),(86,'Source Code','kitchen','12A'),(87,'The Bourne Legacy','kitchen','PG'),(88,'In Time','kitchen','12A'),(89,'The Grey','kitchen','15'),(90,'Moonrise Kingdom','kitchen','12'),(91,'Hercules','kitchen','15'),(92,'Transendence','kitchen','15'),(93,'Shallow Hal','kitchen','12'),(94,'Mummy 3','kitchen','15'),(95,'Yes Man','kitchen','12A'),(96,'Clear And Present Danger','kitchen','15'),(97,'Unstoppable','kitchen','15'),(98,'The Rewrite','kitchen','15'),(99,'500 Days of Summer','kitchen','12A'),(100,'Red','kitchen','12A'),(101,'The Incredible Hulk','kitchen','12A'),(102,'The Lone Ranger','kitchen','12A'),(103,'The Terminal','kitchen','PG'),(104,'300: Rise of an Empire','kitchen','15'),(105,'Jason and the Argonauts','kitchen','12A'),(106,'The Lady in the Van','kitchen','15'),(107,'TwigÃ­n','kitchen','12A'),(108,'Captain America: The Winter Soldier','kitchen','U'),(109,'Runaway Bride','kitchen','15'),(110,'Captain Philips','kitchen','18'),(111,'The Alamo','kitchen','12A'),(112,'Serendipity','kitchen','15'),(113,'American Hustle','kitchen','15'),(114,'The Sting','kitchen','15'),(115,'Jaws 2','kitchen','12A'),(116,'Wyatt Earp','kitchen','PG'),(117,'Green Berets','kitchen','15'),(118,'Pulp Fiction','kitchen','18'),(119,'The Bridge at Remagen','kitchen','12'),(120,'The Imitation Game','kitchen','15'),(121,'The Recruit','kitchen','12A'),(122,'Eagle Eye','kitchen','15'),(123,'Along Came Polly','kitchen','12A'),(124,'Hunger Games: Mockingjay Part 1','kitchen','15'),(125,'Beautiful Creatures','kitchen','12A'),(126,'Bad Neighbours','kitchen','15'),(127,'Hanna','kitchen','18'),(128,'Maleficent','kitchen','15'),(129,'The Grand Budapest Hotel','kitchen','12A'),(130,'Miss Congeniality','kitchen','15'),(131,'Leap Year','kitchen','15'),(132,'Life As We Know It','kitchen','15'),(133,'22 Jump Street','kitchen','15'),(134,'The Last Airbender','kitchen','12A'),(135,'A Walk Among the Tombstones','kitchen','12A'),(136,'X-Men: Days of Future Past','kitchen','15'),(137,'The Fault in Our Stars','kitchen','15'),(138,'Cliffhanger','kitchen','12A'),(139,'The Wolverine','kitchen','12A'),(140,'A lincoln Vampire','kitchen','PG'),(141,'Room','kitchen','12A'),(142,'Lucy','kitchen','12A'),(143,'Far and Away','kitchen','15'),(144,'Fury','kitchen','15'),(145,'The Way Back','kitchen','18'),(146,'Safe House','kitchen','12'),(147,'Speed 2','kitchen','15'),(148,'Admission','kitchen','12A'),(149,'Book Thief','kitchen','15'),(150,'Reign of Fire','kitchen','U'),(151,'Dawn of the Planet of the Apes','kitchen','12'),(152,'The Monuments Men','kitchen','PG'),(153,'Righteous Kill','kitchen','15'),(154,'The Italian Job','kitchen','15'),(155,'Payback','kitchen','12A'),(156,'The Devil Wears Prada','kitchen','15'),(157,'The Fugitive','kitchen','15'),(158,'Contagion','kitchen','12A'),(159,'16 Blocks','kitchen','12A'),(160,'The Ladykillers','kitchen','12A'),(161,'13 going on 30','kitchen','PG'),(162,'Blended','kitchen','15'),(163,'Eraser','kitchen','PG'),(164,'The Hunger Games','kitchen','15'),(165,'Never Say Never Again','kitchen','12A'),(166,'21 Jump Street','kitchen','15'),(167,'Goldfinger','kitchen','15'),(168,'Goodfellas','kitchen','18'),(169,'Jack Ryan: Shadow Recruit','kitchen','15'),(170,'Run All Night','kitchen','12A'),(171,'Fifty Shades of Grey','kitchen','U'),(172,'K-9','kitchen','PG'),(173,'Around the World in 80 Days','kitchen','12A'),(174,'The Theory of Everything','kitchen','12A'),(175,'Exodus: Gods and Kings','kitchen','15'),(176,'Mad Max: Fury Road','kitchen','15'),(177,'Mission Impossible: Rogue Nation','kitchen','15'),(178,'Executive Decision','kitchen','PG'),(179,'Total Recall','kitchen','15'),(180,'The World is Not Enough','kitchen','12A'),(181,'Kingsman','kitchen','PG'),(182,'Lego','kitchen','PG'),(183,'Romancing the Stone','kitchen','15'),(184,'Jewel of the Nile','kitchen','15'),(185,'Demolition Man','kitchen','15'),(186,'Singing in the Rain','kitchen','15'),(187,'Big Hero 6','kitchen','15'),(188,'Brooklyn','kitchen','15'),(189,'Terminator: Genesis','kitchen','12A'),(190,'Look Who\'s Talking','kitchen','12A'),(191,'Avengers Ultron','kitchen','15'),(192,'Into The Woods','kitchen','12A'),(193,'Daddy\'s Home','kitchen','15'),(194,'Khartoum','kitchen','18'),(195,'Hunger Games: Mockingjay Part 2','kitchen','12A'),(196,'Safe House','kitchen','15'),(197,'Sherlock Homes: Game of Shadows','kitchen','15'),(198,'Sleepless in Seatle','kitchen','12A'),(199,'Jack the Giant Slayer','kitchen','15'),(200,'Gone with the Wind','kitchen','12'),(201,'Watermelon','kitchen','12A'),(202,'Super 8','kitchen','15'),(203,'The Mummy Returns','kitchen','15'),(204,'Seeker Dark is Risen','kitchen','12A'),(205,'Firewall','kitchen','PG'),(206,'The Martian','kitchen','U'),(207,'Van Helsing','kitchen','15'),(208,'The Legend of Hercules','kitchen','15'),(209,'Mission Impossible: Rogue Nation','kitchen','18'),(210,'Star Wars: Attack of the Clones','kitchen','15'),(211,'Outbreak','kitchen','15'),(212,'Presumed Innocent','kitchen','15'),(213,'True Lies','kitchen','15'),(214,'Enough','kitchen','15'),(215,'Chain Reaction','kitchen','15'),(216,'Pale Rider','kitchen','U'),(217,'Kindergarden Cop','kitchen','15'),(218,'Bridge of Spies','kitchen','15'),(219,'Star Wars: The Phantom Menace','kitchen','15'),(220,'The Martian','kitchen','15'),(221,'Allied','kitchen','12A'),(222,'Edge of Tomorrow','kitchen','15'),(223,'Fast & Furious','kitchen','12A'),(224,'Non-Stop','kitchen','15'),(225,'The Jungle Book (2016)','kitchen','15'),(226,'Cinderella','kitchen','15'),(227,'Emma','kitchen','15'),(228,'Babalyn_AD','kitchen','15'),(229,'Cruel Intentions','kitchen','15'),(230,'Rise of Guardians','kitchen','15'),(231,'The Proposal','kitchen','12A'),(232,'Armageddon','kitchen','15'),(233,'The Rock','kitchen','15'),(234,'Enemy of the State','kitchen','12A'),(235,'X-Men: Apocalypse','kitchen','15'),(236,'Independence Day 2','kitchen','12A'),(237,'Ali','kitchen','15'),(238,'Mercuy Rising','kitchen','15'),(239,'Interstellar','kitchen','15'),(240,'Lighthouse','kitchen','12A'),(241,'Me Before You','kitchen','15'),(242,'Huntsman: Winter\'s Tale','kitchen','15'),(243,'Eddie The Eagle','kitchen','15'),(244,'Jason Bourne','kitchen','12A'),(245,'Maze Runner: The Scorch Trials','kitchen','15'),(246,'Thomas Crown','kitchen','12A'),(247,'Starship Troopers','kitchen','12A'),(248,'The Departed','kitchen','15'),(249,'The Man  Who Would Be King','kitchen','15'),(250,'Big Game','kitchen','15'),(251,'Captain America: Civil War','kitchen','15'),(252,'Eye In The Sky','kitchen','15'),(253,'Railway','kitchen','15'),(254,'The Day the Earth Stood Still','kitchen','15'),(255,'Hamburger Hill','kitchen','15'),(256,'Hellboy','kitchen','15'),(257,'The Last Stand','kitchen','15'),(258,'Untouchables','kitchen','15'),(259,'LA Confidential','kitchen','15'),(260,'Legion','kitchen','15'),(261,'It Could Happen 2','kitchen','12A'),(262,'Alien Covenant','kitchen','12A'),(263,'Huntsman: Winter\'s Tale','kitchen','15'),(264,'High Plains Drifter','kitchen','12A'),(265,'Dances With Wolves','kitchen','15'),(266,'Seven Worlds, One Planet','kitchen','15'),(267,'Snow Piercer','kitchen','15'),(268,'Face/Off','kitchen','15'),(269,'Jack Reacher','kitchen','15'),(270,'Enemy at the Gates','kitchen','12A'),(271,'The Client','kitchen','15'),(272,'Kingsman 2','kitchen','12A'),(273,'The Guardian','kitchen','15'),(274,'The Unknown Girl','kitchen','15'),(275,'Star Wars: The Last Jedi','kitchen','12A'),(276,'Guardians of the Galaxy 2','kitchen','12A'),(277,'Land of Mine','kitchen','15'),(278,'The Scarlet and the Black (1983)','kitchen','PG'),(279,'Hell or High Water','kitchen','15'),(280,'Chaplin','kitchen','PG'),(281,'Full Monty','kitchen','15'),(282,'Parasite','kitchen','15'),(283,'Angel Has Fallen','kitchen','15'),(284,'The Riddle of the Sands','kitchen','PG'),(285,'Invisible Man','kitchen','15'),(286,'Alita: Battle Angel','kitchen','12A');
/*!40000 ALTER TABLE `kitchen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lounge`
--

DROP TABLE IF EXISTS `lounge`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lounge` (
  `id` int NOT NULL AUTO_INCREMENT,
  `film_name` varchar(80) NOT NULL,
  `location` varchar(20) NOT NULL,
  `age_rating` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `check_lounge` CHECK (((`age_rating` in (_utf8mb4'U',_utf8mb4'PG',_utf8mb4'12',_utf8mb4'12A',_utf8mb4'15',_utf8mb4'18',_utf8mb4'BLANK')) and (`location` = _utf8mb4'lounge')))
) ENGINE=InnoDB AUTO_INCREMENT=178 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lounge`
--

LOCK TABLES `lounge` WRITE;
/*!40000 ALTER TABLE `lounge` DISABLE KEYS */;
INSERT INTO `lounge` VALUES (1,'Eragon','lounge','PG'),(2,'Up in the air','lounge','15'),(3,'My Cousin Vinny','lounge','15'),(4,'The Invention of Lying','lounge','12'),(5,'Weekend at Bernies','lounge','12'),(6,'The Gruffalo','lounge','U'),(7,'The Gruffalo\'s Child','lounge','U'),(8,'Turner and Hooch','lounge','PG'),(9,'Constantine','lounge','15'),(10,'Inglourious Basterds','lounge','18'),(11,'2012/Top Gun','lounge','12'),(12,'Bedtime Stories','lounge','PG'),(13,'Dragonheart','lounge','PG'),(14,'The Wizard of Oz','lounge','U'),(15,'Avatar','lounge','12A'),(16,'Leap Year','lounge','PG'),(17,'Glory','lounge','15'),(18,'Clueless','lounge','12A'),(19,'Cheaper by the Dozen','lounge','PG'),(20,'Paul Blart: Mall Cop','lounge','PG'),(21,'Gladiator','lounge','15'),(22,'One Fine Day','lounge','PG'),(23,'The Guns of Naverone','lounge','PG'),(24,'The Princess Bride','lounge','PG'),(25,'300','lounge','15'),(26,'Wall Street - Money Never Sleeps','lounge','12'),(27,'Michael Collins','lounge','15'),(28,'The Breakfast Club','lounge','15'),(29,'Notting Hill','lounge','15'),(30,'Housesitter','lounge','PG'),(31,'Yes man','lounge','12'),(32,'Battle of Los Angeles','lounge','12'),(33,'The Money Pit','lounge','12'),(34,'Hancock','lounge','12'),(35,'Unbreakable','lounge','12'),(36,'10,000 BC','lounge','12'),(37,'Innerspace','lounge','PG'),(38,'Conan The Barbarian','lounge','15'),(39,'Terminator Salvation','lounge','12'),(40,'Star Wars: Episode II - Attack of the Clones','lounge','PG'),(41,'The Eagle','lounge','12'),(42,'Hope and Glory','lounge','15'),(43,'Conspiracy Theory','lounge','15'),(44,'A Knight\'s Tale','lounge','PG'),(45,'Splash','lounge','PG'),(46,'Dirty Rotten Scoundrels','lounge','PG'),(47,'The Bounty Hunter','lounge','12'),(48,'Big','lounge','12A'),(49,'Battle of Britain','lounge','PG'),(50,'Catch Me if You Can','lounge','12'),(51,'The Hangover','lounge','15'),(52,'Memphis Belle','lounge','12'),(53,'The Battle of the Bulge','lounge','U'),(54,'The Girl with the Dragon Tattoo','lounge','18'),(55,'Horrible Bosses','lounge','15'),(56,'Planet of the Apes (1968)','lounge','PG'),(57,'Tower Heist','lounge','12A'),(58,'The New World','lounge','12A'),(59,'Short Circuit','lounge','PG'),(60,'One Day','lounge','12A'),(61,'The Hangover Part II','lounge','15'),(62,'Seven Pounds','lounge','12A'),(63,'The Artist','lounge','PG'),(64,'About Last Night','lounge','15'),(65,'Apocalypto','lounge','18'),(66,'Ted','lounge','15'),(67,'Immortals','lounge','15'),(68,'Killers','lounge','12A'),(69,'Ocean\'s Twelve','lounge','12A'),(70,'The Alamo','lounge','12A'),(71,'Saving Private Ryan','lounge','15'),(72,'Das Boot','lounge','15'),(73,'Planes, Trains and Automobiles','lounge','15'),(74,'Skyfall','lounge','12A'),(75,'Iron Man','lounge','12A'),(76,'Iron Man 2','lounge','12A'),(77,'Independence Day','lounge','12'),(78,'Django Unchained','lounge','18'),(79,'Forrest Gump','lounge','12'),(80,'Troy','lounge','15'),(81,'Apocalypse Now','lounge','18'),(82,'The Count of Monte Cristo','lounge','12A'),(83,'The Meaning of Life','lounge','15'),(84,'Heartbreakers','lounge','12A'),(85,'Dredd','lounge','18'),(86,'Blue Streak','lounge','12'),(87,'The Blind Side','lounge','12A'),(88,'Basic','lounge','15'),(89,'Age of Heroes','lounge','15'),(90,'Jaws','lounge','12'),(91,'Flatliners','lounge','15'),(92,'13th Warrior','lounge','15'),(93,'Mission Impossible 2','lounge','12'),(94,'The Host','lounge','15'),(95,'Hansel & Gretel: Witch Hunters','lounge','15'),(96,'Extremely Loud & Incredibly Close','lounge','12A'),(97,'Oblivion','lounge','12A'),(98,'Men In Black','lounge','PG'),(99,'A Perfect Murder','lounge','15'),(100,'Star Trek','lounge','12A'),(101,'Once','lounge','15'),(102,'World War Z','lounge','15'),(103,'Friday the 13th','lounge','18'),(104,'Ghost','lounge','12'),(105,'Standby ','lounge','15'),(106,'The Hobbit: Desolation of Smaug','lounge','12A'),(107,'The Fifth Element','lounge','12'),(108,'Red Riding Hood','lounge','12A'),(109,'Pompeii','lounge','12A'),(110,'Goldeneye','lounge','12'),(111,'The Lone Ranger','lounge','12A'),(112,'The Amazing Spider-Man 2','lounge','12A'),(113,'Goodfellas','lounge','18'),(114,'District 9','lounge','15'),(115,'Robin Hood','lounge','12A'),(116,'Riddick','lounge','15'),(117,'Patriot Games','lounge','15'),(118,'7 Years in Tibet','lounge','PG'),(119,'Spectre','lounge','12A'),(120,'Mary Poppins','lounge','U'),(121,'Empire of the Sun','lounge','PG'),(122,'The Lincoln Lawyer','lounge','15'),(123,'12 Years a Slave','lounge','15'),(124,'Captain Corelli\'s Mandolin','lounge','15'),(125,'Lethal Weapon','lounge','18'),(126,'My Name is Emily','lounge','12A'),(127,'The Outlaw Josey Wales','lounge','15'),(128,'Air Force One','lounge','15'),(129,'Righteous Kill','lounge','15'),(130,'La La Land','lounge','12A'),(131,'American Sniper','lounge','15'),(132,'The Equalizer','lounge','15'),(133,'Poseiden','lounge','12A'),(134,'King Kong','lounge','12A'),(135,'Unforgiven','lounge','15'),(136,'Sing Street','lounge','12A'),(137,'Deepwater Horizon','lounge','12A'),(138,'Friends with Benefits','lounge','15'),(139,'Flightplan','lounge','12A'),(140,'Deadpool','lounge','15'),(141,'Total Recall','lounge','18'),(142,'Jack Ryan: Shadow Recruit','lounge','12A'),(143,'The Last of the Mohicans','lounge','15'),(144,'In the Line of Fire','lounge','12'),(145,'SWAT','lounge','12A'),(146,'Drive','lounge','18'),(147,'Gone in Sixty Seconds','lounge','12'),(148,'Stake Out','lounge','15'),(149,'Doctor Strange','lounge','12A'),(150,'Heartbreak Ridge','lounge','15'),(151,'Pulp Fiction','lounge','18'),(152,'War For The Planet Of The Apes','lounge','12'),(153,'Passengers','lounge','12A'),(154,'Mission to Mars','lounge','PG'),(155,'Signs','lounge','12A'),(156,'3:10 to Yuma','lounge','15'),(157,'Hidden Figures','lounge','PG'),(158,'Stand By Me','lounge','15'),(159,'Windtalkers','lounge','15'),(160,'Poltergeist','lounge','15'),(161,'Hacksaw Ridge','lounge','15'),(162,'Enigma','lounge','15'),(163,'The Patriot','lounge','15'),(164,'The Two Faces of January','lounge','12A'),(165,'Man Up','lounge','15'),(166,'Highlander','lounge','15'),(167,'Three Billboards Outside Ebbing, Missouri','lounge','15'),(168,'The Witness','lounge','15'),(169,'Heist','lounge','15'),(170,'The Nice Guys','lounge','15'),(171,'First Blood','lounge','15'),(172,'Buried','lounge','15'),(173,'The Commitments','lounge','15'),(174,'Rambo III','lounge','18'),(175,'Prometheus','lounge','15'),(176,'The Mission (1986)','lounge','12'),(177,'The Hurricane','lounge','15');
/*!40000 ALTER TABLE `lounge` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `passwords`
--

DROP TABLE IF EXISTS `passwords`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `passwords` (
  `username` varchar(60) NOT NULL,
  `user_password` varchar(100) NOT NULL,
  `secret` varchar(65) DEFAULT NULL,
  PRIMARY KEY (`username`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `passwords`
--

LOCK TABLES `passwords` WRITE;
/*!40000 ALTER TABLE `passwords` DISABLE KEYS */;
INSERT INTO `passwords` VALUES ('ADMIN','$2b$12$lneRdfTfBQwKgWIO1OtEfeHXBxYwG/TtEN7WT/eUAcgWxf/wp8Sdi','UJBNWD33NJJSWSKXGGPVQKV6L2ISXB7D'),('Cassie','$2b$12$uxA.C.iKGQX5N/UCUSM2TejqSnAQlgwCDaCkB.1TcjZUIect1JIHO',''),('Peter','$2b$12$TxNKN4fhMS0xa6D0TWPKP.0PxwND0KJGdFdIfY/aF82yKOnfDn8NC',NULL),('Peter Oliver','$2b$12$ctaLFTrOgRF6e.3mFgYw/uD0le75uOPc8c7GA0CJV9OvdvCEq9FwK',NULL),('Peter2','$2b$12$TxNKN4fhMS0xa6D0TWPKP.0PxwND0KJGdFdIfY/aF82yKOnfDn8NC',NULL),('Vincent','$2b$12$GohcAfue92fnqWh9x5qYlu13506hz0crI3PhXwT2GJ1Olh3XU7W/S','');
/*!40000 ALTER TABLE `passwords` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `username` varchar(60) NOT NULL,
  `date_created` datetime(6) NOT NULL,
  `is_locked` varchar(10) NOT NULL,
  `date_unlock` datetime(6) NOT NULL,
  `num_lockouts` int NOT NULL,
  `is_admin` varchar(10) NOT NULL,
  `failed_entry` int NOT NULL,
  PRIMARY KEY (`username`),
  UNIQUE KEY `username_UNIQUE` (`username`),
  CONSTRAINT `check_admin` CHECK ((((`username` = _utf8mb4'ADMIN') and (`is_admin` = _utf8mb4'True')) or (`is_admin` = _utf8mb4'False'))),
  CONSTRAINT `check_dates` CHECK (((`is_locked` = _utf8mb4'True') or (`date_created` = `date_unlock`))),
  CONSTRAINT `check_failed_entry` CHECK (((`failed_entry` >= 0) and (`failed_entry` <= 3))),
  CONSTRAINT `check_is_locked` CHECK (((`is_locked` = _utf8mb4'True') or (`is_locked` = _utf8mb4'False'))),
  CONSTRAINT `check_num_lockouts` CHECK (((`num_lockouts` >= 0) and (`num_lockouts` <= 1000)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('ADMIN','2025-08-21 13:25:21.202163','False','2025-08-21 13:25:21.202163',0,'True',0),('Cassie','2025-08-21 13:25:21.202163','False','2025-08-21 13:25:21.202163',0,'False',0),('Peter','2025-08-17 19:31:44.000000','False','2025-08-17 19:31:44.000000',0,'False',1),('Peter Oliver','2025-08-20 10:50:41.397015','False','2025-08-20 10:50:41.397015',0,'False',0),('Peter2','2025-08-17 19:31:44.000000','False','2025-08-17 19:31:44.000000',0,'False',0),('Vincent','2025-08-23 17:35:47.595155','False','2025-08-23 17:35:47.595155',0,'False',0);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-08-27 15:19:40
