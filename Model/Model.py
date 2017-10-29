from .Translator import Translator
from Controller.Constants import Constants
from Model.FileImplementer import FileImplementer
import json
from Model.Database import Database

"""
we have a table in database named "users" :
[
    "user_id" : int
    "first_name" : string
    "user_name" : string
]

"""
class Model:

    __database = None
    __users_table_name = "users"

    def __init__(self):
        pass

    '''
    first of all this method checks if the user_id exists in database
    if exists so it does nothing! and if not it adds the user information into database !
    '''
    def add_user_in_database(self, user_id: int, update_obj):
        self.__database.connect_db()

        cond = "user_id=\"%d\"" % user_id
        result = self.__database.get_rows(self.__users_table_name, cond)

        if len(result) == 0:

            try:
                __first_name = update_obj["message"]["from"]["first_name"]
            except:
                __first_name = "--"

            try:
                __username = update_obj["message"]["from"]["username"]
            except Exception:
                __username = "--"

            model = [
                ["user_id", user_id, False],
                ["first_name", __first_name, True],
                ["user_name", __username, True]
            ]

            self.__database.insert(self.__users_table_name, model)

        self.__database.close_db()

    '''
    '''
    def configure_database(self, database_info, db_connection):

        db = Database()
        username = db_connection["username"]
        password = db_connection["password"]
        dbname = database_info["db_name"]
        db.connect_db(username=username, password=password)

        # creating the database if not exist!
        query = "CREATE DATABASE IF NOT EXISTS " + dbname
        db.exec_query(query)
        db.close_db()

        # initializing the connection data into Database class!
        self.__database = Database(username=username, password=password, dbname=dbname)

        # creating the tables if not exists!
        self.__database.connect_db()
        for t in database_info["tables"]:

            # checking if table exists or not!
            cond = "table_schema='%s' and table_name='%s'" % (dbname, t["table_name"])
            result = self.__database.get_rows("information_schema.tables", cond)

            if len(result) == 0:
                self.__database.create_table(t["table_name"], t["table_struct"])

        self.__database.close_db()
