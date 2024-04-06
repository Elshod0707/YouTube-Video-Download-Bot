# ©️ Tushar 

from pyrogram import Client, filters
from pytube import YouTube
import asyncio

# Replace 'YOUR_API_ID', 'YOUR_API_HASH', and 'YOUR_BOT_TOKEN' with your actual values
API_ID = '21125888'
API_HASH = 'b03021a37d433123ca5e3635036ba8db'
BOT_TOKEN = '6990332801:AAGm7f1nXyP6vkvM4INbHoBLhRgbEPKXRlE'

# Create a Pyrogram client
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Start command handler
@app.on_message(filters.command("tushar"))
def start(client, message):
    user = message.from_user
    message.reply_text(f"Hello, @{user.username}!\n\nSend me the YouTube link of the video you want to upload.")

# Help command handler
@app.on_message(filters.command("help"))
def help(client, message):
    help_text = """
    Welcome to the YouTube Video Uploader Bot!

To upload a YouTube video, simply send me the YouTube link.
    
Enjoy using the bot!

   ©️ Channel : @AIM_AIIMS143
    """
    message.reply_text(help_text)

# Message handler for processing YouTube links
@app.on_message(filters.regex(r'^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+'))
async def process_youtube_link(client, message):
    youtube_link = message.text
    try:
        # Downloading text message
        downloading_msg = await message.reply_text("Downloading video...")

        # Download the YouTube video
        yt = YouTube(youtube_link)
        video = yt.streams.filter(progressive=True, file_extension='mp4').first()
        video.download(filename='downloaded_video.mp4')

        # Uploading text message
        uploading_msg = await message.reply_text("Uploading video...")

        # Send the video file to the user
        sent_message = await app.send_video(message.chat.id, video=open('downloaded_video.mp4', 'rb'), caption=yt.title)

        # Delay for a few seconds and delete downloading and uploading
        await downloading_msg.delete()
        await uploading_msg.delete()
        await asyncio.sleep(2)

         # Delete downloading and uploading text messages
        await app.delete_messages(message.chat.id, [downloading_msg.message_id, uploading_msg.message_id])
    except Exception as e:
        error_text = 'BOT MADE BY : @Tushar_1665🌟\nFor the List of Telegram'
        await message.reply_text(error_text)
        
# Start the bot
print("🎊 I AM ALIVE 🎊")
app.run()
