import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from image_bot import ImageBot


def main():
    load_dotenv()

    token = os.getenv("TOKEN")

    if not token:
        raise ValueError("BOT_TOKEN topilmadi .env faylda")

    bot = ImageBot(token=token)

    updater = Updater(bot.token)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", bot.handlers.start_command))
    dp.add_handler(CommandHandler("dog", bot.handlers.dog_command))
    dp.add_handler(CommandHandler("cat", bot.handlers.cat_command))
    dp.add_handler(CommandHandler("fox", bot.handlers.fox_command))
    dp.add_handler(CallbackQueryHandler(bot.handlers.button_handler))

    print("Bot ishga tushdi...")

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
