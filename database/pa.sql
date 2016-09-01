-- MySQL dump 10.13  Distrib 5.5.50, for debian-linux-gnu (armv7l)
--
-- Host: localhost    Database: pa
-- ------------------------------------------------------
-- Server version	5.5.50-0+deb8u1

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
-- Table structure for table `shows`
--

DROP TABLE IF EXISTS `shows`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shows` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(100) NOT NULL,
  `season` int(11) NOT NULL,
  `episode` int(11) NOT NULL,
  `ref` int(11) NOT NULL,
  `link` varchar(2000) DEFAULT NULL,
  `comment` char(255) DEFAULT NULL,
  `last_update` int(11) DEFAULT NULL,
  `seen` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shows`
--

LOCK TABLES `shows` WRITE;
/*!40000 ALTER TABLE `shows` DISABLE KEYS */;
INSERT INTO `shows` VALUES (1,'Suits',6,8,10910,'ed2k://|file|%E8%AF%89%E8%AE%BC%E5%8F%8C%E9%9B%84.Suits.S06E08.%E4%B8%AD%E8%8B%B1%E5%AD%97%E5%B9%95.HR-HDTV.AC3.1024X576.x264.mp4|421298348|fb69d764a0cc776569d586bcb51dd60c|h=ktwmf522abkoo7ltd4xuelb35ojzf3dh|/','None',1472738293,1),(4,'NinjaTurtle',4,17,28360,'ed2k://|file|%E5%BF%8D%E8%80%85%E7%A5%9E%E9%BE%9F.Teenage.Mutant.Ninja.Turtles.2012.S04E17.WEB-HR.AAC.1024X576.x264.mp4|226992554|67a39f416fbe0b223c58740a48b8de5e|h=4l7fey2b6fn4knjt5azwi27u6th6dxmz|/','',1472755522,1),(5,'RickAndMorty',3,0,31346,'','',0,1),(6,'Shield',4,0,30675,'','',0,1),(7,'Veep',6,0,27963,'','',0,1),(8,'TheOddCouple',3,0,33316,'','',0,1),(9,'Supernatural',12,0,11015,'ed2k://|file|%E5%87%B6%E9%AC%BC%E6%81%B6%E7%81%B5.Supernatural.S11E01.%E4%B8%AD%E8%8B%B1%E5%AD%97%E5%B9%95.WEB-HR.AC3.1024X576.x264.mp4|424323446|3111d94f8122b2808a1eea3a1054a28a|h=mkmiwlsy7eslszzdcjle3wkprgxblqlw|/','',0,1),(10,'Wrecked',2,0,34528,'','',0,1),(11,'TheFlash',3,0,32235,'','',0,1),(12,'GameOfThrones',7,0,10733,'','',0,1),(13,'Siblings',2,1,32580,'','',0,1),(14,'TheBlacklist',4,0,29964,'','',0,1),(15,'BlooklynNineNine',4,0,30722,'','',0,1),(16,'Scorpion',3,0,32763,'','',0,1),(17,'TBBT',10,0,11005,'','',0,1),(18,'NewGirl',6,0,10974,'','',0,1);
/*!40000 ALTER TABLE `shows` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-09-01 22:00:14
