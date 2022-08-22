import logging
from telegram import *
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import os
import time
import instaloader

#Environment Variables
USER = os.environ.get('ig_username')
PASSWORD = os.environ.get('ig_password')
API_Hash = os.environ.get('BOT_API_TOKEN')
CHANNELID = int(os.environ.get('channel'))
password = os.environ.get('secret_command')
time_sleep = int(os.environ.get('every_x_minutes'))
posts_to_scrape = int(os.environ.get('no_of_posts'))
channel_bot_start_msg = os.environ.get('Welcome_Message')
CAPTION = os.environ.get('every_post_caption')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def scrape_feed():
    L = instaloader.Instaloader()
    L.login("{}".format(USER), "{}".format(PASSWORD))      # (login)
    L.download_feed_posts(max_count=posts_to_scrape, fast_update=True, post_filter=None)
    print("\n"+"Downloading feed : Done!")

async def post_scrape(update: Update, context: ContextTypes):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="***Bot Started Collecting Posts Successfully!*** \n \n ___Go to your respective channel now___",parse_mode= 'Markdown')    
    await context.bot.send_message(chat_id=CHANNELID, text=channel_bot_start_msg, parse_mode= 'Markdown')
    await context.bot.send_sticker(chat_id=CHANNELID, sticker='CAACAgEAAxkBAAEFonRjAwlCFg3_h8NDZn2Yr7l2mu86wAACNAEAApHV8Ec2k-NTOFBhtCkE')

    #Loop Where the main logic begins
    while True:
        n = 1
        checkdownload_dir = "./：feed"
        temp_downloaded_files = os.listdir('./：feed/')
        for unnecessary_files in temp_downloaded_files:
            unPath=os.path.join(checkdownload_dir,unnecessary_files)
            os.remove(unPath)
            print("Unnecessary files were removed!!")
        
        scrape_feed()
        print("Sending from feed. \n")
        time.sleep(30)
        download_dir = "./：feed"
        downloaded_files = os.listdir('./：feed/')
        downloads = []
        for lists in downloaded_files:
            files = os.path.join(download_dir,lists)
            downloads.append(files)
        #print(downloads)

        media_group = []
        temp_list = list()
        postcount = 0
        for posts in downloads:
            if posts.endswith(".mp4"):
                #print(posts)
                media_group.append(InputMediaVideo(open(posts,'rb'),caption = CAPTION if postcount == 0 else ''))
                postcount += 1
                temp_list.append(posts)
            elif posts.endswith(".jpg"):
                #print(posts)
                media_group.append(InputMediaPhoto(open(posts,'rb'), caption = CAPTION if postcount == 0 else ''))
                postcount += 1
                temp_list.append(posts)
            elif posts.endswith(".txt"):
                #Opening Text file
                a= open(posts,'r',encoding="utf8")
                caption = a.read()
                sdsd = caption.split(" ")
                wordcount = 0
                postcount = 0
                #Removing unncessary stuffs
                for words in sdsd:
                    if words[:1]=="#" or words[:1]=="@" or words[:1]=="\n" or words[:1]=="©" or words[:2]=="##" or words[:1]=="." or words[:2]=="  " or words[:1]==".":
                        break
                    else:
                        wordcount = wordcount +1 
                while len(sdsd)-1 >= wordcount:
                    sdsd.remove(sdsd[wordcount])
                    wordcount = wordcount + 1
                sentence = ' '.join(sdsd)
                first_file = temp_list[0]
                if len(temp_list)==1:
                    if first_file.endswith(".jpg"):
                        print("Sending Photo as single file")
                        await context.bot.send_photo(chat_id = CHANNELID, photo=open(first_file, 'rb'), caption="▶ " + sentence+"\n"+CAPTION)
                        print("Sent {} Post".format(str(n)))
                        n =+1
                    os.remove(first_file)
                    media_group.clear()
                    temp_list.clear()
                    time.sleep(30)
                else:
                    await context.bot.send_message(chat_id=CHANNELID, text="▶ "+sentence)
                    #print(media_group)
                    await context.bot.send_media_group(chat_id = CHANNELID, media = media_group)
                    media_group.clear()
                    for files in temp_list:
                        print("Removed already sent files.")
                        os.remove(files)
                    temp_list.clear()
                    print("Sent {} Post".format(str(n)))
                    n += 1
                    time.sleep(20)
                    await context.bot.send_sticker(chat_id=CHANNELID, sticker='CAACAgEAAxkBAAEFonRjAwlCFg3_h8NDZn2Yr7l2mu86wAACNAEAApHV8Ec2k-NTOFBhtCkE')
                    time.sleep(20)
                a.close()
                print("Removed Text File \n \n")
                os.remove(posts)
            else:
                print("Removed Clutter Files.")
                os.remove(posts)      
        print("I need a rest of {} minutes.".format(time_sleep))
        n =0
        time.sleep(time_sleep*60)

async def start(update: Update, context: ContextTypes):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="***Bot Started Successfully.*** \n \n ___Enter password as command to run in Channel___",parse_mode= 'Markdown')


if __name__ == '__main__':
    application = ApplicationBuilder().token(API_Hash).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    mid_handler = CommandHandler(password, post_scrape)
    application.add_handler(mid_handler)
    
    application.run_polling()