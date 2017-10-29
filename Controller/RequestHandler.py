from threading import Thread
from Model.Model import Model
from Model.Texts import Texts
from Model.TvPlans import TvPlans
from .Constants import Constants
from .TelegramInteracotor import TelegramInteractor


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
    def __init__(self, update, main_keyboard, cities_keyboard):
        # super(RequestHandler, self).__init__()
        self.get_const_data(update)
        self.init_user_text(update)

        # the main keyboard that will be shown to the user
        self.__main_keyboard = main_keyboard
        self.__cities_keyboard = cities_keyboard

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
            print("access to bot command")
            if self.__text == Constants.Commands.COMMAND_START:
                print("access to start command!")
                TelegramInteractor.send_message(self.__chat_id, Texts.START_TEXT, self.__main_keyboard)

            elif self.__text == Constants.Commands.COMMAND_SHOW_KEYBOARD:
                pass # TODO

        else:
            print("access to else")
            if self.__text == Constants.KeyboardButtons.KEYBOARD_BACK:
                self.__state = Constants.States.NORMAL
                TelegramInteractor.send_message(self.__chat_id, Texts.BACK_TEXT, self.__main_keyboard)

            elif self.__state == Constants.States.NORMAL:
                print("access to normal state")

                if self.__text == Constants.KeyboardButtons.KEYBOARD_TV_PLANS:
                    print("access to tvplan 1")
                    self.ans_tv_plan(1)

                elif self.__text == Constants.KeyboardButtons.KEYBOARD_TRANSLATE:
                    self.ans_english_word(1)

                elif self.__text == Constants.KeyboardButtons.KEYBOARD_WEATHER:
                    self.ans_weather(1, None)

                elif self.__text == Constants.KeyboardButtons.KEYBOARD_COIN_CURRENCY:
                    TelegramInteractor.send_message(self.__chat_id, Model.get_coin_currency(), None)

                elif self.__text == Constants.KeyboardButtons.KEYBOARD_HELP:
                    TelegramInteractor.send_message(self.__chat_id, Constants.ANSWER_BOT_HELP, None)

                else:
                    self.ans_ordinary_req()

            elif self.__state == Constants.States.TV_PLAN_CHANNEL_ENTERING:
                print("access to tvplan2")
                self.ans_tv_plan(2)

            elif self.__state == Constants.States.ENGLISH_WORD_ENTERING:
                print("access to english2")
                self.ans_english_word(2)

            elif self.__state == Constants.States.WEATHER_CITY_ENTERING:
                print("access to weather2!")
                self.ans_weather(2, self.__text)

            else:
                print("something wrong happened!")

        print("request answered to : ", self.__first_name)

    def ans_english_word(self, step: int):
        if step == 1:
            self.__state = Constants.States.ENGLISH_WORD_ENTERING
            message = Constants.TranslationMessages.INITIAL_MESSAGE
            TelegramInteractor.send_message(self.__chat_id, message, None)

        elif step == 2:
            print("AC1")
            if len(self.__text) > 20:
                print("AC2")
                message = Constants.TranslationMessages.ILLEGAL_CHARACTER_LEN
                TelegramInteractor.send_message(self.__chat_id, message, None)

            else:
                print("AC3")
                self.__state = Constants.States.NORMAL
                translate_json = Model.translate(self.__text)
                text = translate_json["text"]
                voice = translate_json["voice"]
                TelegramInteractor.send_message(self.__chat_id, text, self.__main_keyboard)

                print("voice = " , voice)
                if voice != -1:
                    caption = translate_json["word"] + "\n\n" + Constants.BotInfo.BOT_USERNAME
                    TelegramInteractor.send_voice(self.__chat_id, voice, self.__main_keyboard, caption)

    def ans_tv_plan(self, step: int):
        if step == 1:
            self.__state = Constants.States.TV_PLAN_CHANNEL_ENTERING
            message = "کانال موردنظر را انتخاب کنید."
            TelegramInteractor.send_message(self.__chat_id, message, TvPlans.get_channels_keyboard())
        elif step == 2:
            try:
                message = Model.get_tv_plans(self.__text)
                TelegramInteractor.send_message(self.__chat_id, message, None)
            except Exception as e:
                print("Error: in getting TvPlans data => RequestHandler line 90")
                message = "در دریافت اطلاعات شبکه خطایی رخ داد." + "\n" + "لطفا این موضوع را به سازنده بات اطلاع دهید."
                TelegramInteractor.send_message(self.__chat_id, message, None)

    def ans_weather(self, step: int, city):
        if step == 1:
            self.__state = Constants.States.WEATHER_CITY_ENTERING
            message = "شهر موردنظر خود را انتخاب کنید."
            TelegramInteractor.send_message(self.__chat_id, message, self.__cities_keyboard)
        elif step == 2:
            self.__state = Constants.States.NORMAL
            result = Model.get_weather(city)
            print(result)
            TelegramInteractor.send_message(self.__chat_id, result, self.__main_keyboard)

    def ans_ordinary_req(self):
        TelegramInteractor.send_message(self.__chat_id, "منظوری دریافت نشد!", None)
