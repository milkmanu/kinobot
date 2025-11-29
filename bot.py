import telebot

bot = telebot.TeleBot("8273644502:AAFTsY_fuvja6nIBXbC1vtZBfJ1HEK6V-s0")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        kod = int(message.text)
        bot.forward_message(message.chat.id, "@ksbsvslqvdlsnwkino", kod)
        bot.reply_to(message, "✅ Kino topildi!")
    except:
        bot.reply_to(message, "❌ Bu kodli kino topilmadi")
        
        
bot.polling()
