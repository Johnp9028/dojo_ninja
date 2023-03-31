from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja


class Dojo:
    def __init__(self , db_data ):
        self.id = db_data['id']
        self.location = db_data['location']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.ninjas = []


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"

        results = connectToMySQL('dojos_schema').query_db(query)
        dojos = []

        for d in results:
            dojos.append( cls(d) )
        return dojos

    @classmethod
    def save(cls, data):
        query= "INSERT INTO dojos (location) VALUES (%(location)s);"
        result = connectToMySQL('dojos_schema').query_db(query,data)
        return result

    @classmethod
    def delete(cls,data):
        query  = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL('dojos_schema').query_db(query,data)

    @classmethod
    def get_one(cls, data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_schema').query_db(query,data)
        print(results)
        dojo = cls(results[0])
        for row in results:
            n = {
                'id': row['ninjas.id'],
                'first': row['first'],
                'last': row['last'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            dojo.ninjas.append( Ninja(n) )
        return dojo