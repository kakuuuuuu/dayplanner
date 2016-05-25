"""
    Sample Model File

    A Model should be in charge of communicating with the Database.
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import re

class Place(Model):
    def __init__(self):
        super(Place, self).__init__()

    def create_user(self, info):
        # We write our validations in model functions.
        # They will look similar to those we wrote in Flask
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        # Some basic validation
        if not info['name']:
            errors.append('First Name cannot be blank')

        elif len(info['name']) < 2:
            errors.append('First Name must be at least 2 characters long')

        if not info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Email format must be valid!')
        if not info['password']:
            errors.append('Password cannot be blank')
        elif len(info['password']) < 8:
            errors.append('Password must be at least 8 characters long')
        elif info['password'] != info['pw_confirmation']:
            errors.append('Password and confirmation must match!')
        # If we hit errors, return them, else return True.
        if errors:

            return {"status": False, "errors": errors}
        else:
            pw_hash = self.bcrypt.generate_password_hash(info['password'])

            query="INSERT INTO users(name, email, password) VALUES (:name, :email, :password)"
            data={'name':info['name'], 'email':info['email'],'password':pw_hash}

            self.db.query_db(query, data)

            get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            users = self.db.query_db(get_user_query)

            status = { "status": True, "user": users[0]}
            return status

    def login(self, info):

        errors = []

        query_login = "SELECT * FROM users WHERE email = :email LIMIT 1"
        data = { 'email': info['email'] }
        pw=info['password']
        print "password is", pw

        user = self.db.query_db(query_login, data)

        if user == []:
            print "no user"
            errors.append('InValid1 login!')
            return{"status": False, "errors": errors}
        else:
            if self.bcrypt.check_password_hash(user[0]['password'], info['password']):
                print "password matched"
                return {"status": True, "user": user[0] }
            else:
                print "password not matched"
                errors.append('Invalid login!')
                return{"status": False, "errors": errors}

    def insert_planning_data(self, info):
        query="INSERT INTO plans(city, start_time, end_time, start_location, users_id, transportation)VALUES(:city, :start_time, :end_time, :start_location,:users_id, :transportation)"
        data={
            'city':info['main_location'],
            'start_time':info['start_time'],
            'end_time':info['end_time'],
            'start_location':info['start_location'],
            'users_id':info['users_id'],
            'transportation':info['transportation']
        }
        print "This is", data
        return self.db.query_db(query, data)

    def insert_meal(self, info):
        query="INSERT INTO activities(type, duration, category, price, plan_id)VALUES(:type, :duration,  :category, :price, :plan_id)"
        data={
        'type':info['type'],
        'duration':info['duration'],
        'category':info['category'],
        'price':info['price'],
        'plan_id':info['plan_id']
        }
        return self.db.query_db(query, data)

    def insert_activity(self, info):
        query="INSERT INTO activities(type, duration, category, plan_id)VALUES(:type, :duration,  :category, :plan_id)"
        data={
        'type':info['type'],
        'duration':info['duration'],
        'category':info['category'],
        'plan_id':info['plan_id']
        }
        return self.db.query_db(query, data)

    def get_activities(self):
        query="SELECT * FROM activities"
        return self.db.query_db(query)

    def delete_activity(self, info):
        query="DELETE FROM activities WHERE id=:id"
        data={'id':info['id']}
        return self.db.query_db(query,data)
    def get_trips(self):
        query="SELECT * FROM plans"
        return self.db.query_db(query)
    












