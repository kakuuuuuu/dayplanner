CREATE DATABASE  IF NOT EXISTS `planner` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `planner`;
-- MySQL dump 10.13  Distrib 5.7.9, for osx10.9 (x86_64)
--
-- Host: 127.0.0.1    Database: planner
-- ------------------------------------------------------
-- Server version	5.5.42

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
-- Table structure for table `activities`
--

DROP TABLE IF EXISTS `activities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `activities` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(45) DEFAULT NULL,
  `duration` time DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `price` varchar(45) DEFAULT NULL,
  `plan_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_activities_plans_idx` (`plan_id`),
  CONSTRAINT `fk_activities_plans` FOREIGN KEY (`plan_id`) REFERENCES `plans` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=106 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `activities`
--

LOCK TABLES `activities` WRITE;
/*!40000 ALTER TABLE `activities` DISABLE KEYS */;
INSERT INTO `activities` VALUES (87,'Starting Point',NULL,'439 North Fairfax Ave','Los Angeles',NULL,109),(88,'meal',NULL,'110 N Fairfax Ave #12, Los Angeles, CA 90036, United States','Chipotle Mexican Grill',NULL,109),(89,'activity',NULL,'430 N Fairfax Ave, Los Angeles, CA 90036, United States','Norm Maxwell Studio Gallery',NULL,109),(90,'activity',NULL,'8250 Melrose Ave, Los Angeles, CA 90046, United States','Peak Sports Usa',NULL,109),(91,'meal',NULL,'8256 Beverly Blvd, Los Angeles, CA 90048, United States','Bao Dim Sum House',NULL,109),(92,'Starting Point',NULL,'','union city',NULL,110),(93,'Starting Point',NULL,'niland st','union city',NULL,111),(94,'meal',NULL,'3880 Lake Arrowhead Ave, Fremont, CA 94555, United States','China Station',NULL,111),(97,'Starting Point',NULL,'224 Traminer Court','Fremont',NULL,114),(98,'meal',NULL,'46356 Warm Springs Blvd, Fremont, CA 94539, United States','Hong Kong Chef',NULL,114),(99,'Starting Point',NULL,'1980 Zanker rd 30','San Jose',NULL,115),(100,'meal',NULL,'3927 Rivermark Plaza, Santa Clara, CA 95054, United States','Yan Can Asian Bistro',NULL,115),(101,'Starting Point',NULL,'865 Market St, San Francisco, CA 94103','San Francisco',NULL,116),(102,'meal',NULL,'1063 Market St, San Francisco, CA 94102, United States','Oriental Restaurant',NULL,116),(103,'activity',NULL,'88 5th St, San Francisco, CA 94103, United States','San Francisco Museum and Historical Society',NULL,116),(104,'activity',NULL,'865 Market St, San Francisco, CA 94103, United States','Vans',NULL,116),(105,'meal',NULL,'1655 Post St, San Francisco, CA 94115, United States','SEOUL GARDEN',NULL,116);
/*!40000 ALTER TABLE `activities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `plans`
--

DROP TABLE IF EXISTS `plans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `plans` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `city` varchar(255) DEFAULT NULL,
  `start_time` time DEFAULT NULL,
  `end_time` time DEFAULT NULL,
  `start_location` varchar(255) DEFAULT NULL,
  `transportation` varchar(255) DEFAULT NULL,
  `users_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_plans_users1_idx` (`users_id`),
  CONSTRAINT `fk_plans_users1` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=117 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plans`
--

LOCK TABLES `plans` WRITE;
/*!40000 ALTER TABLE `plans` DISABLE KEYS */;
INSERT INTO `plans` VALUES (109,'Los Angeles','00:00:00','00:00:00','439 North Fairfax Ave','300',9),(110,'union city','00:00:00','00:00:00','','20',10),(111,'union city','00:00:00','00:00:00','niland st','20',10),(114,'Fremont','00:00:00','00:00:00','224 Traminer Court','20',7),(115,'San Jose','00:00:00','00:00:00','1980 Zanker rd 30','20',7),(116,'San Francisco','00:00:00','00:00:00','865 Market St, San Francisco, CA 94103','20',7);
/*!40000 ALTER TABLE `plans` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'user1','email1@abc.com','$2b$12$IbA14eDE1LIjy21pWavRe.OG5XfWoDsL7cqQnJmi26PDOq4/Q0K5O'),(2,'user2','email2@abc.com','$2b$12$mnqOOk06gN6LmQMVuSJ4qOm9O8xy1VzC2SeNT4GVocA.MDocOIKtS'),(3,'user3','email3@abc.com','$2b$12$bHLClDEYCfhzcbGvL.B84.vmxIdgXpdQwHl3VS/hMtMpY4WJZR0He'),(4,'shannon beck','sbeck@clemson.edu','$2b$12$2l015GyKFV5WC.5Q1ObuQe510vzXmQ1dO6a/ncFvLW5abxxkFBTju'),(5,'Kyle','kt.fremont@gmail.com','$2b$12$t835hVfAKwmdUgvSHqdLWOd3yCyY5wcobJLciju2XALxsLj0KEVyu'),(7,'Kyle','kt.fremont@comcast.net','$2b$12$Bk4WEtpAQFH058VBzOOGnODQ5A5V1m85VQozsFmkFvEYr4RP5pnkG'),(8,'Derek','drock@gmail.com','$2b$12$EH/yZjKIEiWTGD1FPkMHuO1u0W7zVUNz4hawe0.TKLwGMJOmiEVWq'),(9,'Frank','frank@gmail.com','$2b$12$fcTF3VszaYJYmOv5wNz2buP0N0E9Ej45TPnYBs0wA1JILPRuBiWFa'),(10,'ashj','abc@gmail.com','$2b$12$H4vWbAXXXorrHqtb.iQO1eK4trwd2jG/rfXELDciw4sKtguxpXBn.');
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

-- Dump completed on 2016-05-26  0:24:18
