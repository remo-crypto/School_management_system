CREATE TABLE `student` (
  `Admin_no` int NOT NULL,
  `Name` varchar(30) DEFAULT NULL,
  `Gender` char(1) DEFAULT NULL,
  `Class` int DEFAULT NULL,
  `Father_name` varchar(30) DEFAULT NULL,
  `Mother_name` varchar(30) DEFAULT NULL,
  `Contact_no` char(10) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  PRIMARY KEY (`Admin_no`)
);

CREATE TABLE `exam` (
  `Admin_no` int DEFAULT NULL,
  `Physics` int DEFAULT (0),
  `Chemistry` int DEFAULT (0),
  `English` int DEFAULT (0),
  `cs` int DEFAULT (0),
  `Hindi` int DEFAULT (0),
  `Maths` int DEFAULT (0),
  `Bio` int DEFAULT (0),
  `Total` int DEFAULT NULL,
  `Pass_Fail` char(1) DEFAULT NULL,
  KEY `Admin_no` (`Admin_no`),
  CONSTRAINT `exam_ibfk_1` FOREIGN KEY (`Admin_no`) REFERENCES `student` (`Admin_no`) ON DELETE CASCADE ON UPDATE CASCADE
);
