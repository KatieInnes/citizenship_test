from flask import flash
from flask_app.models import user
from flask_app.config.mysqlconnection import connectToMySQL

class Tip:
    DB = "citizenship_test"
    def __init__(self, data):
        self.id = data['id']
        self.tip = data['tip']
        self.user_id = data['user_id']

    @staticmethod
    def validate_tip(tip):
        is_valid = True

        if len(tip['tip']) < 5:
            flash("Advice must be at least 5 characters.")
            is_valid = False

        return is_valid

    @classmethod
    def get_all_tips(cls, data):
        query = "SELECT * FROM tips"
        results = connectToMySQL(cls.DB).query.db(query)

        tips = []
        for item in results:
            tips.append(cls(item))
        return tips

    @classmethod
    def get_one_tip_by_id(cls, id):
        query = """
            SELECT * FROM 
                tips 
            WHERE id = %(id)s
        """
        one_tip = connectToMySQL(cls.DB).query_db(query, {"id":id})
        return cls(one_tip[0])

    @classmethod
    def get_one_random_tip(cls):
        query = """
            SELECT * FROM
                tips
            ORDER BY RAND() LIMIT 1
        """
        one_random_tip = connectToMySQL(cls.DB).query_db(query)
        return one_random_tip[0]

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO 
                tips 
                (tip, user_id) 
            VALUES
                (%(tip)s, %(user_id)s)
            """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def update(data):
        query = """
            UPDATE tips 
            SET %(tip)s
            WHERE id = %(user_id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results


    @classmethod
    def delete(cls, id):
        query  = """
            DELETE FROM 
            tips 
            WHERE id = %(id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query, {"id":id})
        return results


    # @classmethod
    # def get_one_tip_by_id(cls, data):
    #     query = """"
    #         SELECT * FROM 
    #             advice 
    #         LEFT JOIN users on advice.user_id = users.id
    #         WHERE advice.id = %(id)s
    #     """
    #     result = connectToMySQL(cls.DB).query_db(query, data)
    #     return cls(result[0])
