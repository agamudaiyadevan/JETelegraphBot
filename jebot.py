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
               text= f"""Hello {message.from_user.first_name},

▷ Just send me a photo or video under 5MB.
▷ Then I will download it.
▷ I will then upload it to the telegra.ph link.""",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "TENDKOTTA", url="https://telegram.me/tendkotta"),
                                        InlineKeyboardButton(
                                            "TharamaanaMovies", url="https://telegram.me/tharamaanamovies"),
                                  ],[
                                        InlineKeyboardButton(
                                            "YouTube DL", url="https://telegram.me/YouTubedownloadergroup1"),
                                        InlineKeyboardButton(
                                            "Channel List 📢", url="https://telegram.me/tharamaanateambot"),
                                        InlineKeyboardButton(
                                            "Bot List 🤖", url="https://telegram.me/tharamaanateambot"),
                                  ],[
                                        InlineKeyboardButton(
                                            "🤖 Click Here To Movie Request 🤖", url="http://t.me/movie_request_v3_robot")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jebot.on_message(filters.command("help"))
async def help(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>Telegraph Bot Help!

▷ Just send me a photo or video under 5MB.
▷ Then I will download it.
▷ I will then upload it to the telegra.ph link.</b>

<b>Maintained by :</b> <a href="https://telegram.me/tharamaanaadmin">∪∩∩᭄_1997</a>""",
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Help", callback_data="help"),
                                        InlineKeyboardButton(
                                            "About", callback_data="about"),
                                  ],[
                                        InlineKeyboardButton(
                                            "🤖 Click Here To Movie Request 🤖", url="http://t.me/movie_request_v3_robot")
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

<b>♞ Developer:</b> <a href="https://telegram.me/tharamaanaadmin">∪∩∩᭄_1997</a>

<b>♞ Tharamaana Team:</b> <a href="https://Telegram.me/tharamaanateambot">Click Here</a>

<b>♞ YouTube Downloader Group:</b> <a href="https://telegram.me/YouTubedownloadergroup1">Click Here</a>

<b>Maintained by :</b> <a href="https://telegram.me/tharamaanaadmin">∪∩∩᭄_1997</a>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back", callback_data="start")
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
        await msg.edit_text(f'**Get Your Link 👇\n\n🔅 https://telegra.ph{response[0]},\n\n<b>Please Subscribe</b> : [@TENDKOTTA](https://t.me/TENDKOTTA) 🇮🇳**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)

@Jebot.on_message(filters.video)
async def telegraphvid(client, message):
    msg = await message.reply_text("Uploading To Telegraph...)
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Video size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**Get Your Link 👇\n\n🔅 https://telegra.ph{response[0]},\n\n<b>Please Subscribe</b> : [@TENDKOTTA](https://t.me/TENDKOTTA) 🇮🇳**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)

@Jebot.on_message(filters.animation)
async def telegraphgif(client, message):
    msg = await message.reply_text(Uploading To Telegraph...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Gif size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**Get Your Link 👇\n\n🔅 https://telegra.ph{response[0]},\n\n<b>Please Subscribe</b> : [@TENDKOTTA](https://t.me/TENDKOTTA) 🇮🇳**',
            disable_web_page_preview=True,
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
<b>Create by :</b> <a href="https://telegram.me/tharamaanaadmin">∪∩∩᭄_1997</a>
"""
)

Jebot.run()
