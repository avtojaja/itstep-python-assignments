-- 1. შექმენით მონაცემთა ბაზა "lesson27_hw".
CREATE DATABASE lesson27_hw;


-- 2. მონაცემთა ბაზაში შექმენით ცხრილები შესაბამისი დიზაინითა და მონაცემებით.
CREATE TABLE migrations (
    id INT PRIMARY KEY,
    distance INT,
    days INT
);

INSERT INTO migrations (id, distance, days) VALUES
(10484, 1000, 107),
(11728, 1531, 56),
(11729, 1370, 37),
(11732, 1622, 62),
(11734, 1491, 58),
(11735, 2723, 82),
(11736, 1571, 52),
(11737, 1957, 92);

CREATE TABLE sea_lions (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    species VARCHAR(100)
);

INSERT INTO sea_lions (id, name, species) VALUES
(10484, 'Ayah', 'Zalophus californianus'),
(11728, 'Spot', 'Zalophus californianus'),
(11729, 'Tiger', 'Zalophus californianus'),
(11732, 'Mabel', 'Zalophus californianus'),
(11734, 'Rick', 'Zalophus californianus'),
(11790, 'Jolee', 'Zalophus californianus');


-- 3. გამოიყენეთ ყველა სახის JOIN (JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN) და შეადარეთ შედეგები ერთმანეთს. FULL JOIN-ში გამოიყენეთ UNION და UNION ALL.

-- INNER JOIN
SELECT
    m.id,
    m.distance,
    m.days,
    s.name,
    s.species
FROM migrations m
JOIN sea_lions s ON m.id = s.id;

-- LEFT JOIN
SELECT
    m.id,
    m.distance,
    m.days,
    s.name,
    s.species
FROM migrations m
LEFT JOIN sea_lions s ON m.id = s.id;

-- RIGHT JOIN
SELECT
    m.id,
    m.distance,
    m.days,
    s.name,
    s.species
FROM migrations m
RIGHT JOIN sea_lions s ON m.id = s.id;

-- FULL JOIN (UNION-ის გამოყენებით)
SELECT
    m.id,
    m.distance,
    m.days,
    s.name,
    s.species
FROM migrations m
LEFT JOIN sea_lions s ON m.id = s.id

UNION

SELECT
    m.id,
    m.distance,
    m.days,
    s.name,
    s.species
FROM migrations m
RIGHT JOIN sea_lions s ON m.id = s.id;

-- FULL JOIN (UNION ALL – დუბლიკატებით)
SELECT
    m.id,
    m.distance,
    m.days,
    s.name,
    s.species
FROM migrations m
LEFT JOIN sea_lions s ON m.id = s.id

UNION ALL

SELECT
    m.id,
    m.distance,
    m.days,
    s.name,
    s.species
FROM migrations m
RIGHT JOIN sea_lions s ON m.id = s.id;
