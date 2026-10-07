import telebot
# التوكن الخاص بك مدمج مباشرة
TOKEN =
8988196691: AAFaD8890YsOHcnyz52W
OJC3XtgTKPnF3gI'
bot = telebot. TeleBot (TOKEN)
@bot. message_handler(commands=|'
start 'l)
def send_welcome message) :
bot.reply_to (message, " مرحباً
بك! البوت يعمل الآن بنجاح
@bot. message_handler(func=lambda
message: True)
def echo_all (message) :
bot. reply_to message,
:{message. text]" الا ا
if
_name_
'_main_':
("... البوت يعمل الآن ") print
bot. infinity_polling()
