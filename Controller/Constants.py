class Constants:
    MESSAGE_TYPE_BOT_COMMAND = "bot_command"
    MESSAGE_TYPE_ORDINARY = "not_bot_command"

    ANSWER_BOT_HELP = """
"""

    class Commands:
        COMMAND_START = "/start"
        COMMAND_SHOW_KEYBOARD = "/showkeyboard"

    class KeyboardButtons:
        KEYBOARD_TV_PLANS = "📺 برنامه های تلویزیون"
        KEYBOARD_COIN_CURRENCY = "💰 قیمت سکه و ارز"
        KEYBOARD_HELP = "⁉️ راهنمای بات"
        KEYBOARD_TRANSLATE = "مترجم " + "🇬🇧"
        KEYBOARD_WEATHER = "🌤 آب و هوا"

        KEYBOARD_BACK = "بازگشت ↩️"

    class States:
        NORMAL = 1
        ENGLISH_WORD_ENTERING = 2
        TV_PLAN_CHANNEL_ENTERING = 3
        WEATHER_CITY_ENTERING = 4

    class BotInfo:
        BOT_USERNAME = "@ranggobot"
        BOT_TOKEN = "393845550:AAEQkQ_c_w2xtjXUm8cBXZ7rg_VJ3qQilmk"

    class TranslationMessages:
        INITIAL_MESSAGE = "لغت موردنظر خود را وارد کنید." + "\n"
        ILLEGAL_CHARACTER_LEN = "طول متن واردشده بیشتر از ۲۰ کاراکتر است."+"\n"+"لطفا متن یا لغت دیگری وارد کنید"
