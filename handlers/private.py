import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/d26d3885b9c592d167952.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━
🖤 ʜᴇʏ, ɪ ᴀᴍ sᴜᴘᴇʀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs...
ᴀʟʟ ᴏꜰ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✰ ᴋᴀᴋᴀ ᴡᴏʀʟᴅ ✰", url=f"https://t.me/marrkmusic")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo", "channel"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/d26d3885b9c592d167952.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ʀᴇᴘᴏ ᴀᴘᴘᴇᴀʟ ᴏɴ ᴛʜᴇsᴇ ɢʀᴏᴜᴘ ", url=f"https://t.me/marrkmusic")
                ]
            ]
        ),
    )
