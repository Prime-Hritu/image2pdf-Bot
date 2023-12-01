# code dev by t.me/Prime_Hritu
# © Hritu
# Use The Code With Credits To t.me/Prime_Hritu otherwise Strict Action will be taken
import os
from PIL import Image
from pyrogram import Client,filters 
from pyrogram.types import (InlineKeyboardButton,  InlineKeyboardMarkup)
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from pyrogram.errors import UserBannedInChannel, UserNotParticipant
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant

TOKEN = os.environ.get("TOKEN", "")

API_ID = int(os.environ.get("API_ID", ))

API_HASH = os.environ.get("API_HASH", "")

CH_ID = os.environ.get("CH_ID", "")

CH_NM = os.environ.get("CH_NM", "")

OWNER = os.environ.get("OWNER", "")

app = Client(
        "pdf",
        bot_token=TOKEN,api_hash=API_HASH,
            api_id=API_ID
    )


LIST = {}

@app.on_message(filters.text & filters.private & filters.incoming)
async def fore(c, m):
      try:
        chat = await c.get_chat_member(CH_ID, m.from_user.id)
        if chat.status=="kicked":
           await c.send_message(chat_id=m.chat.id, text="You are Banned ☹️\n\n📝 If u think this is an ERROR message in @PrivateHelpXBot", reply_to_message_id=m.id)
           m.stop_propagation()
      except UserBannedInChannel:
         return await c.send_message(chat_id=m.chat.id, text="Hai you made a mistake so you are banned from channel so you are banned from me too 😜")
      except UserNotParticipant:
          button = [[InlineKeyboardButton('🇮🇳 Updates Channel', url=f'https://t.me/{CH_NM}')]]
          markup = InlineKeyboardMarkup(button)
          return await c.send_message(chat_id=m.chat.id, text="""Hai bro,\n\nYou must join my channel for using me.\n\nPress this button to join now\n\nReport Error at @PrivateHelpXBot 👇""", reply_markup=markup)
      m.continue_propagation()

@app.on_message(filters.command(['start']))
async def start(client, message):
 await message.reply_text(text =f"""Hello {message.from_user.first_name } , I Am image to pdf bot 

i can convert image to pdf

**Send Me Images And At End Send /convert**

This bot created by @Prime_Hritu""",reply_to_message_id = message.id ,  reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Updates Channel 🇮🇳" ,url=f"https://t.me/{CH_NM}") ],
[
                    InlineKeyboardButton("Developer 💀" ,url="https://t.me/Prime_Hritu") ]
                 ]        ) )




@app.on_message(filters.private & filters.photo)
async def pdf(client,message):
 
 if not isinstance(LIST.get(message.from_user.id), list):
   LIST[message.from_user.id] = []

  
 
 file_id = str(message.photo.file_id)
 ms = await message.reply_text("Converting to PDF ......")
 file = await client.download_media(file_id)
 
 image = Image.open(file)
 img = image.convert('RGB')
 LIST[message.from_user.id].append(img)
 await ms.edit(f"{len(LIST[message.from_user.id])} image   Successful created PDF if you want add more image Send me One by one\n\n **if done click here 👉 /convert\n\nReport Error @PrivateHelpXBot** ")
 

@app.on_message(filters.command(['convert']))
async def done(client,message):
 images = LIST.get(message.from_user.id)

 if isinstance(images, list):
  del LIST[message.from_user.id]
 if not images:
  await message.reply_text( "No image !!")
  return

 path = f"{message.from_user.id}" + ".pdf"
 images[0].save(path, save_all = True, append_images = images[1:])
 
 await client.send_document(message.from_user.id, open(path, "rb"), caption = "Here your pdf !!")
 os.remove(path)
 
 
 
 
app.run()
