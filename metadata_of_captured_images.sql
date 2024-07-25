show databases;
use metadata;
CREATE TABLE captures (
    id INT AUTO_INCREMENT PRIMARY KEY,
    filename VARCHAR(255) NOT NULL,
    metadata TEXT
);


SELECT * FROM captures;