from .TelegramInteracotor import TelegramInteractor
from Controller.RequestHandler import RequestHandler
import time
import json
from .Constants import Constants
from threading import Thread
from Model.Model import Model
from Model.Database import Database

class Controller:

    ##############################
    __database_info = {
        "db_name": "smart_bot_db",
        "tables": [
            {
                "table_name": "users",
                "table_struct": [
                    ["user_id", Database.INTEGER],
                    ["first_name", Database.VARCHAR+"(50)"],
                    ["user_name", Database.VARCHAR+"(50)"]
                ]
            }
        ]
    }
    ##############################

    __model = None
    __offset = 0

    """
    a collection :
    key => user_id
    value => request handler thread
    """
    __requests = {}

    def __init__(self):
        db_connection = {
            "username": "root",
            "password": "123",
        }
        self.__model = Model()

        """ configuring the database """
        self.__model.configure_database(self.__database_info, db_connection)

    """
    note :
     in a loop => checks the updates form telegram server
     then assign to all updates a thread
     and then starts the thread
    """
    def invoke(self):
        """initializing the keyboards"""
        '''
        main keyboard
        '''
        main_keyboard = [
            [{"text": Constants.KeyboardButtons.KEYBOARD_COIN_CURRENCY}, {"text": Constants.KeyboardButtons.KEYBOARD_TV_PLANS}],
            [{"text": Constants.KeyboardButtons.KEYBOARD_TRANSLATE}, {"text": Constants.KeyboardButtons.KEYBOARD_WEATHER}],
            [{"text": Constants.KeyboardButtons.KEYBOARD_HELP}]
        ]
        final_main_keyboard = {
            "keyboard": main_keyboard,
            "resize_keyboard": True,
            "one_time_keyboard": True
        }

        '''
        cities keyboard
        '''
        cities_keyboard = [
            [{"text": Constants.KeyboardButtons.KEYBOARD_BACK}],
            [{"text": "اصفهان"}, {"text": "مشهد"}, {"text": "تهران"}],
            [{"text": "شیراز"}, {"text": "تبریز"}, {"text": "کرج"}],
            [{"text": "کرمانشاه"}, {"text": "قم"}, {"text": "اهواز"}],
            [{"text": "زاهدان"}, {"text": "رشت"}, {"text": "ارومیه"}],
            [{"text": "همدان"}, {"text": "اراک"}, {"text": "کرمان"}],
            [{"text": "بندرعباس"}, {"text": "اردبیل"}, {"text": "یزد"}],
            [{"text": "سنندج"}, {"text": "قزوین"}, {"text": "زنجان"}],
            [{"text": "ساری"}, {"text": "گرگان"}, {"text": "خرم آباد"}],
            [{"text": "بیرجند"}, {"text": "بوشهر"}, {"text": "بجنورد"}],
            [{"text": "سمنان"}, {"text": "شهرکرد"}, {"text": "ایلام"}],
            [{"text": "یاسوج"}]
        ]
        final_cities_keyboard = {
            "keyboard": cities_keyboard,
            "resize_keyboard": True,
            "one_time_keyboard": True
        }

        while True:
            # sending the request to telegram for getting the updates!
            respond = TelegramInteractor.get_updates(self.__offset)

            # checking if request has done properly!
            if respond.status_code == 200:
                updates_text = respond.text
            else:
                print("ERROR:\nCouldn't send the request! status code ::", respond.status_code)
                return

            # converting updates string into json !
            updates = json.loads(updates_text)["result"]

            # implementing the req_handler for all updates!
            for u in updates:
                # checking if request exists in the collection!

                '''
                there is two ways :
                1) the thread related to user request handler exists in the collection so we handle the request!
                2) the thread doesn't exist in the collection so we must add the user_id and related thread to ..
                   .. collection and then implementing some actions like checking if this user exists in the collection
                   .. and somthing else!
                '''
                user_id = u["message"]["from"]["id"]
                if Controller.is_key_exist(self.__requests, user_id):
                    # getting the user text and starting the thread
                    req_handler = self.__requests[user_id]
                    req_handler.init_user_text(u)

                    req_handler.invoke()

                else:
                    # adding the request to the collection!
                    t = Thread(target=self.__model.add_user_in_database(user_id, u))
                    t.start()

                    req_handler = RequestHandler(u, final_main_keyboard, final_cities_keyboard)
                    self.__requests[user_id] = req_handler
                    req_handler.invoke()

                # checking the offset!
                update_id = u["update_id"]
                if self.__offset < update_id: # Do we need this ?
                    self.__offset = update_id

            if len(updates) != 0:
                self.__offset += 1

            time.sleep(0.5)
        # END OF WHILE #

    @staticmethod
    def is_key_exist(collection, key):
        if key in collection:
            return True
        else:
            return False

