# SQLDataBase

A script that creates an SQLite database and fills one table with 2,000 made-up email and password pairs.

I wrote it in January 2023 to have something to run queries against while learning SQLite from Python. Nothing in it is real: both halves of every row are eight characters drawn from letters and digits, every email ends in @gmail.com, and the inserts go through ? placeholders rather than string formatting.

## Run it

    python sqlbd.py

It prints nothing. What you get is a file called mailpas.db next to the script, with one table called passwords.

## Rough edges

- Run it twice and it stops with "table passwords already exists", because the CREATE TABLE has no IF NOT EXISTS.
- random.sample draws without replacement, so no character ever repeats within an email or a password.
