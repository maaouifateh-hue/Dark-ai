import telebot
bot = telebot.TeleBot("8685849166:AAGbEOyrKi-vcb-GhPCTjXeq2p06Iu3OFE4")
@bot.message_handler(func=lambda m: True)
def all(m): bot.reply_to(m, f"صدى: {m.text}")
bot.infinity_polling()

