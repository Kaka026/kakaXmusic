import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"",
        caption="""**[☞](https://te.legra.ph/file/d26d3885b9c592d167952.jpg) 
✰ʜᴇʟʟᴏ...
ᴛʜɪs ᴍᴜsɪᴄ ʙᴏᴛ ɪs ᴛʜᴇ ɴᴇxᴛ ʟᴇᴠᴇʟ ᴏғ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴛʜᴀᴛ ʜᴀs ʙᴇsᴛ ʜɪɢʜ ǫᴜᴀʟɪᴛʏ ᴏғ ᴍᴜsɪᴄ ʙᴏᴛ ᴀɴᴅ ᴛʜᴇ ᴛʜɪs ᴍᴜsɪᴄ ʙᴏᴛ sᴍᴀsʜ ᴛʜᴇᴍ ᴏғ ᴀʟʟ sᴇʀᴠᴇʀ ᴏғ ᴍᴜsɪᴄ ʙᴏᴛ ᴀss...
➖➖➖➖➖➖➖➖➖➖➖➖➖
✰ ᴍᴀɴᴀɢᴇᴅ ʙʏ:-[•|ᴄʀᴀxʏ|🇮🇳|•](https://t.me/craxy_026)
➖➖➖➖➖➖➖➖➖➖➖➖➖**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✰ ᴍᴀʀʀᴋ ᴡᴏʀʟᴅ ✰", url=f"https://t.me/marrkmusic")
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
