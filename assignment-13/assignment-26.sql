-- თუ არ გაქვთ შექმნილი, შექმენით მონაცემთა ბაზა სახელად hw_26 და შეასრულეთ შემდეგი დავალებები:
CREATE DATABASE hw_26;


-- 1. დაწერეთ SQL, რომელიც შექმნის Authors ცხრილს, რომელსაც ექნება პირველადი გასაღები.
CREATE TABLE Authors (
    AuthorID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    Country VARCHAR(50)
);


-- 2. დაწერეთ SQL, რომელიც შექმნის Books ცხრილს, სადაც გექნებათ მეორადი გასაღები AuthorID.
CREATE TABLE Books (
    BookID INT PRIMARY KEY AUTO_INCREMENT,
    Title VARCHAR(150) NOT NULL,
    PublishedYear INT,
    AuthorID INT,
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID)
);


-- 3. დაწერეთ SQL Author და Books ცხრილებისთვის, სადაც შექმნით მინიმუმ 5 ჩანაწერს.
INSERT INTO Authors (Name, Country) VALUES
('George Orwell', 'UK'),
('J.K. Rowling', 'UK'),
('Ernest Hemingway', 'USA'),
('Fyodor Dostoevsky', 'Russia'),
('Gabriel Garcia Marquez', 'Colombia');

INSERT INTO Books (Title, PublishedYear, AuthorID) VALUES
('1984', 1949, 1),
('Animal Farm', 1945, 1),
('Harry Potter', 1997, 2),
('The Old Man and the Sea', 1952, 3),
('Crime and Punishment', 1866, 4);


-- 4. დაწერეთ SQL Books ცხრილისთვის, სადაც გამოიყენებთ update ბრძანებას და გაანახლებთ კონკრეტული ჩანაწერის ერთ-ერთი ველის მნიშვნელობას.
UPDATE Books
SET PublishedYear = 1950
WHERE Title = 'Harry Potter';


-- 5. დაწერეთ SQL, რომელიც დაბეჭდავს გაერთიანებულ ცხრილებს.
SELECT
    Authors.Name AS AuthorName,
    Authors.Country,
    Books.Title,
    Books.PublishedYear
FROM Authors
JOIN Books ON Authors.AuthorID = Books.AuthorID;


-- 6. წაშალეთ ყველა ჩანაწერი Author და Books ცხრილიდან.
DELETE FROM Books;
DELETE FROM Authors;


-- 7. წაშალეთ Author და Books ცხრილები.
DROP TABLE Books;
DROP TABLE Authors;
