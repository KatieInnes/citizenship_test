from flask import flash
from flask_app.models import user
from flask_app.config.mysqlconnection import connectToMySQL

class Tip:
    def __init__(self, data):
        self.id = data['id']
        self.advice = data['advice']
        self.user = data['user_id']

    @staticmethod
    def validate_tip(tip):
        is_valid = True

        if len(tip['advice']) < 5:
            flash("Advice must be at least 5 characters.")
            is_valid = False

        return is_valid

    @classmethod
    def get_all(cls, data):
        query = """"

        """"

    @classmethod
    def get_one(cls, data):
        query = """"

        """"

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO 
            advice 
            (advice, user_id) 
        VALUES
            (%(advice)s, %(user_id)s)
        """
        return connectToMySQL("citizenship_test").query_db(query, data)