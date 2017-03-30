-- MySQL dump 10.13  Distrib 5.7.9, for osx10.9 (x86_64)
--
-- Host: 127.0.0.1    Database: mydb
-- ------------------------------------------------------
-- Server version	5.7.17

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
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL,
  `password` binary(60) NOT NULL,
  `telephone` varchar(20) DEFAULT NULL,
  `settingsID` int(11) DEFAULT NULL,
  `salt` binary(65) DEFAULT NULL,
  `firstname` varchar(30) DEFAULT NULL,
  `lastname` varchar(30) DEFAULT NULL,
  `email` varchar(35) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'lyubo93','lyubo123\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0','072351251',3,NULL,NULL,NULL,NULL),(2,'alex93','$2b$12$D5xYjMr9xzIhT.V3h3n5eOS5Pdibrv2vLoA2pVWlGUPnF9R5d/jCy','0723541251',3,NULL,NULL,NULL,NULL),(3,'bogdan','$2b$12$GCVu1PauZ.rBegPP1YBbc.vm3h.3dLIPgb8ut34Eh1/BQB5z5Npyq','234152135235',3,NULL,NULL,NULL,NULL),(4,'ionut','$2b$12$skmREDAghnkmvy6nQ83o1.YoEPDtICtYF0hXFfjMQPwtP67WhESSK','7202314',3,'$2b$12$skmREDAghnkmvy6nQ83o1.\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0',NULL,NULL,NULL),(5,'alex22','$2b$12$jFQPhZhgzT6nAgs5drKzwulL4xGCQZx7E3Zc0/qzqMTruRCJZWWlK','07784247825',NULL,'$2b$12$jFQPhZhgzT6nAgs5drKzwu\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0','Alex','Orlando','alexandru.orlando@gmail.com'),(6,'ygvgyg','$2b$12$kTk/X8nXFCedHplh/rbL6emBNMZyrlEYN3GgaqoSsNvO.xEti3CrC','32593252',NULL,'$2b$12$kTk/X8nXFCedHplh/rbL6e\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0','Sara','Zain','aeaga@gmail.com'),(7,'saraz','$2b$12$DlY.DCTTwlNBgeqvII44GOd6Ft/2Pk7zjhkR79jfB8BizIsiQlnXG','07577777777',NULL,'$2b$12$DlY.DCTTwlNBgeqvII44GO\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0','sara','zain','sarazainkcl@gmail.com');
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-03-23 13:09:47
