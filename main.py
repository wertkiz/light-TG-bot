from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = 'YOUR_TOKEN' # Замените 'YOUR_TOKEN' на токен вашего бота
TARGET_USER_ID = 'TARGET_USER_ID' # Замените 'TARGET_USER_ID' на ID пользователя, которому вы хотите пересылать сообщения

# Обработчик команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Этот бот будет пересылать сообщения другому пользователю в полном объёме.')

# Обработчик текстовых сообщений
def text_message(update: Update, context: CallbackContext) -> None:
    # Пересылаем текстовое сообщение
    context.bot.forward_message(chat_id=TARGET_USER_ID, from_chat_id=update.message.chat_id, message_id=update.message.message_id)

# Обработчик мультимедийных сообщений (фото, видео и т.д.)
def media_message(update: Update, context: CallbackContext) -> None:
    # Пересылаем мультимедийное сообщение вместе с подписью
    caption = update.message.caption if update.message.caption else ""
    context.bot.forward_message(chat_id=TARGET_USER_ID, from_chat_id=update.message.chat_id, message_id=update.message.message_id, caption=caption)

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, text_message))
    dispatcher.add_handler(MessageHandler(Filters.photo | Filters.video, media_message))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
