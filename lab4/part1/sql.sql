
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
);


INSERT INTO users (name, age) VALUES ('Alice', 30);
INSERT INTO users (name, age) VALUES ('Bob', 25);
INSERT INTO users (name, age) VALUES ('Charlie', 28);
INSERT INTO users (name, age) VALUES ('John', 23);

SELECT * FROM users WHERE age > 25;

CREATE INDEX idx_name ON users(name);