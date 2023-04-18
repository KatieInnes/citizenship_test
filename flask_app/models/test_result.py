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
            ORDER BY test_date DESC
        """
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result

    @classmethod
    def most_recent_score_for_logged_in_user(cls, data):
        query = """
            SELECT score FROM 
                test_results
            WHERE user_id = %(id)s
            ORDER BY test_date DESC
            LIMIT 1
        """
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result


    @classmethod
    def save_new_score(cls, data):
        query = """
            INSERT INTO
                test_results
                (score, user_id)
            VALUES 
                (%(score)s, %(user_id)s)
        """
        return connectToMySQL(cls.DB).query_db(query, data)
