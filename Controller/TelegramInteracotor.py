import requests,json
from .Constants import Constants

# be aware you should use this class methods as static!
# don't make any instances from this class!
class TelegramInteractor:

    # methods #
    send_message_meth = "sendMessage"
    send_voice_meth = "sendVoice"
    get_updates_meth = "getUpdates"

    # #
    token = Constants.BotInfo.BOT_TOKEN  # ranggo!
    telegram = "https://api.telegram.org/bot"

    def __init__(self):
        pass

    @staticmethod
    def send_message(chat_id, text, reply_markup):
        params = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "HTML",
        }
        if reply_markup is not None:
            str_key = json.dumps(reply_markup)
            params["reply_markup"] = str_key

        # print(reply_markup)
        result = TelegramInteractor.send_req_to_telegram_server(TelegramInteractor.send_message_meth, params)
        return result

    @staticmethod
    def send_voice(chat_id, voice, reply_markup, caption=""):
        params = {
            "chat_id": chat_id,
            "voice": voice,
        }
        if reply_markup is not None:
            str_key = json.dumps(reply_markup)
            params["reply_markup"] = str_key

        if caption != "":
            params["caption"] = caption

        result = TelegramInteractor.send_req_to_telegram_server(TelegramInteractor.send_voice_meth, params)
        return result

    @staticmethod
    def get_updates(offset):
        params = {
            "offset": offset
        }
        if offset is None:
            # print("access")
            params = None

        result = TelegramInteractor.send_req_to_telegram_server(TelegramInteractor.get_updates_meth, params)
        return result

    @staticmethod
    def send_req_to_telegram_server(req_method, params):
        url = TelegramInteractor.telegram + TelegramInteractor.token + "/" + req_method
        r = requests.post(url, params)

        return r
