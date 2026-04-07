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

2. Make sure you have MySQL running with a database named 'sm' and the following tables:

   **student table:**
   ```sql
   CREATE TABLE student (
       Admin_no INT PRIMARY KEY,
       Name VARCHAR(60),
       Gender CHAR(1),
       Class INT,
       Father_name VARCHAR(60),
       Mother_name VARCHAR(60),
       Contact_no VARCHAR(10),
       DOB DATE
   );
   ```

   **exam table:**
   ```sql
   CREATE TABLE exam (
       Admin_no INT PRIMARY KEY,
       Physics INT,
       Chemistry INT,
       English INT,
       CS INT,
       Hindi INT,
       Maths INT,
       Bio INT,
       Total INT,
       Pass_Fail CHAR(1)
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