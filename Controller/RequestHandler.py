from threading import Thread
from .Constants import Constants
from .TelegramInteracotor import TelegramInteractor
from Model.FileSearcher import FileSearcher

class RequestHandler:
    # user info
    __user_id = None
    __first_name = None
    __username = None

    # chat info
    __chat_id = None
    __is_private = None

    # message info
    __message_id = None
    __language = None
    __text = None
    __type = None

    __main_keyboard = None
    __cities_keyboard = None

    #
    __state = Constants.States.NORMAL

    def get_state(self):
        return self.__state

    """
    if the class instanced for the first time (not existed in the collection)
    it must be called just the __init__ method just by instancing the class!
    but if the class there exist in the collection then method get_user_text must be called;
    before calling run method !!!
    """
    def __init__(self, update, main_keyboard):
        # super(RequestHandler, self).__init__()
        self.get_const_data(update)
        self.init_user_text(update)

        # the main keyboard that will be shown to the user
        self.__main_keyboard = main_keyboard

    def get_const_data(self, update):
        # self.__message_id = update["message"]["message_id"] #
        self.__user_id = update["message"]["from"]["id"]
        self.__first_name = update["message"]["from"]["first_name"]
        self.__chat_id = update["message"]["chat"]["id"]
        self.__is_private = update["message"]["chat"]["type"]

        try:
            self.__username = update["message"]["from"]["username"]
        except Exception:
            self.__username = "--"

    def init_user_text(self, update):
        try:
            self.__text = update["message"]["text"]
        except:
            print("couldn't get the user text")

        try:
            self.__type = update["message"]["entities"][0]["type"]
        except:
            self.__type = Constants.MESSAGE_TYPE_ORDINARY

    """
    initializes the thread for answer_request method!!
    """
    def invoke(self):
        t = Thread(target=self.answer_request)
        t.start()

    """
    routine of answering happens in this function!
    """
    def answer_request(self):
        msg = "request got from : firstname :: %s  username :: %s \ntext : %s" % (self.__first_name, self.__username , self.__text)
        print(msg)

        if self.__type == Constants.MESSAGE_TYPE_BOT_COMMAND:
            if self.__text == Constants.Commands.COMMAND_START:
                TelegramInteractor.send_message(self.__chat_id, Constants.START_TEXT)

            elif self.__text == Constants.Commands.COMMAND_FETCH_FILE:
                self.__state = Constants.States.SENDING_FILE_NAME
                TelegramInteractor.send_message(self.__chat_id, Constants.SEND_FILE_NAME)

        else:
            FileSearcher.search_file(chat_id=self.__chat_id, file_name=self.__text)
