from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:

    def __init__(self, data):
        self.id = data['id']
        self.first = data['first']
        self.last=data['last']
        self.age=data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas"
        ninjas_from_db = connectToMySQL('dojos_schema').query_db(query)
        ninjas = []
        for n in ninjas_from_db:
            ninjas.append(cls(n))
        return ninjas


    @classmethod
    def save(cls,data):
        query = "Insert INTO ninjas (first,last,age,dojo_id,created_at,updated_at) VALUES(%(first)s,%(last)s,%(age)s,%(dojo_id)s,NOW(),NOW());"
        ninja_id = connectToMySQL('dojos_schema').query_db(query,data)
        return ninja_id



    @classmethod
    def get_all(cls):
            query = "SELECT * FROM ninjas;"
            ninjas_from_db =  connectToMySQL('dojos_schema').query_db(query)
            ninjas =[]
            for n in ninjas_from_db:
                ninjas.append(cls(n))
            return ninjas

    @classmethod
    def get_one(cls,data):
            query = "SELECT * FROM ninjas WHERE ninjas.id = %(id)s;"
            ninja_from_db = connectToMySQL('dojos_schema').query_db(query,data)

            return cls(ninja_from_db[0])

    @classmethod
    def update(cls,data):
            query = "UPDATE ninjas SET first=%(first)s, last=%(last)s, age=%(age)s, updated_at = NOW() WHERE id = %(id)s;"
            return connectToMySQL('dojos_schema').query_db(query,data)

    @classmethod
    def destroy(cls,data):
            query = "DELETE FROM ninjas WHERE id = %(id)s;"
            return connectToMySQL('dojos_schema').query_db(query,data)


