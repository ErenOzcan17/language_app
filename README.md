sqlite codes is here for tables
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);
CREATE TABLE languages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    language_name VARCHAR(255) NOT NULL,
    table_name VARCHAR(255) NOT NULL
);
CREATE TABLE english_language (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word VARCHAR(255) NOT NULL,
    menaning VARCHAR(255) NOT NULL
);

if you want to add a dataset do this:
Convert the source file to CSV format and execute dataset.py. This should populate the database
