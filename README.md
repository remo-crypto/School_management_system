# School Management System

A web-based school management system built with Flask and MySQL.

## Features

- Add new students
- Search and update student information
- Add exam marks
- View exam results
- Delete student records

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Make sure you have MySQL running with a database named 'sm'. You can run the schema from `schema.sql` or create the tables manually.

   SQL schema file: `schema.sql`

   **student table:**
   ```sql
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
   ```

   **exam table:**
   ```sql
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
   ```

3. Update the database credentials in `backend.py` if necessary.

4. Run the application:
   ```
   python app.py
   ```

5. Open your browser and go to `http://localhost:5000`

## Database Configuration

The application connects to MySQL with the following default settings:
- Host: localhost
- User: root
- Password: maoji@123
- Database: sm

Update these in `backend.py` as needed.</content>
<parameter name="filePath">c:\Users\Anansing Basumatary\School_Management\README.md