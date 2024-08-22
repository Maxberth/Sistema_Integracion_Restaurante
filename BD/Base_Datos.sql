-- MySQL dump 10.13  Distrib 8.2.0, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: mimanuela
-- ------------------------------------------------------
-- Server version	8.2.0

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
-- Table structure for table `administrador`
--

DROP TABLE IF EXISTS `administrador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administrador` (
  `Id_administrador` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(100) DEFAULT NULL,
  `Papellido` varchar(100) DEFAULT NULL,
  `Sapellido` varchar(100) DEFAULT NULL,
  `Usuario` varchar(50) DEFAULT NULL,
  `Contraseña` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Id_administrador`),
  UNIQUE KEY `Usuario` (`Usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrador`
--

LOCK TABLES `administrador` WRITE;
/*!40000 ALTER TABLE `administrador` DISABLE KEYS */;
INSERT INTO `administrador` VALUES (2,'Jhony','Lozano','Quiroz','admi','admi6910');
/*!40000 ALTER TABLE `administrador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `boleta`
--

DROP TABLE IF EXISTS `boleta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `boleta` (
  `Id_boleta` int NOT NULL AUTO_INCREMENT,
  `Id_pedido` int DEFAULT NULL,
  `Fecha` datetime DEFAULT NULL,
  `MontoTotal` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`Id_boleta`),
  KEY `Id_pedido` (`Id_pedido`),
  CONSTRAINT `boleta_ibfk_1` FOREIGN KEY (`Id_pedido`) REFERENCES `pedido` (`Id_pedido`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `boleta`
--

LOCK TABLES `boleta` WRITE;
/*!40000 ALTER TABLE `boleta` DISABLE KEYS */;
/*!40000 ALTER TABLE `boleta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `Id_cliente` int NOT NULL AUTO_INCREMENT,
  `Dni` varchar(50) DEFAULT NULL,
  `Nombre` varchar(100) DEFAULT NULL,
  `Papellido` varchar(100) DEFAULT NULL,
  `Sapellido` varchar(100) DEFAULT NULL,
  `NumeroCel` varchar(15) DEFAULT NULL,
  `CorreoPer` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Id_cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES (19,'70605040','Javier','Suarez','Bodero','926759813','correo@hot.com');
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cocinero`
--

DROP TABLE IF EXISTS `cocinero`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cocinero` (
  `Id_cocinero` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(100) DEFAULT NULL,
  `Papellido` varchar(100) DEFAULT NULL,
  `Sapellido` varchar(100) DEFAULT NULL,
  `Usuario` varchar(50) DEFAULT NULL,
  `Contraseña` varchar(100) DEFAULT NULL,
  `Id_administrador` int DEFAULT NULL,
  PRIMARY KEY (`Id_cocinero`),
  UNIQUE KEY `Usuario` (`Usuario`),
  KEY `Id_administrador` (`Id_administrador`),
  CONSTRAINT `cocinero_ibfk_1` FOREIGN KEY (`Id_administrador`) REFERENCES `administrador` (`Id_administrador`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cocinero`
--

LOCK TABLES `cocinero` WRITE;
/*!40000 ALTER TABLE `cocinero` DISABLE KEYS */;
INSERT INTO `cocinero` VALUES (15,'Carlos','Ruiz','Sanchez','cocinero1','carlos586',2),(18,'Alberth','Gutierrez','Pia','cocinero2','1234',2);
/*!40000 ALTER TABLE `cocinero` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detallepedido`
--

DROP TABLE IF EXISTS `detallepedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detallepedido` (
  `Id_detalle` int NOT NULL AUTO_INCREMENT,
  `Id_pedido` int DEFAULT NULL,
  `Id_platillo` int DEFAULT NULL,
  `Cantidad` int DEFAULT NULL,
  PRIMARY KEY (`Id_detalle`),
  KEY `Id_pedido` (`Id_pedido`),
  KEY `Id_platillo` (`Id_platillo`),
  CONSTRAINT `detallepedido_ibfk_1` FOREIGN KEY (`Id_pedido`) REFERENCES `pedido` (`Id_pedido`),
  CONSTRAINT `detallepedido_ibfk_2` FOREIGN KEY (`Id_platillo`) REFERENCES `platillo` (`Id_platillo`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detallepedido`
--

LOCK TABLES `detallepedido` WRITE;
/*!40000 ALTER TABLE `detallepedido` DISABLE KEYS */;
/*!40000 ALTER TABLE `detallepedido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estadopedido`
--

DROP TABLE IF EXISTS `estadopedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estadopedido` (
  `Id_estado` int NOT NULL AUTO_INCREMENT,
  `Estado` varchar(50) NOT NULL,
  PRIMARY KEY (`Id_estado`)
) ENGINE=InnoDB AUTO_INCREMENT=70 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estadopedido`
--

LOCK TABLES `estadopedido` WRITE;
/*!40000 ALTER TABLE `estadopedido` DISABLE KEYS */;
INSERT INTO `estadopedido` VALUES (69,'proceso');
/*!40000 ALTER TABLE `estadopedido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mesa`
--

DROP TABLE IF EXISTS `mesa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mesa` (
  `Id_mesa` int NOT NULL AUTO_INCREMENT,
  `Capacidad` int DEFAULT NULL,
  `Ubicacion` int DEFAULT NULL,
  PRIMARY KEY (`Id_mesa`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mesa`
--

LOCK TABLES `mesa` WRITE;
/*!40000 ALTER TABLE `mesa` DISABLE KEYS */;
INSERT INTO `mesa` VALUES (5,4,1);
/*!40000 ALTER TABLE `mesa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mesero`
--

DROP TABLE IF EXISTS `mesero`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mesero` (
  `Id_mesero` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(100) DEFAULT NULL,
  `Papellido` varchar(100) DEFAULT NULL,
  `Sapellido` varchar(100) DEFAULT NULL,
  `Usuario` varchar(50) DEFAULT NULL,
  `Contraseña` varchar(100) DEFAULT NULL,
  `Id_administrador` int DEFAULT NULL,
  PRIMARY KEY (`Id_mesero`),
  UNIQUE KEY `Usuario` (`Usuario`),
  KEY `Id_administrador` (`Id_administrador`),
  CONSTRAINT `mesero_ibfk_1` FOREIGN KEY (`Id_administrador`) REFERENCES `administrador` (`Id_administrador`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mesero`
--

LOCK TABLES `mesero` WRITE;
/*!40000 ALTER TABLE `mesero` DISABLE KEYS */;
INSERT INTO `mesero` VALUES (20,'Alberth','Bigo','Ruiz','mesero1','1234',2),(22,'carlos','perez','chunga','mesero4','1234',2);
/*!40000 ALTER TABLE `mesero` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pedido`
--

DROP TABLE IF EXISTS `pedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pedido` (
  `Id_pedido` int NOT NULL AUTO_INCREMENT,
  `Id_mesero` int DEFAULT NULL,
  `Id_mesa` int DEFAULT NULL,
  `Id_cliente` int DEFAULT NULL,
  `Fecha` date DEFAULT NULL,
  `MontoTotal` decimal(10,2) DEFAULT NULL,
  `Id_estado` int DEFAULT NULL,
  `cantidad` int DEFAULT NULL,
  PRIMARY KEY (`Id_pedido`),
  KEY `Id_mesero` (`Id_mesero`),
  KEY `Id_mesa` (`Id_mesa`),
  KEY `Id_cliente` (`Id_cliente`),
  KEY `Id_estado` (`Id_estado`),
  CONSTRAINT `pedido_ibfk_1` FOREIGN KEY (`Id_mesero`) REFERENCES `mesero` (`Id_mesero`),
  CONSTRAINT `pedido_ibfk_2` FOREIGN KEY (`Id_mesa`) REFERENCES `mesa` (`Id_mesa`),
  CONSTRAINT `pedido_ibfk_3` FOREIGN KEY (`Id_cliente`) REFERENCES `cliente` (`Id_cliente`),
  CONSTRAINT `pedido_ibfk_4` FOREIGN KEY (`Id_estado`) REFERENCES `estadopedido` (`Id_estado`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pedido`
--

LOCK TABLES `pedido` WRITE;
/*!40000 ALTER TABLE `pedido` DISABLE KEYS */;
/*!40000 ALTER TABLE `pedido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `platillo`
--

DROP TABLE IF EXISTS `platillo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `platillo` (
  `Id_platillo` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(100) DEFAULT NULL,
  `Precio` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`Id_platillo`)
) ENGINE=InnoDB AUTO_INCREMENT=667 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `platillo`
--

LOCK TABLES `platillo` WRITE;
/*!40000 ALTER TABLE `platillo` DISABLE KEYS */;
INSERT INTO `platillo` VALUES (1,'Aji de gallina',10.00),(2,'Lomito  saltado de carne',18.00),(3,'Tallarinas verdes con pollo',12.00),(4,'Tallarines verdes con carne',18.00),(5,'Chicharron de pollo',12.00),(6,'Milanesa de pollo',14.00),(7,'Filete de pollo',12.00),(8,'Tallarin saltado de pollo',12.00),(9,'Chuleta frita',18.00),(10,'Arroz chaufa de pollo',14.00),(11,'Arroz chaufa de chancho',18.00),(30,'Tallarin saltado de carne',18.00),(31,'Pescado apanado',16.00),(32,'Tallarines rojos',12.00),(33,'Biztec a lo pobre',22.00);
/*!40000 ALTER TABLE `platillo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-21 23:06:39
