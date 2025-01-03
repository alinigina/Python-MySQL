-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: teste_bd_py
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.32-MariaDB

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
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `NOME` varchar(20) DEFAULT NULL,
  `SOBRENOME` varchar(20) DEFAULT NULL,
  `CPF` varchar(11) DEFAULT NULL,
  `EMAIL` varchar(100) DEFAULT NULL,
  `IDADE` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (0,'','','','',0),(1,'João','Silva','12345678901','email@example.com',20),(2,'Pedro','inacio','11369638890','email@example.com',20),(3,'Maria','guarezi','17340560789','email@example.com',20),(4,'José','nascimento','52374362767','email@example.com',20),(5,'Joyce','Ouriques','11111111111','Joynacio@gmail.com',39),(6,'Pedro','silva','97901810925','email@example.com',36),(7,'Vitorio','Inacio','12071075107','vitorioguarezi@gmail.com',17),(10,'Wanderson','guarezi','22222222222','wanderson@gmail.com',40),(11,'Anabelle','Camargo','76908575821','anabelle@gmail.com',17),(12,'Martinho','Vô_má','12519857190','vô_má@gmail.com',69),(13,'Adelia','Vó_lela','85707523572','Vó_lela@gmail.com',69),(15,'Gabriel','Americo','29037531050','Gabrielamerico@gmail.com',17),(16,'Fabio','Gabriel','07342680208','fabiogabriel@gmail.com',36),(17,'Maria','Aparecida','24687306270','mariaparecida@gmail.com',67),(18,'Fabiana','Gabriel','28396792867','fabianacabelos@gmail.com',27),(19,'Maria','Alexia','03267298472','marialexia@gmail.com',7),(20,'Alex','Isodoro','05439867345','alexisodoro@gmail.com',40);
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

-- Dump completed on 2025-01-03 12:09:40
