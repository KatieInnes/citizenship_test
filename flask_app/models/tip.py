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
            flash("Tip must be at least 5 characters.")
            is_valid = False

        return is_valid

    @classmethod
    def get_all_tips(cls):
        query = """
            SELECT * FROM 
                tips 
            JOIN users on tips.user_id = users.id
        """
        results = connectToMySQL(cls.DB).query_db(query)
        tips = []
        for tip in results:
            this_tip = cls(tip)
            user_data = {
                    "id": tip['users.id'],
                    "username": tip['username'],
                    "email": tip['email'],
                    "password": "",
                    "created_at": tip['users.created_at'],
                    "updated_at": tip['users.updated_at']
            }
            this_tip.test_taker = user.User(user_data)
            tips.append(this_tip)
        return tips

    @classmethod
    def save_new_tip(cls, data):
        query = """
            INSERT INTO 
                tips 
                (tip, user_id) 
            VALUES
                (%(tip)s, %(user_id)s)
            """
        return connectToMySQL(cls.DB).query_db(query, data)


    @classmethod
    def get_one_tip_by_id(cls, data):
        query = """
            SELECT * FROM 
                tips 
            JOIN users on tips.user_id = users.id
            WHERE tips.id = %(id)s
        """
        result = connectToMySQL(cls.DB).query_db(query, data)

        tip = result[0]
        this_tip = cls(tip)
        user_data = {
                    "id": tip['users.id'],
                    "username": tip['username'],
                    "email": tip['email'],
                    "password": "",
                    "created_at": tip['users.created_at'],
                    "updated_at": tip['users.updated_at']
            }
        this_tip.test_taker = user.User(user_data)
        return this_tip

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
    def update_tip(cls, data):
        query = """
        UPDATE
            tips SET
            tip=%(tip)s
        WHERE id = %(id)s
        """
        return connectToMySQL(cls.DB).query_db(query, data)


    @classmethod
    def delete_tip(cls, data):

        query  = """
            DELETE FROM 
            tips 
            WHERE id = %(id)s
        """
        return connectToMySQL(cls.DB).query_db(query, data)
        


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


    # @classmethod
    # def get_all_tips(cls, data):
    #     query = "SELECT * FROM tips"
    #     results = connectToMySQL(cls.DB).query.db(query)

    #     tips = []
    #     for tip in results:
    #         tips.append(cls(tip))
    #     return tips

    # @classmethod
    # def get_one_tip_by_id(cls, id):
    #     query = """
    #         SELECT * FROM 
    #             tips 
    #         WHERE id = %(id)s
    #     """
    #     one_tip = connectToMySQL(cls.DB).query_db(query, {"id":id})
    #     return cls(one_tip[0])
