import telebot
from telebot import types
import datetime

# @BotFather'dan olgan tokenni bu yerga qo'ying
API_TOKEN = '8782950949:AAH9vh305D1NtB6xCXZ6_C4Jk7IlL64TmY0'
bot = telebot.TeleBot(API_TOKEN)

user_data = {}

# QO'NG'IROQLAR JADVALI
BELL_SCHEDULE = {
    "1": "08:00 - 08:45", "2": "08:50 - 09:35", "3": "09:40 - 10:25",
    "4": "10:45 - 11:30", "5": "11:35 - 12:20", "6": "12:25 - 13:10"
}

# BARCHA SINFLAR JADVALI (6A dan 11B gacha)
SCHEDULE = {
    "6A": {
        "Dushanba": ["Kelajak soati", "Ona tili", "Rus tili", "Matematika", "Ingliz tili"],
        "Seshanba": ["Matematika", "Informatika", "Tabiiy fan", "Ingliz tili", "Texnologiya", "Texnologiya"],
        "Chorshanba": ["Ona tili", "Matematika", "Tarix", "Ingliz tili"],
        "Payshanba": ["Ona tili", "Adabiyot", "Jismoniy t.", "Musiqa", "Tarbiya", "Texnologiya"],
        "Juma": ["Tasviriy s.", "Adabiyot", "Tabiiy fan", "Matematika", "Tarix", "Jismoniy t."],
        "Shanba": ["Rus tili", "Matematika", "Tabiiy fan", "Ingliz tili", "Ona tili"]
    },
    "6B": {
        "Dushanba": ["Kelajak soati", "Rus tili", "Matematika", "Jismoniy t.", "Ona tili", "Ingliz tili"],
        "Seshanba": ["Musiqa", "Tarbiya", "Tabiiy fan", "Matematika", "Informatika"],
        "Chorshanba": ["Tarix", "Rus tili", "Jismoniy t.", "Ona tili", "Ingliz tili", "Matematika"],
        "Payshanba": ["Adabiyot", "Ona tili", "Texnologiya", "Texnologiya", "Ingliz tili"],
        "Juma": ["Tarix", "Tabiiy fan", "Matematika", "Tasviriy s.", "Adabiyot", "Jismoniy t."],
        "Shanba": ["Ingliz tili", "Ona tili", "Rus tili"]
    },
    "7A": {
        "Dushanba": ["Kelajak soati", "Matematika", "Ona tili", "Geografiya", "Ingliz tili", "Biologiya"],
        "Seshanba": ["Kimyo", "Musiqa", "O'zb. tarixi", "Biologiya", "Ingliz tili", "Musiqa"],
        "Chorshanba": ["Jahon tarixi", "Matematika", "Texnologiya", "Texnologiya", "Informatika", "Matematika"],
        "Payshanba": ["Rus tili", "Jismoniy t.", "Fizika", "Ingliz tili", "Kimyo", "Ona tili"],
        "Juma": ["Adabiyot", "Tasviriy s.", "Jismoniy t.", "Geografiya", "Rus tili", "Matematika"],
        "Shanba": ["O'zb. tarixi", "Fizika", "Kimyo", "Matematika", "Ingliz tili", "Adabiyot"]
    },
    "7B": {
        "Dushanba": ["Kelajak soati", "Rus tili", "Ona tili", "Matematika", "Geografiya"],
        "Seshanba": ["O'zb. tarixi", "Musiqa", "Texnologiya", "Texnologiya", "Ingliz tili", "Matematika"],
        "Chorshanba": ["Ingliz tili", "Matematika", "Jahon tarixi", "Ona tili", "Tarbiya", "Jismoniy t."],
        "Payshanba": ["Jismoniy t.", "Biologiya", "Fizika", "Kimyo", "Ona tili"],
        "Juma": ["Informatika", "Adabiyot", "Tasviriy s.", "Geografiya", "Jismoniy t.", "Rus tili"],
        "Shanba": ["Fizika", "O'zb. tarixi", "Adabiyot", "Kimyo", "Ona tili", "Matematika"]
    },
    "8A": {
        "Dushanba": ["Kelajak soati", "Fizika", "Algebra", "Ona tili", "Geografiya", "Jismoniy t."],
        "Seshanba": ["Chizmachilik", "O'zb. tarixi", "Algebra", "Kimyo", "Biologiya", "Geografiya"],
        "Chorshanba": ["Algebra", "Jahon tarixi", "Algebra", "Ona tili", "Texnologiya", "Informatika"],
        "Payshanba": ["Tarbiya", "Fizika", "Rus tili", "Ingliz tili", "Ona tili", "Biologiya"],
        "Juma": ["Rus tili", "Jismoniy t.", "Geometriya", "Adabiyot", "O'zb. tarixi"],
        "Shanba": ["Huquq", "Adabiyot", "Geometriya", "Ona tili", "Kimyo"]
    },
    "8B": {
        "Dushanba": ["Kelajak soati", "Geografiya", "Fizika", "Ona tili", "Ingliz tili", "Algebra"],
        "Seshanba": ["Texnologiya", "Chizmachilik", "Kimyo", "O'zb. tarixi", "Biologiya", "Jismoniy t."],
        "Chorshanba": ["Algebra", "Ona tili", "Jahon tarixi", "Texnologiya", "Informatika", "O'zb. tarixi"],
        "Payshanba": ["Biologiya", "Tarbiya", "Ingliz tili", "Rus tili", "Fizika"],
        "Juma": ["Ona tili", "Rus tili", "Kimyo", "Jismoniy t.", "Geografiya", "Algebra"],
        "Shanba": ["Informatika", "Huquq", "Biologiya", "Geometriya", "Adabiyot", "Adabiyot"]
    },
    "9A": {
        "Dushanba": ["Kelajak soati", "Algebra", "Fizika", "Infor/Rus", "Ingliz tili", "Ona tili"],
        "Seshanba": ["Fizika", "Biologiya", "Chizmachilik", "Jismoniy t.", "Tarbiya"],
        "Chorshanba": ["Infor/Rus", "Algebra", "Rus/Infor", "Geometriya", "Jismoniy t.", "Ona tili"],
        "Payshanba": ["Chizmachilik", "Kimyo", "O'zb. tarixi", "Geografiya", "Ingliz tili", "Adabiyot"],
        "Juma": ["Algebra", "Jahon tarixi", "Geometriya", "Ona tili", "Geografiya", "Fizika"],
        "Shanba": ["Biologiya", "Kimyo", "O'zb. tarixi", "Ingliz tili", "Huquq", "Adabiyot"]
    },
    "9B": {
        "Dushanba": ["Kelajak soati", "Ona tili", "Rus/Infor", "Algebra", "Fizika", "Texnologiya"],
        "Seshanba": ["Biologiya", "Fizika", "Chizmachilik", "Ingliz tili", "Jismoniy t.", "Tarbiya"],
        "Chorshanba": ["Rus/Infor", "Infor/Rus", "Geometriya", "Jismoniy t.", "Ona tili"],
        "Payshanba": ["Kimyo", "Ingliz tili", "Geografiya", "Jismoniy t.", "Adabiyot", "O'zb. tarixi"],
        "Juma": ["Jahon tarixi", "Algebra", "Ona tili", "Geometriya", "Fizika", "Geografiya"],
        "Shanba": ["Biologiya", "Kimyo", "O'zb. tarixi", "Ingliz tili", "Huquq", "Adabiyot"]
    },
    "10A": {
        "Dushanba": ["Kelajak soati", "Ona tili", "Rus/Infor", "Algebra", "Fizika", "Texnologiya"],
        "Seshanba": ["Informatika", "Jismoniy t.", "O'zb. tarixi", "Geografiya", "CHQBT", "Biologiya"],
        "Chorshanba": ["Algebra", "Ingliz tili", "Huquq", "Ona tili", "CHQBT", "Jismoniy t."],
        "Payshanba": ["Informatika", "Geografiya", "Kimyo", "Jismoniy t.", "Biologiya", "O'zb. tarixi"],
        "Juma": ["Fizika", "Algebra", "Rus tili", "Geometriya", "Adabiyot"],
        "Shanba": ["Tarbiya", "Algebra", "Rus tili", "Adabiyot", "Geometriya"]
    },
    "10B": {
        "Dushanba": ["Kelajak soati", "Ingliz tili", "Ona tili", "Fizika", "Biologiya", "CHQBT"],
        "Seshanba": ["Geografiya", "Kimyo", "Jismoniy t.", "O'zbek tarixi"],
        "Chorshanba": ["CHQBT", "Algebra", "Ingliz tili", "Huquq", "Ona tili"],
        "Payshanba": ["Geografiya", "Biologiya", "Jahon tarixi", "Kimyo", "Adabiyot", "Jismoniy t."],
        "Juma": ["Algebra", "Rus/Infor", "Fizika", "Infor/Rus", "Geometriya", "Adabiyot"],
        "Shanba": ["Algebra", "Geometriya", "Ona tili", "Rus/Infor", "Tarbiya"]
    },
    "11A": {
        "Dushanba": ["Kelajak soati", "Kimyo", "Algebra", "Fizika", "Jismoniy t.", "CHQBT"],
        "Seshanba": ["Tadbir. asoslari", "Ingliz tili", "CHQBT", "Algebra", "O'zb. tarixi", "Fizika"],
        "Chorshanba": ["Algebra", "CHQBT", "Ona tili", "Tarbiya", "Huquq"],
        "Payshanba": ["Ingliz tili", "Jahon tarixi", "Ona tili", "Adabiyot", "Jismoniy t."],
        "Juma": ["Rus t/Infor", "Kimyo", "Infor/Rus", "Adabiyot", "Geometriya"],
        "Shanba": ["Infor/Rus", "Geometriya", "Rus t/Infor", "Fizika", "Adabiyot"]
    },
    "11B": {
        "Dushanba": ["Kelajak soati", "Jismoniy t.", "Kimyo", "Biologiya", "Algebra", "Informatika"],
        "Seshanba": ["O'zb. tarixi", "CHQBT", "Ingliz tili", "Fizika", "Algebra"],
        "Chorshanba": ["Tadbir. asoslari", "Adabiyot", "Ona tili", "Jismoniy t.", "Huquq"],
        "Payshanba": ["Jahon tarixi", "Ingliz tili", "Adabiyot", "Ona tili", "CHQBT", "Astronomiya"],
        "Juma": ["Kimyo", "Geometriya", "Tarbiya", "Rus tili", "Informatika"],
        "Shanba": ["Geometriya", "Rus tili", "Fizika", "Biologiya"]
    }
}

