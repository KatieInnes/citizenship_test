from flask import flash
from flask_app.models import user
from flask_app.config.mysqlconnection import connectToMySQL

class Test_Result:
    DB = "citizenship_test"
    def __init__(self, data):
        self.id = data['id']
        self.score = data['score']
        self.test_date = data['test_date']
        self.user_id = data['user_id']

    @classmethod
    def get_all_scores(cls): 
        query = "SELECT * FROM test_results"
        results = connectToMySQL(cls.DB).query_db(query)

        scores = []
        for score in results:
            scores.append(score)
        return scores

    @classmethod
    def get_scores_for_logged_in_user(cls, data):
        query = """
            SELECT * FROM 
                test_results
            WHERE user_id = %(id)s
        """
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result