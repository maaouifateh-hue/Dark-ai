from google import genai
import telebot

# It-Token tal-bot tat-Telegram tiegħek
TOKEN = '8988196691:AAFaD8890YsOHcnyz52W0JC3XtgTKPnF3gI'

# Il-Gemini API Key li tajtni integrata direttament
GEMINI_API_KEY = 'AQ.Ab8RN6JwKg_tGqLBCK6hbh6zWzoJ-fs7mb5e-bYUpC0VYUrzAw'

bot = telebot.TeleBot(TOKEN)
client = genai.Client(api_key=GEMINI_API_KEY)

# Il-personalità ta' Dark AI
SYSTEM_PROMPT = (
    "أنت ذكاء اصطناعي يسمى Dark AI. أسلوبك غامض، عميق، ذكي جداً، وتجيب بنبرة مظلمة"
    " ولكنها مفيدة وتقدم تحليلات دقيقة وعميقة للمستخدم."
)


@bot.message_handler(commands=['start'])
def send_welcome(message):
  bot.reply_to(
      message,
      "مرحباً بك في عالم الظلام. أنا **Dark AI**. كيف يمكنني مساعدتك اليوم؟",
  )


@bot.message_handler(func=lambda message: True)
def chat_with_gemini(message):
  try:
    # Ibgħat ir-risposta lil Gemini bil-personalità
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=message.text,
        config={
            'system_instruction': SYSTEM_PROMPT,
        },
    )
    bot.reply_to(message, response.text)
  except Exception as e:
    bot.reply_to(
        message, 'حدث خطأ ما في شبكة الظلام أو أن مفتاح الـ API غير صالح.'
    )
    print(f'Error: {e}')


if __name__ == '__main__':
  print('البوت يعمل الآن مع ذكاء Gemini...')
  bot.infinity_polling()
