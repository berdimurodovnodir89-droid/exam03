from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext
from .image_service import ImageService


class Handlers:
    def __init__(self, image_service: ImageService):
        self.image_service = image_service

    def start_command(self, update: Update, context: CallbackContext) -> None:
        keyboard = [
            [
                InlineKeyboardButton("🐶 Dog", callback_data="dog"),
                InlineKeyboardButton("🐱 Cat", callback_data="cat"),
                InlineKeyboardButton("🦊 Fox", callback_data="fox"),
            ]
        ]
        update.message.reply_text(
            "Qaysi hayvon rasmini ko'rmoqchisiz?",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    def button_handler(self, update: Update, context: CallbackContext) -> None:
        query = update.callback_query
        query.answer()

        animal = query.data
        chat_id = query.message.chat_id

        image_url = self.image_service.fetch_random_image(animal)
        context.bot.send_photo(chat_id=chat_id, photo=image_url)

    def dog_command(self, update: Update, context: CallbackContext) -> None:
        chat_id = update.effective_chat.id
        url = self.image_service.fetch_random_image("dog")
        context.bot.send_photo(chat_id=chat_id, photo=url)

    def cat_command(self, update: Update, context: CallbackContext) -> None:
        chat_id = update.effective_chat.id
        url = self.image_service.fetch_random_image("cat")
        context.bot.send_photo(chat_id=chat_id, photo=url)

    def fox_command(self, update: Update, context: CallbackContext) -> None:
        chat_id = update.effective_chat.id
        url = self.image_service.fetch_random_image("fox")
        context.bot.send_photo(chat_id=chat_id, photo=url)
