DROP TABLE IF EXISTS "user";

CREATE TABLE  IF NOT EXISTS "user" (
	id serial PRIMARY KEY,
	name VARCHAR ( 50 ) NOT NULL,
	password VARCHAR ( 50 ) NOT NULL,
    company VARCHAR ( 50 ),
	customer_code INTEGER NOT NULL,
    type VARCHAR (50) NOT NULL
);

INSERT INTO "user" (name, password, company, customer_code, type)
VALUES
  ('John Doe', 'password123', 'Company A', 12345, 'person'),
  ('Jane Smith', 'securepass', 'Company B', 67890, 'company'),
  ('Bob Johnson', 'pass1234', 'Company C', 54321, 'person'),
  ('Alice Williams', 'mypassword', '', 98765, 'person'),
  ('Charlie Brown', 'p@ssw0rd', 'Company B', 13579, 'company');

