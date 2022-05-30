import asyncio

from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins

from YorForger import client as telethn
from YorForger.events import register as nobara

from telegram.utils.helpers import escape_markdown, mention_html, mention_markdown


@nobara(pattern="^/tagall ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    mentions = str(event.pattern_match.group(1)).strip()
    chat = await event.get_input_chat()
    async for x in telethn.iter_participants(chat, 100):
        mentions += f" \n @{x.username}"
    await event.reply(mentions)
    await event.delete()


@nobara(pattern="^/users ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    mentions = "Users : "
    chat = await event.get_input_chat()
    async for x in telethn.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f" \n @{x.username}"
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


__mod_name__ = "User Tagger"
__help__ = """
An "odds and ends" module for small, simple commands which don't really fit anywhere

× /id: Get the current group id. If used by replying to a message, gets that user's id.
× /info: Get information about a user.
× /wiki : Search wikipedia articles.
× /rmeme: Sends random meme scraped from reddit.
× /ud <query> : Search stuffs in urban dictionary.
× /wall <query> : Get random wallpapers directly from bot!
× /reverse : Reverse searches image or stickers on google.
× /paste: Saves replied content to `hastebin` and replies with a url.
× /gdpr: Deletes your information from the bot's database. Private chats only.
× /markdownhelp: Quick summary of how markdown works in telegram - can only be called in private chats.
"""
