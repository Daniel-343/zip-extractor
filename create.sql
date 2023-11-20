CREATE TABLE IF NOT EXISTS "user"
(
    id serial,
    name varchar(50),
    password varchar(50)
);
INSERT INTO "user" (name, password) VALUES
('John Doe', 'password123'),
('Jane Smith', 'pass444'),
('Bob Johnson', 'qwerty789');
