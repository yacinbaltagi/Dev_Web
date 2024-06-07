import sqlite3
import os

# Nom du fichier de base de données
DATABASE = 'quiz.db'

# Vérifiez si le fichier existe déjà
if not os.path.exists(DATABASE):
    # Connexion à la base de données
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()

    # Création de la table questions
    cur.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        position INTEGER NOT NULL,
        title TEXT NOT NULL,
        text TEXT NOT NULL,
        image TEXT
    )
    ''')

    # Création de la table answers
    cur.execute('''
    CREATE TABLE IF NOT EXISTS answers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_id INTEGER,
        text TEXT NOT NULL,
        isCorrect BOOLEAN NOT NULL,
        FOREIGN KEY(question_id) REFERENCES questions(id)
    )
    ''')

    # Fermeture de la connexion
    conn.commit()
    conn.close()
else:
    print(f"Database {DATABASE} already exists.")