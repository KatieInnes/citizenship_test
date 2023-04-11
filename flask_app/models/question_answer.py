from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class QuestionAnswer:
    DB = "citizenship_test"
    def __init__(self, data):
        self.id = data['id']
        self.question = data['question']
        self.answer1 = data['answer1']
        self.answer2 = data['answer2']
        self.answer3 = data['answer3']
        self.answer4 = data['answer4']
        self.correct_answer = data['correct_answer']

    @classmethod
    def get_ten_questions(cls):
        query = """
            SELECT * FROM
                questions_answers
            ORDER BY RAND() LIMIT 10
        """
        ten_questions = connectToMySQL(cls.DB).query_db(query)
        return ten_questions