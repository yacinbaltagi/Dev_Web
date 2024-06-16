from flask import Flask, jsonify, request
from flask_cors import CORS
import questions  
import jwt_utils

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return "Hello, world"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
    conn = questions.get_db()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM questions")
    size = cur.fetchone()[0]
    conn.close()
    return {"size": size, "scores": []}, 200

@app.route('/login', methods=['POST'])
def login():
    payload = request.get_json()
    password = payload.get('password')
    if password == 'flask123':
        token = jwt_utils.build_token()
        return jsonify({'token': token})
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/questions', methods=['POST'])
def add_question():
    response, status = questions.add_question()
    return jsonify(response), status

@app.route('/questions', methods=['GET'])
def get_all_questions():
    response, status = questions.get_all_questions()
    return response, status

if __name__ == "__main__":
    app.run(port=5001)
