BEGIN TRANSACTION;
CREATE TABLE "translators" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" TEXT,
    "surname" TEXT
);
CREATE TABLE "series" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" TEXT,
    "description" TEXT
);
CREATE TABLE "rel_translator_compositions" (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`translator_id`	INTEGER,
	`composition_id`	INTEGER
);
CREATE TABLE "rel_publisher_books" (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`publisher_id`	INTEGER,
	`book_id`	INTEGER
);
CREATE TABLE "rel_compositions_translators" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "composition_id" INTEGER,
    "translator_id" TEXT
);
CREATE TABLE "rel_composition_genres" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "composition_id" TEXT,
    "genre_id" TEXT
);
CREATE TABLE "rel_composition_authors" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "composition_id" INTEGER,
    "author_id" INTEGER
);
CREATE TABLE "rel_book_series" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "book_id" INTEGER,
    "series_id" INTEGER
);
CREATE TABLE `rel_book_genres` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`book_id`	INTEGER,
	`genre_id`	INTEGER
);
CREATE TABLE "rel_book_editors" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "book_id" TEXT,
    "editor_id" TEXT
);
CREATE TABLE rel_book_compositions (
    "id" INTEGER NOT NULL,
    "composition_id" INTEGER,
    "book_id" INTEGER
);
CREATE TABLE "publishers" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" TEXT,
    "url" TEXT,
    "city" TEXT
);
CREATE TABLE "genres" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" TEXT,
    "description" TEXT
);
CREATE TABLE editors (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" TEXT,
    "surname" TEXT
);
CREATE TABLE "compositions" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" TEXT,
    "annotation" TEXT
);
CREATE TABLE "books" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" TEXT,
    "isbn" TEXT,
    "orig_name" TEXT,
    "year" TEXT,
    "note" TEXT
);
CREATE TABLE "authors" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" TEXT,
    "surname" TEXT,
    "origin_id" TEXT
);
COMMIT;
