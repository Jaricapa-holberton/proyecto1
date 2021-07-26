-- -------------------------------------------------------------
-- TablePlus 2.3(222)
--
-- https://tableplus.com/
--
-- Database: restaurant
-- Generation Time: 2019-05-06 12:51:15.3060
-- -------------------------------------------------------------


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


DROP TABLE IF EXISTS `categoria`;
CREATE TABLE `categoria` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `platillos`;
CREATE TABLE `platillos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(60) DEFAULT NULL,
  `precio` float DEFAULT NULL,
  `disponible` tinyint(1) DEFAULT NULL,
  `categoriaId` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `categoriaId` (`categoriaId`),
  CONSTRAINT `platillos_ibfk_1` FOREIGN KEY (`categoriaId`) REFERENCES `categoria` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `reservaciones`;
CREATE TABLE `reservaciones` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(60) NOT NULL,
  `apellido` varchar(60) NOT NULL,
  `hora` time DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `cantidadmesa` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `categoria` (`id`, `nombre`) VALUES ('1', 'Desayunos'),
('2', 'Comida'),
('3', 'Bebidas'),
('4', 'Bebidas con Alcohol'),
('5', 'Postres'),
('6', 'Ensaladas');

INSERT INTO `platillos` (`id`, `nombre`, `precio`, `disponible`, `categoriaId`) VALUES ('1', 'Pastel de Chocolate', '89', '1', '5'),
('2', '400g de Rib Eye', '199', '1', '2'),
('3', 'Refresco', '25', '1', '3'),
('4', 'Café Americano', '35', '1', '3'),
('5', 'Tequila', '89', '1', '4'),
('6', 'Vodka con Jugo', '119', '1', '4'),
('7', 'Hot Cakes (3)', '119', '1', '1'),
('8', 'Omellete', '89', '0', '1'),
('9', 'Pastel de Zanahoria', '89', '0', '5'),
('10', 'Rol de Canela', '69', '1', '5'),
('11', 'Agua de Naranja', '79', '1', '3'),
('12', 'Chuletas de Cerdo', '179', '1', '2'),
('13', 'Costillas BBQ', '189', '1', '2'),
('14', 'Huevo al Gusto', '49', '1', '1'),
('15', 'Omellete Hiervas Finas y Queso de Cabra', '79', '1', '1'),
('16', 'Jugo de Zanahoria', '49', '0', '3'),
('17', 'Jugo de Narnaja', '49', '1', '3'),
('18', 'Jugo de Toronja', '49', '1', '3'),
('19', 'Ensalada Violeta', '89', '1', '6'),
('20', 'Ensalada de Higo', '89', '1', '6'),
('21', 'Ensalada Cesar', '89', '0', '6'),
('22', 'Club Sandwich', '99', '1', '1'),
('23', 'Sandwich Salami', '119', '1', '1'),
('24', 'Filete de Pescado Róbalo', '179', '0', '2'),
('25', 'Filete de Atún ', '179', '1', '2'),
('26', 'Milanesa de Pollo', '149', '1', '2'),
('27', 'Pierna de Ternera al Horno', '199', '1', '2'),
('28', 'Café Capuchino', '45', '1', '3'),
('29', 'Café Latte', '50', '1', '3'),
('30', 'Café Expresso', '25', '1', '3'),
('31', 'Vino Tinto Francia', '89', '0', '4'),
('32', 'Vino Tinto Chile', '89', '1', '4'),
('33', 'Vino Tinto México', '89', '1', '4'),
('34', 'Vino Tinto España', '89', '0', '4'),
('35', 'Vino Tinto Argentina', '89', '1', '4');

INSERT INTO `reservaciones` (`id`, `nombre`, `apellido`, `hora`, `fecha`, `cantidadmesa`) VALUES ('1', 'Juan', 'De la torre', '10:30:00', '2019-06-28', '3'),
('2', 'Antonio', 'Hernandez', '14:00:00', '2019-07-30', '2'),
('3', 'Pedro', 'Juarez', '20:00:00', '2019-06-25', '5'),
('4', 'Mireya', 'Perez', '19:00:00', '2019-06-25', '2'),
('5', 'Jose', 'Castillo', '14:00:00', '2019-07-30', '3'),
('6', 'Maria', 'Diaz', '14:30:00', '2019-06-25', '2'),
('7', 'Clara', 'Duran', '10:00:00', '2019-07-01', '3'),
('8', 'Miriam', 'Ibañez', '09:00:00', '2019-07-01', '3'),
('9', 'Samuel ', 'Reyes', '10:00:00', '2019-07-02', '2'),
('10', 'Joaquin', 'Muñoz', '19:00:00', '2019-06-28', '3'),
('11', 'Julia', 'Lopez', '08:00:00', '2019-06-25', '3'),
('12', 'Carmen', 'Ruiz', '20:00:00', '2019-07-01', '4'),
('13', 'Isaac', 'Sala', '09:00:00', '2019-07-30', '3'),
('14', 'Ana', 'Preciado', '14:30:00', '2019-06-28', '4'),
('15', 'Sergio', 'Iglesias', '10:00:00', '2019-07-02', '2'),
('16', 'Aina', 'Acosta', '14:00:00', '2019-07-30', '3'),
('17', 'Carlos', 'Ortiz', '20:00:00', '2019-06-25', '2'),
('18', 'Roberto', 'Serrano', '10:00:00', '2019-07-30', '4'),
('19', 'Carlota', 'Perez', '14:00:00', '2019-07-01', '2'),
('20', 'Ana Maria', 'Igleias', '14:00:00', '2019-07-02', '2'),
('21', 'Jaime', 'Jimenez', '14:00:00', '2019-07-01', '4'),
('22', 'Roberto ', 'Torres', '10:00:00', '2019-07-02', '3'),
('23', 'Juan', 'Cano', '09:00:00', '2019-07-02', '5'),
('24', 'Santiago', 'Hernandez', '19:00:00', '2019-06-28', '5'),
('25', 'Berta', 'Gomez', '09:00:00', '2019-07-01', '3'),
('26', 'Miriam', 'Dominguez', '19:00:00', '2019-06-28', '3'),
('27', 'Antonio', 'Castro', '14:30:00', '2019-07-02', '2'),
('28', 'Hugo', 'Alonso', '09:00:00', '2019-06-28', '2'),
('29', 'Victoria', 'Perez', '10:00:00', '2019-07-02', '1'),
('30', 'Jimena', 'Leon', '10:30:00', '2019-07-30', '2'),
('31', 'Raquel ', 'Peña', '20:30:00', '2019-06-25', '3');




/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;