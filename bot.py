# code dev by t.me/Prime_Hritu
# © Hritu
# Use The Code With Credits To t.me/Prime_Hritu otherwise Strict Action will be taken
import os
from PIL import Image
from pyrogram import Client,filters 
from pyrogram.types import (InlineKeyboardButton,  InlineKeyboardMarkup)
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from myrogram import notJoin , forceMe , STARTER , BOTBY

TOKEN = os.environ.get("TOKEN", "")

API_ID = int(os.environ.get("API_ID", ))

API_HASH = os.environ.get("API_HASH", "")

app = Client(
        "pdf",
        bot_token=TOKEN,api_hash=API_HASH,
            api_id=API_ID
    )

print("Bot Started! © t.me/Prime_Hritu")
LIST = {}

@app.on_message(filters.command(['start']))
def start(client, message):
 res = forceMe(message.chat.id)
 if res == "no":
   return notJoin(client,message)
 message.reply_text(text =f"""Hello {message.from_user.first_name } , I Am image to pdf bot 

i can convert image to pdf

**Send Me Images And At End Send /convert**

This bot created by {BOTBY}""",reply_to_message_id = message.id ,  reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Updates Channel 🇮🇳" ,url=f"https://t.me/Private_Bots") ],
[
                    InlineKeyboardButton("Developer 💀" ,url="https://t.me/Prime_Hritu") ],
[
                    InlineKeyboardButton("Source Code 👀" ,url="https://github.com/Prime-Hritu/image2pdf-Bot") ]
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
