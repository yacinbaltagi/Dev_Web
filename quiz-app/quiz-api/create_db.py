import sqlite3
import os

DATABASE = 'quiz.db'

if not os.path.exists(DATABASE):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        position INTEGER NOT NULL,
        title TEXT NOT NULL,
        text TEXT NOT NULL,
        image TEXT
    )
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS answers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_id INTEGER,
        text TEXT NOT NULL,
        isCorrect BOOLEAN NOT NULL,
        FOREIGN KEY(question_id) REFERENCES questions(id)
    )
    ''')

    conn.commit()
    conn.close()
else:
    print(f"Database {DATABASE} already exists.")
