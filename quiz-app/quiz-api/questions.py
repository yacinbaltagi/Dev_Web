import sqlite3
from flask import request
import jwt_utils
from models import Question, Answer

DATABASE = 'quiz.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def add_question():
    token = request.headers.get('Authorization')
    if not token:
        return {'message': 'Token is missing!'}, 401
    try:
        jwt_utils.decode_token(token.split(" ")[1])
    except jwt_utils.JwtError as e:
        return {'message': str(e)}, 401

    question_data = request.get_json()
    question = Question.from_dict(question_data)

    conn = get_db()
    cur = conn.cursor()
    cur.execute("begin")
    try:
        cur.execute("INSERT INTO questions (position, title, text, image) VALUES (?, ?, ?, ?)",
                    (question.position, question.title, question.text, question.image))
        question_id = cur.lastrowid
        for answer in question.possibleAnswers:
            cur.execute("INSERT INTO answers (question_id, text, isCorrect) VALUES (?, ?, ?)",
                        (question_id, answer.text, answer.isCorrect))
        conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        return {'message': str(e)}, 500
    finally:
        conn.close()
    return {'id': question_id, 'message': 'Question added successfully'}, 200

def get_all_questions():
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM questions")
        rows = cur.fetchall()
        questions_list = []
        for row in rows:
            question_id = row[0]
            cur.execute("SELECT id, question_id, text, isCorrect FROM answers WHERE question_id = ?", (question_id,))
            answers = [Answer(id=ans[0], question_id=ans[1], text=ans[2], isCorrect=ans[3]) for ans in cur.fetchall()]
            question = Question(id=row[0], position=row[1], title=row[2], text=row[3], image=row[4], possibleAnswers=answers)
            questions_list.append(question.to_dict())
        conn.close()
        return questions_list, 200
    except Exception as e:
        print(f"Error retrieving questions: {e}")
        return {'message': 'Error retrieving questions'}, 500

def get_question(id):
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM questions WHERE id = ?", (id,))
        row = cur.fetchone()
        if row:
            question_id = row[0]
            cur.execute("SELECT id, question_id, text, isCorrect FROM answers WHERE question_id = ?", (question_id,))
            answers = [Answer(id=ans[0], question_id=ans[1], text=ans[2], isCorrect=ans[3]) for ans in cur.fetchall()]
            question = Question(id=row[0], position=row[1], title=row[2], text=row[3], image=row[4], possibleAnswers=answers)
            conn.close()
            return question.to_dict(), 200
        conn.close()
        return {'message': 'Question not found'}, 404
    except Exception as e:
        print(f"Error retrieving question: {e}")
        return {'message': 'Error retrieving question'}, 500

def update_question(id):
    token = request.headers.get('Authorization')
    if not token:
        return {'message': 'Token is missing!'}, 401
    try:
        jwt_utils.decode_token(token.split(" ")[1])
    except jwt_utils.JwtError as e:
        return {'message': str(e)}, 401

    question_data = request.get_json()
    question = Question.from_dict(question_data)

    conn = get_db()
    cur = conn.cursor()
    cur.execute("begin")
    try:
        cur.execute("UPDATE questions SET position = ?, title = ?, text = ?, image = ? WHERE id = ?",
                    (question.position, question.title, question.text, question.image, id))
        cur.execute("DELETE FROM answers WHERE question_id = ?", (id,))
        for answer in question.possibleAnswers:
            cur.execute("INSERT INTO answers (question_id, text, isCorrect) VALUES (?, ?, ?)",
                        (id, answer.text, answer.isCorrect))
        conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        return {'message': str(e)}, 500
    finally:
        conn.close()
    return {'message': 'Question updated successfully'}, 200

def delete_question(id):
    token = request.headers.get('Authorization')
    if not token:
        return {'message': 'Token is missing!'}, 401
    try:
        jwt_utils.decode_token(token.split(" ")[1])
    except jwt_utils.JwtError as e:
        return {'message': str(e)}, 401

    conn = get_db()
    cur = conn.cursor()
    cur.execute("begin")
    try:
        cur.execute("DELETE FROM answers WHERE question_id = ?", (id,))
        cur.execute("DELETE FROM questions WHERE id = ?", (id,))
        conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        return {'message': str(e)}, 500
    finally:
        conn.close()
    return {'message': 'Question deleted successfully'}, 200