# --- KEYBOARDS ---
def class_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    buttons = [types.KeyboardButton(cls) for cls in SCHEDULE.keys()]
    markup.add(*buttons)
    return markup

def day_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    days = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba"]
    markup.add(*[types.KeyboardButton(d) for d in days])
    markup.add(types.KeyboardButton("Bugun"), types.KeyboardButton("⬅️ Ortga"))
    # Menyu ichiga Start tugmasini qo'shish
    markup.add(types.KeyboardButton("/start"))
    return markup

# --- HANDLERS ---
@bot.message_handler(commands=['start'])
def start_cmd(message):
    bot.send_message(message.chat.id, "🏫 **7-maktab dars jadvali botiga xush kelibsiz!**\n\nSinfingizni tanlang:", 
                     reply_markup=class_keyboard(), parse_mode="Markdown")

@bot.message_handler(func=lambda m: m.text in SCHEDULE.keys())
def process_class(message):
    user_data[message.chat.id] = message.text
    bot.send_message(message.chat.id, f"✅ *{message.text}* sinfi tanlandi.\nKunning tanlang:", 
                     reply_markup=day_keyboard(), parse_mode="Markdown")

@bot.message_handler(func=lambda m: m.text in ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Bugun", "⬅️ Ortga", "/start"])
def process_day(message):
    chat_id = message.chat.id
    
    if message.text == "/start":
        return start_cmd(message)

    if chat_id not in user_data:
        bot.send_message(chat_id, "Avval sinfni tanlang.", reply_markup=class_keyboard())
        return

    if message.text == "⬅️ Ortga":
        bot.send_message(chat_id, "Sinfni qayta tanlang:", reply_markup=class_keyboard())
        return

    user_class = user_data[chat_id]
    target_day = message.text
    
    if target_day == "Bugun":
        days_uz = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba"]
        target_day = days_uz[datetime.datetime.now().weekday()]

    if target_day == "Yakshanba":
        bot.send_message(chat_id, "😴 Bugun yakshanba, dam olish kuni!")
        return

    lessons = SCHEDULE[user_class].get(target_day, [])
    
    if not lessons:
        bot.send_message(chat_id, "Bu kun uchun jadval topilmadi.")
    else:
        text = f"📅 *{target_day} | {user_class} sinfi*\n\n"
        text += "📝 *Darslar va vaqti:*\n"
        for i, lesson in enumerate(lessons, 1):
            time_range = BELL_SCHEDULE.get(str(i), "--:--")
            text += f"{i}. {time_range} — *{lesson}*\n"
        
        bot.send_message(chat_id, text, parse_mode="Markdown")

import os
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot ishlayapti!"

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))

def keep_alive():
    t = Thread(target=run)
    t.start()

# Botni ishga tushirishdan oldin bu funksiyani chaqiramiz
if __name__ == '__main__':
    print("Bot ishga tushdi...")
      keep_alive()
    # skip_pending=True eski (to'planib qolgan) xabarlarni o'chirib yuboradi
    bot.infinity_polling(skip_pending=True)
    
