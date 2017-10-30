class Constants:
    MESSAGE_TYPE_BOT_COMMAND = "bot_command"
    MESSAGE_TYPE_ORDINARY = "not_bot_command"

    ANSWER_BOT_HELP = """
"""

    START_TEXT = """
    دوست عزیز به بات astm standard خوش آمدید!
    با استفاده ازین بات می توانید فایل های pdf موردنظر خود را از سرور دریافت کنید.
    """

    SEND_FILE_NAME = """
    لطفا اسم فایل موردنظر خود را با پسوند وارد نمایید.
    """

    class Commands:
        COMMAND_START = "/start"
        COMMAND_FETCH_FILE = "/getFile"

    class KeyboardButtons:
        pass

    class States:
        NORMAL = 1
        SENDING_FILE_NAME = 2

    class BotInfo:
        BOT_USERNAME = "@StandardSharingBot"
        BOT_TOKEN = "323477520:AAHkQzYMr5PhytMJF4VUFgGtotAj4ndrYpQ"
