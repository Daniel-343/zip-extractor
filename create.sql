DROP TABLE IF EXISTS "user";

CREATE TABLE  IF NOT EXISTS "user" (
	id serial PRIMARY KEY,
	name VARCHAR ( 50 ) NOT NULL,
	password VARCHAR ( 50 ) NOT NULL,
    company VARCHAR ( 50 ),
	customer_code INTEGER NOT NULL,
    type VARCHAR (50) NOT NULL,
    created_at DATE NOT NULL
);

INSERT INTO "user" (name, password, company, customer_code, type, created_at)
VALUES
  ('John Doe', 'password123', 'Company A', 12345, 'person', now()),
  ('Jane Smith', 'securepass', 'Company B', 67890, 'company', now()),
  ('Bob Johnson', 'pass1234', 'Company C', 54321, 'person', now()),
  ('Alice Williams', 'mypassword', '', 98765, 'person', now()),
  ('Charlie Brown', 'p@ssw0rd', 'Company B', 13579, 'company', now());

