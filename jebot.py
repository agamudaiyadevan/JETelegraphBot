import os
import logging
from pyrogram import Client, filters
from telegraph import upload_file
from config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

Jebot = Client(
   "Telegraph Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@Jebot.on_message(filters.command("start"))
async def start(client, message):
   if message.chat.type == 'private':
       await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>Hello {message.from_user.first_name}!\n<b>I am Telegram to telegra.ph Image Uploader Bot</b>\n\n▷ Just give me a media under 5MB.\n▷ Then I will download it.\n▷ I will then upload it to the telegra.ph link.</b>""",   
                            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="TENDKOTTA", url=f"https://telegram.me/tendkotta"), InlineKeyboardButton(text="TharamaanaMovies", url=f"https://telegram.me/tharamaanamovies"), ],
                                           [InlineKeyboardButton(text="Youtube DL", url=f"https://telegram.me/YouTubedownloadergroup1"), InlineKeyboardButton(text="Channel List 📢", url=f"https://telegram.mr/tharamaanateambot"), InlineKeyboardButton(text="Bot Lists 🤖", url=f"https://telegram.me/tharamaanateambot"),],
                                           [InlineKeyboardButton(text="🤖 Movie Request Bot 🤖", url=f"https://telegram.me/Movie_Request_v3_Robot")]])
        ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jebot.on_message(filters.command("help"))
async def help(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>Telegraph Bot Help!

Just send a photo or video less than 5mb file size, I'll upload it to telegraph.

~ @Infinity_BOTs</b>""",
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back", callback_data="start"),
                                        InlineKeyboardButton(
                                            "About", callback_data="about"),
                                  ],[
                                        InlineKeyboardButton(
                                            "🤖 Movie Request Bot 🤖", url="https://telegram.me/tharamaanateambot")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jebot.on_message(filters.command("about"))
async def about(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>About Telegraph Bot!</b>

<b>♞ Developer:</b> <a href="https://telegram.me/tharamaanaadmin">Tharamaana Admin😎</a>

<b>♞ Tharamaana Team:</b> <a href="https://telegram.me/tharamaanateambot">Channel & Bot List</a>

<b>♞ TENDKOTTA ❤️:</b> <a href="https://telegram.me/tendkotta">Join Our Channel</a>

<b>~ @tharamaanamovies</b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back", callback_data="help"),
                                        InlineKeyboardButton(
                                            "🤖 Movie Request Bot 🤖", url="https://telegram.me/movie_request_v3_robot")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jebot.on_message(filters.photo)
async def telegraphphoto(client, message):
    msg = await message.reply_text("Uploading To Telegraph...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Photo size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**Uploaded To Telegraph!\n\n👉 https://telegra.ph{response[0]}\n\nJoin @tharamaanateambot**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)

@Jebot.on_message(filters.video)
async def telegraphvid(client, message):
    msg = await message.reply_text("Uploading To Telegraph...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Video size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**Uploaded To Telegraph!\n\n👉 https://telegra.ph{response[0]}\n\nJoin @tharamaanateambot**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)

@Jebot.on_message(filters.animation)
async def telegraphgif(client, message):
    msg = await message.reply_text("Uploading To Telegraph...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Gif size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**Uploaded To Telegraph!\n\n▷ https://telegra.ph{response[0]}\n\nCreate By @TharamaanaAdmin😎**',
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Open Link", url=f"https://telegra.ph{tlink[0]}"), InlineKeyboardButton(text="Share Link", url=f"https://telegram.me/share/url?url=https://telegra.ph{tlink[0]}"), ],
                                           [InlineKeyboardButton(text="🤖 Movie Request Bot 🤖", url="https://telegram.me/movie_request_v3_robot")]])
        )
    finally:
        os.remove(download_location)

@Jebot.on_callback_query()
async def button(bot, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(bot, update.message)
      elif "about" in cb_data:
        await update.message.delete()
        await about(bot, update.message)
      elif "start" in cb_data:
        await update.message.delete()
        await start(bot, update.message)

print(
    """
Bot Started!
Join @tharamaanateambot
"""
)

Jebot.run()
