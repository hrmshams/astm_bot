import os.path
from Controller.TelegramInteracotor import TelegramInteractor

class FileSearcher:
    def __init__(self):
        pass

    @staticmethod
    def search_file(chat_id, file_name):
        file_address = "Files/" + file_name

        print(file_address)
        if os.path.exists(file_address):
            print('file_exists!')
            result = TelegramInteractor.send_file(chat_id, file_address)

            if result == -1:
                TelegramInteractor.send_message(chat_id, text="در ارسال فایل مشکلی پیش آمد")
            print(result)

        else:
            TelegramInteractor.send_message(chat_id, text="فایل موردنظر پیدا نشد!")

