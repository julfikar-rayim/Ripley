import os
import telebot
import re

BOT_TOKEN = os.environ.get("BOT_TOKEN")
ALLOWED_CHAT_IDS = [int(cid) for cid in os.environ.get("ALLOWED_CHAT_IDS", "").split(",")]

bot = telebot.TeleBot(BOT_TOKEN)

# ==========================
# BANGLA AUTO REPLY ENGINE
# ==========================

def get_reply(text):

    msg = text.lower()

    # Greeting
    if any(k in msg for k in ["hi", "hello", "salam", "assalamu", "আসসালামু", "সালাম"]):
        return "ওয়ালাইকুম সালাম! 😊 কিভাবে সাহায্য করতে পারি?"

    # How are you
    if any(k in msg for k in ["কেমন আছ", "how are you", "কি খবর"]):
        return "আলহামদুলিল্লাহ ভালো আছি ভাই, আপনি কেমন আছেন?"

    # Link related
    if "লিংক" in msg or "link" in msg:
        return "আপনার কোন লিংক সমস্যা হচ্ছে? বিস্তারিত বলুন।"

    # Help
    if any(k in msg for k in ["help", "সাহায্য", "হেল্প"]):
        return "জি ভাই সাহায্য লাগলে বলুন, আমি আছি 😊"

    # Group rules
    if any(k in msg for k in ["রুল", "rules"]):
        return "গ্রুপের মূল নিয়ম:\n1️⃣ সবাই ভদ্র ভাষায় কথা বলবেন\n2️⃣ স্প্যাম বা অপ্রয়োজনীয় লিংক শেয়ার করবেন না\n3️⃣ এডমিনের কথা সম্মান করবেন 😊"

    # Thanks
    if any(k in msg for k in ["ধন্যবাদ", "thank", "thanks"]):
        return "স্বাগতম ভাই 😊"

    # Bye
    if any(k in msg for k in ["bye", "বিদায়"]):
        return "আচ্ছা ভাই দেখা হবে ইনশাআল্লাহ 😊"

    # Default reply
    return "জি ভাই, বুঝেছি। একটু বিস্তারিত বলবেন?"


# ==========================
# MESSAGE HANDLER
# ==========================

@bot.message_handler(func=lambda m: True, content_types=['text'])
def auto_reply(message):

    if message.chat.id not in ALLOWED_CHAT_IDS:
        return  # অন্য গ্রুপে কাজ করবে না

    if message.from_user.is_bot:
        return  # বটের মেসেজে রিপ্লাই করবে না

    text = message.text
    reply = get_reply(text)

    bot.reply_to(message, reply)


print("🤖 Auto Reply Admin Bot Running...")
bot.infinity_polling()
