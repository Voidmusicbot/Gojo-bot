from YorForger import dispatcher
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode
from telegram.utils.helpers import escape_markdown

from telegram.ext import (
    CallbackContext,
    CommandHandler,
)

PHOTO = "https://te.legra.ph/file/d278826d0f59ed9c00341.mp4"


def alive(update: Update, context: CallbackContext):
    TEXT = "[](https://te.legra.ph/file/d278826d0f59ed9c00341.mp4)Hi **{}**, I Am **Yor Forger**!\n\n◈I'm working properly! \n\n◈My Darling - **[AUGSTUN 🝪 𝕮UᏒᏕɆĐ](https://t.me/Aug0felix)**\n\n◈Thanks For Using Me Here◈"

    first_name = update.effective_user.first_name

    update.effective_message.reply_text(
        TEXT.format(escape_markdown(first_name)), 
        parse_mode=ParseMode.MARKDOWN,
    )

void_handler = CommandHandler("alive", alive, run_async = True)
dispatcher.add_handler(void_handler)


__help__ = """ 
❂ /alive: To check if bot is alive or not."""
   
__mod_name__ = "Alive"