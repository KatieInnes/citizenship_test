from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self , data):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.advice = [] 
    
    @staticmethod
    def validate_user_registration(user):
        is_valid = True

        if User.search_by_email({ "email": user['email'] }):
            flash("Email already in use.")
            is_valid = False

        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email format")
            is_valid = False

        if len(user['password']) <8:
            flash("Password must be at least 8 characters")
            is_valid = False

        if user['password'] != user['password_confirm']:
            flash("Passwords must match")
            is_valid = False

        if len(user['email']) < 1:
            flash("Email is required.")
            is_valid = False

        if len(user['username']) < 4:
            flash("Username must be at least 4 characters.")
            is_valid = False

        return is_valid

    @classmethod
    def save(cls, data ):
        query = """
        INSERT INTO 
            users 
            (username, email, password) 
        VALUES
            (%(username)s, %(email)s, %(password)s)
        """
        return connectToMySQL("citizenship_test").query_db( query, data ) 

    @classmethod
    def search_by_id(cls, data):
        query = """
        SELECT * FROM 
            users 
        WHERE 
            id = %(id)s;
        """
        result = connectToMySQL("citizenship_test").query_db(query, data)
        if result == False:
            return False
        return cls(result[0])

    @classmethod
    def search_by_email(cls, data):
        query = """
        SELECT * FROM 
            users 
        WHERE email = %(email)s
        """
        result = connectToMySQL("citizenship_test").query_db(query, data)
        if not result:
            return False
        return cls(result[0])
