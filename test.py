from Controller.Controller import Controller
from Model.TvPlans import TvPlans
from Model.StringImplementer import StringImplementer
from Model.CoinCurrencyPrice import CoinCurrencyPrice
from Model.Model import Model
from Model.FileImplementer import FileImplementer
from Model.DataGetter import DataGetter
from Model.Translator import Translator
from Model.Weather import Weather
import time

from Model.Database import Database

# t = Controller()
# t.invoke()

# print(Texts.START_TEXT)

# tvpl = TvPlans()
# tvpl.get_tv_plans(TvPlans.CHANNEL_POOYA)

# mainStr = "hamid={}"
# firstStr = "="
# endStr = "="
# cuttenStr = StringImplementer.string_cutter(mainStr, firstStr, endStr)
# print(cuttenStr)

# print(CoinCurrencyPrice.get_coin_currency_price())
# str = "123"
# print (str[0:len(str)])

# CoinCurrencyPrice.third_tokenize("1123123123123123")
# Translator.translate("hello")

# print(Controller.is_key_exist({"hey":"you", "hi":"me"}, "1hey"))

# FileImplementer.rewrite_file("Model/Data/TvPlansData", "hey")
# DataGetter.invoke()

# print( TvPlans.get_tv_plans(34) )

# for i in range(0, 30):
#     print("<==", i, "==>")
#     Weather.get_weather(None)
#     time.sleep(10)

# print(Weather.get_desired_weather("ardabil")[1])

# DataGetter.invoke()

# r = Database.create_table("table1", model)
# print(r)

# print(Translator.longman_translate("start"))

# table_model = [
#     ["firstname", Database.VARCHAR + "(50)"],
#     ["lastname", Database.VARCHAR + "(50)"]
# ]
#
# values_model = [
#     ["firstname", "\"reza\""],
#     ["lastname", "\"123\""]
# ]
#
# /db = Database(dbname="smart_bot", username="root", password="123")
# db.connect_db()

# try:
#     db.create_table("first_table", table_model)
# except:
#     print("exception creating table!")


# db.insert("first_table", values_model)
# r = db.get_rows("first_table", None)
# print(r[0][1])
# db.close_db()
