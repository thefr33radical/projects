CREATE DATABASE  IF NOT EXISTS `recipes` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `recipes`;
-- MySQL dump 10.13  Distrib 5.6.24, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: recipes
-- ------------------------------------------------------
-- Server version	5.6.26-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `categories` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(50) DEFAULT NULL,
  `category_desc` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`category_id`),
  KEY `category_name_idx` (`category_name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (1,'Entree','Main course'),(2,'Desserts',NULL);
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `food_warnings`
--

DROP TABLE IF EXISTS `food_warnings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `food_warnings` (
  `warning_id` int(11) NOT NULL AUTO_INCREMENT,
  `ingredient_id` int(11) NOT NULL,
  `aversion` varchar(50) DEFAULT NULL,
  `details` varchar(1024) DEFAULT NULL,
  PRIMARY KEY (`warning_id`),
  KEY `aversion_idx` (`aversion`),
  KEY `FK_ingredient_id_idx` (`ingredient_id`),
  CONSTRAINT `FK_warnings_ingredient` FOREIGN KEY (`ingredient_id`) REFERENCES `ingredients` (`ingredient_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `food_warnings`
--

LOCK TABLES `food_warnings` WRITE;
/*!40000 ALTER TABLE `food_warnings` DISABLE KEYS */;
INSERT INTO `food_warnings` VALUES (3,1,'Gluten sensitivity',NULL);
/*!40000 ALTER TABLE `food_warnings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ingredients`
--

DROP TABLE IF EXISTS `ingredients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ingredients` (
  `ingredient_id` int(11) NOT NULL AUTO_INCREMENT,
  `ingred_name` varchar(75) NOT NULL,
  `ingred_desc` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ingredient_id`),
  KEY `ingredient_name_idx` (`ingred_name`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredients`
--

LOCK TABLES `ingredients` WRITE;
/*!40000 ALTER TABLE `ingredients` DISABLE KEYS */;
INSERT INTO `ingredients` VALUES (1,'Chicken breast halves, boneless',NULL),(2,'Flour',NULL),(3,'Olive oil',NULL),(4,'Sliced mushrooms',NULL),(5,'Butter',NULL),(6,'Marsala wine',NULL),(7,'Chicken broth',NULL),(8,'Rosemary, dried and crushed',NULL),(9,'Parsley, minced',NULL),(10,'Parmesan cheese, grated',NULL),(11,'White sugar',NULL),(12,'Egg(s)',NULL),(13,'Vanilla extract',NULL),(14,'Unsweetened cocoa powder',NULL),(15,'Salt',NULL),(16,'Baking powder',NULL),(17,'Butter, softened',NULL),(18,'Honey',NULL),(19,'Sugar, confectioners',NULL);
/*!40000 ALTER TABLE `ingredients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rec_comments`
--

DROP TABLE IF EXISTS `rec_comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rec_comments` (
  `comment_id` int(11) NOT NULL AUTO_INCREMENT,
  `recipe_id` int(11) NOT NULL,
  `date_entered` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `notes` varchar(1024) DEFAULT NULL,
  PRIMARY KEY (`comment_id`),
  KEY `date_idx` (`date_entered`),
  KEY `FK_comment_recipe_id_idx` (`recipe_id`),
  CONSTRAINT `FK_comment_recipe` FOREIGN KEY (`recipe_id`) REFERENCES `recipe_main` (`recipe_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rec_comments`
--

LOCK TABLES `rec_comments` WRITE;
/*!40000 ALTER TABLE `rec_comments` DISABLE KEYS */;
/*!40000 ALTER TABLE `rec_comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rec_ingredients`
--

DROP TABLE IF EXISTS `rec_ingredients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rec_ingredients` (
  `rec_ingredient_id` int(11) NOT NULL AUTO_INCREMENT,
  `recipe_id` int(11) NOT NULL,
  `amount` decimal(6,2) NOT NULL,
  `unit_id` int(11) NOT NULL,
  `ingredient_id` int(11) NOT NULL,
  `optional` bit(1) NOT NULL DEFAULT b'0',
  PRIMARY KEY (`rec_ingredient_id`),
  KEY `FK_ingredient_recipe_id_idx` (`recipe_id`),
  KEY `FK_recipe_ingredient_id_idx` (`ingredient_id`),
  KEY `FK_unit_id_idx_idx` (`unit_id`),
  CONSTRAINT `FK_ingredient_id_idx` FOREIGN KEY (`ingredient_id`) REFERENCES `ingredients` (`ingredient_id`) ON UPDATE CASCADE,
  CONSTRAINT `FK_recipe_id_idx` FOREIGN KEY (`recipe_id`) REFERENCES `recipe_main` (`recipe_id`) ON UPDATE CASCADE,
  CONSTRAINT `FK_unit_id_idx` FOREIGN KEY (`unit_id`) REFERENCES `units` (`unit_id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rec_ingredients`
--

LOCK TABLES `rec_ingredients` WRITE;
/*!40000 ALTER TABLE `rec_ingredients` DISABLE KEYS */;
INSERT INTO `rec_ingredients` VALUES (9,1,4.00,1,1,'\0'),(10,1,2.00,2,2,'\0'),(11,1,2.00,2,3,'\0'),(12,1,2.00,3,4,'\0'),(13,1,2.00,2,5,'\0'),(14,1,0.75,3,6,'\0'),(15,1,0.25,4,8,'\0'),(16,1,2.00,2,9,'\0'),(17,1,2.00,2,10,''),(18,2,0.50,3,3,'\0'),(19,2,1.00,3,11,'\0'),(20,2,2.00,1,12,'\0'),(21,2,1.00,4,13,'\0'),(22,2,0.33,3,14,'\0'),(23,2,0.50,3,2,'\0'),(24,2,0.25,4,15,'\0');
/*!40000 ALTER TABLE `rec_ingredients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rec_nutrition`
--

DROP TABLE IF EXISTS `rec_nutrition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rec_nutrition` (
  `recipe_id` int(11) NOT NULL,
  `serving_size` varchar(35) DEFAULT NULL,
  `calories` int(11) DEFAULT NULL,
  `saturated_fat` int(11) DEFAULT NULL,
  `total_fat` int(11) DEFAULT NULL,
  `cholesterol` int(11) DEFAULT NULL,
  `sodium` int(11) DEFAULT NULL,
  `carbohydrates` int(11) DEFAULT NULL,
  `fiber` int(11) DEFAULT NULL,
  `protein` int(11) DEFAULT NULL,
  `sugars` int(11) DEFAULT NULL,
  PRIMARY KEY (`recipe_id`),
  KEY `calories_idx` (`calories`),
  KEY `sat_fat_idx` (`saturated_fat`),
  KEY `total_fat_idx` (`total_fat`),
  KEY `sodium_idx` (`sodium`),
  KEY `sugars_idx` (`sugars`),
  KEY `fiber_idx` (`fiber`),
  KEY `carbohydrates_idx` (`carbohydrates`),
  KEY `cholesterol_idx` (`cholesterol`),
  CONSTRAINT `FK_recipe_nutrition` FOREIGN KEY (`recipe_id`) REFERENCES `recipe_main` (`recipe_id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rec_nutrition`
--

LOCK TABLES `rec_nutrition` WRITE;
/*!40000 ALTER TABLE `rec_nutrition` DISABLE KEYS */;
/*!40000 ALTER TABLE `rec_nutrition` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rec_tags`
--

DROP TABLE IF EXISTS `rec_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rec_tags` (
  `tag_id` int(11) NOT NULL AUTO_INCREMENT,
  `recipe_id` int(11) NOT NULL,
  `tag_value` varchar(50) NOT NULL,
  PRIMARY KEY (`tag_id`),
  KEY `tag_idx` (`tag_value`),
  KEY `FK_recipe_id_idx` (`recipe_id`),
  CONSTRAINT `FK_recipe_tag` FOREIGN KEY (`recipe_id`) REFERENCES `recipe_main` (`recipe_id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rec_tags`
--

LOCK TABLES `rec_tags` WRITE;
/*!40000 ALTER TABLE `rec_tags` DISABLE KEYS */;
/*!40000 ALTER TABLE `rec_tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipe_main`
--

DROP TABLE IF EXISTS `recipe_main`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recipe_main` (
  `recipe_id` int(11) NOT NULL AUTO_INCREMENT,
  `rec_title` varchar(255) NOT NULL,
  `category_id` int(11) DEFAULT NULL,
  `recipe_desc` varchar(1024) DEFAULT NULL,
  `prep_time` int(11) DEFAULT NULL,
  `cook_time` int(11) DEFAULT NULL,
  `servings` int(11) DEFAULT NULL,
  `difficulty` int(11) DEFAULT NULL,
  `directions` varchar(4096) DEFAULT NULL,
  `photo` blob,
  `source_id` int(11) DEFAULT NULL,
  `author` varchar(75) DEFAULT NULL,
  `source_rec_id` int(11) DEFAULT NULL,
  `entry_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`recipe_id`),
  KEY `recipe_title_idx` (`rec_title`),
  KEY `prep_time_idx` (`prep_time`),
  KEY `cook_time_idx` (`cook_time`),
  KEY `difficulty_idx` (`difficulty`),
  KEY `author_idx` (`author`),
  KEY `FK_recipes_source_rec_idx` (`source_rec_id`),
  KEY `FK_category_id_idx` (`category_id`),
  KEY `FK_source_id_idx` (`source_id`),
  CONSTRAINT `FK_recipes_categories` FOREIGN KEY (`category_id`) REFERENCES `categories` (`category_id`) ON UPDATE CASCADE,
  CONSTRAINT `FK_recipes_source_rec` FOREIGN KEY (`source_rec_id`) REFERENCES `recipe_main` (`recipe_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_recipes_sources` FOREIGN KEY (`source_id`) REFERENCES `sources` (`source_id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipe_main`
--

LOCK TABLES `recipe_main` WRITE;
/*!40000 ALTER TABLE `recipe_main` DISABLE KEYS */;
INSERT INTO `recipe_main` VALUES (1,'Chicken Marsala',1,'Chicken and mushrooms',20,20,4,2,'Flatten chicken breats to 1/4 inch. Place flour in a resealable plastic bag with two pieces of chicken at a time and shake to coat.Cook chicken in olive oil in a large skillet over medium heat for 3-5 minutes on each side or until the meat reaches a temparature of 170°. Remove chicken from skillet and keep warm.Use the same skillet to saute the mushrooms in butter until tender. Add the wine, parsley and rosemary. Bring mixture to a boil and cook until liquid is reduced by half. Serve chicken with mushroom sauce; sprinkle with cheese if desired. ',NULL,NULL,'Unknown',NULL,'2015-07-26 15:27:28'),(2,'Absolute Brownies',2,'Rich, chcolate brownies',25,35,16,2,'Preheat oven to 350 degrees F (175 degrees C). Grease and flour an 8 inch square pan.In a large saucepan, melt 1/2 cup butter. Remove from heat, and stir in sugar, eggs, and 1 teaspoon vanilla. Beat in 1/3 cup cocoa, 1/2 cup flour, salt, and baking powder. Spread batter into prepared pan.Bake in preheated oven for 25 to 30 minutes. Do not overcook.To Make Frosting: Combine 3 tablespoons butter, 3 tablespoons cocoa, 1 tablespoon honey, 1 teaspoon vanilla, and 1 cup confectioners\' sugar. Frost brownies while they are still warm.',NULL,2,'Unknown',NULL,'2015-07-26 15:27:28');
/*!40000 ALTER TABLE `recipe_main` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sources`
--

DROP TABLE IF EXISTS `sources`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sources` (
  `source_id` int(11) NOT NULL AUTO_INCREMENT,
  `source_name` varchar(50) NOT NULL,
  `source_type` varchar(50) DEFAULT NULL,
  `reference` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`source_id`),
  KEY `source_name_idx` (`source_name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sources`
--

LOCK TABLES `sources` WRITE;
/*!40000 ALTER TABLE `sources` DISABLE KEYS */;
INSERT INTO `sources` VALUES (1,'TasteOfHome.com','Website','http://www.tasteofhome.com'),(2,'EatingWell.com','Website','http://www.eatingwell.com'),(3,'AllRecipes','Website','http://www.allrecipes.com');
/*!40000 ALTER TABLE `sources` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `substitutions`
--

DROP TABLE IF EXISTS `substitutions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `substitutions` (
  `sub_id` int(11) NOT NULL AUTO_INCREMENT,
  `ingredient_id` int(11) NOT NULL,
  `substitution_id` int(11) NOT NULL,
  `instructions` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`sub_id`),
  UNIQUE KEY `sub_combo_idx` (`ingredient_id`,`substitution_id`),
  KEY `FK_ingredient_id_idx` (`ingredient_id`),
  KEY `FK_substitution_id_idx` (`substitution_id`),
  CONSTRAINT `FK_ingredient` FOREIGN KEY (`ingredient_id`) REFERENCES `ingredients` (`ingredient_id`) ON UPDATE CASCADE,
  CONSTRAINT `FK_substitution` FOREIGN KEY (`substitution_id`) REFERENCES `ingredients` (`ingredient_id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `substitutions`
--

LOCK TABLES `substitutions` WRITE;
/*!40000 ALTER TABLE `substitutions` DISABLE KEYS */;
INSERT INTO `substitutions` VALUES (1,6,7,'One for one substitution');
/*!40000 ALTER TABLE `substitutions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `units`
--

DROP TABLE IF EXISTS `units`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `units` (
  `unit_id` int(11) NOT NULL AUTO_INCREMENT,
  `unit_name` varchar(35) NOT NULL,
  `unit_desc` varchar(75) DEFAULT NULL,
  PRIMARY KEY (`unit_id`),
  KEY `unit_name_idx` (`unit_name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `units`
--

LOCK TABLES `units` WRITE;
/*!40000 ALTER TABLE `units` DISABLE KEYS */;
INSERT INTO `units` VALUES (1,'Each',NULL),(2,'Tablespoon(s)',NULL),(3,'Cup(s)',NULL),(4,'Teaspoon(s)',NULL);
/*!40000 ALTER TABLE `units` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'recipes'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-10-22 22:24:54



# Q1
insert into recipes.recipe_main
SELECT 
    3,
    'omlet',
    3,
    'continental',
    200,
    30,
    1,
    1,
    'fry and eat',
    '',
    3,
    'author1',
    1,
    '2019-04-21 10:01:10';
SELECT *FROM recipes.recipe_main;
select * from recipes.categories;
insert into recipes.categories select 3, 'Chilli', 'Main course';
insert into recipes.categories select 4, 'Chilli2', 'Main course';

insert into recipes.recipe_main
select 4, 'boiled egg', 3, 'boiled egg', 20, 35, 3, 2, 'boil and eat', '', 4, 'author2', 2, '2019-04-21 10:01:10';

insert into recipes.categories
select 4, 'Entree', 'Main Dinner';

insert into recipes.sources
select 4,'quora','website','http://www.quora.com';
   
select * from recipes.recipe_main;

# Q2
select * from recipes.rec_nutrition;
insert into recipes.ingredients
Values 
(20,'eggs',null),
(21,'oil',null),
(22,'salt',null),
(23,' pepper',null),
(24,'onions',null),
(25,'tomatoes',null),
(26,'ginger garlic paste',null);

insert into recipes.food_warnings
select 4, 22, 'allergic',null;

select * from recipes.food_warnings;

insert into recipes.rec_nutrition
select 3, 4, 300, 50, 95, 60, 10, 110, 40, 80, 75;
insert into recipes.rec_nutrition
select 4, 4, 300, 50, 95, 60, 10, 110, 40, 80, 75;
insert into recipes.substitutions
select 2,20,1, 'flour instead of bread';
insert into recipes.rec_comments
select 1, 3, '2019-04-04 18:10:16','use oil and butter';
insert into recipes.rec_tags
Values
(1,3,300),
(2,1,250),
(3,2,250),
(4,4,325);

select * from rec_ingredients;
insert into recipes.rec_ingredients
values
(25,3,4.00,1,20,0),
(26,3,2.00,2,21,0),
(27,3,2.00,2,22,0),
(28,3,1.00,2,23,0),
(29,3,2.00,1,24,0),
(30,3,2.00,1,25,0),
(31,3,3.00,2,26,0),
(32,3,8.00,1,27,0);
Select recipe_desc from recipes.recipe_main where recipe_id = 1;
Select * from recipes.recipe_main;
Select * from recipes.ingredients;
Select * from recipes.rec_ingredients;
Select * from recipes.rec_nutrition;

# For ingredients
select concat(a.amount,' ',a.unit_id,' ', b.ingred_name) as ingredients
from recipes.rec_ingredients as a join recipes.ingredients as b on a.ingredient_id = b.ingredient_id
where a.recipe_id = 3;

select a.rec_title, a.recipe_desc, a.directions, a.servings,a.prep_time,a.cook_time,b.*
from recipes.recipe_main as a join recipes.rec_nutrition as b on a.recipe_id = b.recipe_id
where a.recipe_id = 4;

(select group_concat(ingred_name separator ', ') as ingredients
FROM recipes.ingredients
WHERE ingredient_id in (SELECT rec_ingredient_id from recipes.rec_ingredients where recipe_id = 1));


select a.rec_title, a.recipe_desc, a.directions, a.servings,a.prep_time,a.cook_time,b.*
from recipes.recipe_main as a join recipes.rec_nutrition as b on a.recipe_id = b.recipe_id
where a.recipe_id = 3;

select a. recipe, a.category, b.tag_value
from (select a.recipe_id, a.rec_title as recipe, b.category_name as category
from recipes.recipe_main as a join recipes.categories as b on a.category_id = b.category_id) as a 
join recipes.rec_tags as b on a.recipe_id = b.recipe_id;