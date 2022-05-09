-- MySQL dump 10.13  Distrib 8.0.28, for Linux (x86_64)
--
-- Host: localhost    Database: oauth2
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Dumping data for table `alembic_version`
--

-- -- LOCK TABLES `alembic_version` WRITE;
-- /*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
-- INSERT INTO `alembic_version` VALUES ('809e204fe6b7');
-- /*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
-- -- UNLOCK TABLES;

--
-- Dumping data for table `oauth2_client`
--

-- LOCK TABLES `oauth2_client` WRITE;
/*!40000 ALTER TABLE `oauth2_client` DISABLE KEYS */;
INSERT INTO `oauth2_client` VALUES (1,'1','xxx','教学管理系统',1),(2,'2','123','学生管理系统',1);
/*!40000 ALTER TABLE `oauth2_client` ENABLE KEYS */;
-- UNLOCK TABLES;

--
-- Dumping data for table `oauth2_configuration`
--

-- LOCK TABLES `oauth2_configuration` WRITE;
/*!40000 ALTER TABLE `oauth2_configuration` DISABLE KEYS */;
INSERT INTO `oauth2_configuration` VALUES (1,NULL,NULL,NULL,NULL,'asdfasdfasdf','asdfasdfasdf',99999);
/*!40000 ALTER TABLE `oauth2_configuration` ENABLE KEYS */;
-- UNLOCK TABLES;

--
-- Dumping data for table `oauth2_user`
--

-- LOCK TABLES `oauth2_user` WRITE;
/*!40000 ALTER TABLE `oauth2_user` DISABLE KEYS */;
INSERT INTO `oauth2_user` VALUES (1,'陈锡','123','20203712062','学生'),(2,'黄旭辉','123','20203712168','教师'),(3,'郑新元','123','20203712032','学生'),(4,'谢毅','123','20203712105','学生');
/*!40000 ALTER TABLE `oauth2_user` ENABLE KEYS */;
-- UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-13  4:40:49
