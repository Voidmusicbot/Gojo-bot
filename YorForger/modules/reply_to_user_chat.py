# This module is made by https://github.com/SOME-1HING/
# You are free to use this module. But don't delete this commented text. Thank you.


import html

from YorForger import dispatcher
from YorForger.modules.disable import DisableAbleMessageHandler
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, Filters

IMG_GM = "https://te.legra.ph/file/d84b6b1ff80a965a7bfa9.mp4"
IMG_GN = "https://te.legra.ph/file/daddc80126c8a5879f680.mp4"
IMG_HELLO = "https://te.legra.ph/file/b3aa85df1bbc16b71103a.mp4"
IMG_BYE = "https://te.legra.ph/file/35a2638006f4311aa282e.mp4"

def goodnight(update: Update, context: CallbackContext):

    update.effective_message.reply_photo(
            IMG_GN,
            parse_mode=ParseMode.MARKDOWN,
    )

def goodmorning(update, context):
    message = update.effective_message
    user1 = message.from_user.first_name
    try:
        update.effective_message.reply_photo(
            IMG_GM,f"*Good Morning:* {user1}",
            parse_mode=ParseMode.MARKDOWN,
        )
    except:
        reply = f"*Good Morning:* {user1}"
        message.reply_text(reply)

def hello(update: Update, context: CallbackContext):
    update.effective_message.reply_photo(
            IMG_HELLO,
            parse_mode=ParseMode.MARKDOWN,
    )

def bye(update: Update, context: CallbackContext):
    message = update.effective_message
    user1 = message.from_user.first_name
    try:
        update.effective_message.reply_animation(
            IMG_BYE,
            parse_mode=ParseMode.MARKDOWN,
        )
    except:
        reply = f"*Bye!!* {user1}"
        message.reply_text(reply)



GDMORNING_HANDLER = DisableAbleMessageHandler(
    Filters.regex(r"(?i)(good morning|gm|goodmorning)"), goodmorning, friendly="goodmorning", run_async = True
)
GDNIGHT_HANDLER = DisableAbleMessageHandler(
    Filters.regex(r"(?i)(surprised|stunned|amazed)"), goodnight, friendly="goodnight", run_async = True
)
BYE_HANDLER = DisableAbleMessageHandler(
    Filters.regex(r"(?i)(bye|brb|afk|goodbye)"), bye, friendly="bye", run_async = True
)
HELLO_HANDLER = DisableAbleMessageHandler(
    Filters.regex(r"(?i)(waiting|w8|w8ing|wait|shyness|shy|delay)"), hello, friendly="hello", run_async = True
)

dispatcher.add_handler(GDMORNING_HANDLER)
dispatcher.add_handler(GDNIGHT_HANDLER)
dispatcher.add_handler(HELLO_HANDLER)
dispatcher.add_handler(BYE_HANDLER)

__handlers__ = [
    GDMORNING_HANDLER,
    GDNIGHT_HANDLER,
    HELLO_HANDLER,
    BYE_HANDLER
]