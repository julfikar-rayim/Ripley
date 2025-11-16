import os
import openai
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
from telegram import Update

openai.api_key = os.getenv("OPENAI_API_KEY")
TOKEN = os.getenv("BOT_TOKEN")

def reply(update: Update, context: CallbackContext):
    user_msg = update.message.text

    prompt = f"ব্যবহারকারীর মেসেজ: {user_msg}\nবাংলায় একটি ছোট, সহজ, ভদ্র উত্তর দাও।"

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    bot_reply = response.choices[0].message["content"]
    update.message.reply_text(bot_reply)

updater = Updater(TOKEN)
updater.dispatcher.add_handler(MessageHandler(Filters.text, reply))

updater.start_polling()
updater.idle()
