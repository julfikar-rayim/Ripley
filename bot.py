import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# -------- BANGLA AUTO REPLY FUNCTION -----------
def bangla_reply(text):
    text = text.lower()

    if "কেমন আছ" in text:
        return "আলহামদুলিল্লাহ ভালো আছি 😊 আপনি কেমন আছেন?"
    if "হাই" in text or "হ্যালো" in text:
        return "জী বলুন, কীভাবে সাহায্য করতে পারি?"
    if "ধন্যবাদ" in text:
        return "স্বাগতম ❤️"
    if "সালাম" in text:
        return "ওয়া আলাইকুমুস সালাম 🌸"
    if "কি কর" in text:
        return "আপনার মেসেজগুলোর উত্তর দিচ্ছি 😄"

    return "বুঝেছি! আর কিছু জানতে চান? 😊"


# ----------- MESSAGE HANDLER ----------------
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message is None:
        return

    user_text = update.message.text

    # শুধু বাংলা অক্ষর আছে কিনা
    if any("অ" <= c <= "হ" for c in user_text):
        reply = bangla_reply(user_text)
        await update.message.reply_text(reply)


# ----------------- MAIN ---------------------
async def main():
    import os
    BOT_TOKEN = os.getenv("BOT_TOKEN")

    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN missing in environment!")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

    print("Bot running...")

    await app.run_polling()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
