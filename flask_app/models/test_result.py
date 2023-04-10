from flask import flash
from flask_app.models import user
from flask_app.config.mysqlconnection import connectToMySQL

class Tip:
    DB = "citizenship_test"
    def __init__(self, data):
        self.id = data['id']
        self.score = data['score']
        self.test_date = data['test_date']
        self.user_id = data['user_id']


    # @classmethod
    # def get_all_tips(cls, data):
    # query = "SELECT * FROM tips"
    # results = connectToMySQL(cls.DB).query.db(query)

    # tips = []
    # for item in results:
    #     tips.append(cls(item))
    # return tips