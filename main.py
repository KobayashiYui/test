import telegram.ext

print("run")
def start(update, context):
    update.message.reply_text("Hello")

def help(update, context):
    update.message.reply_text("""
    this is the user guile
    sss

    
 
    ddd
    """)


updater = telegram.ext.Updater('5356615227:AAGpUBcjU0zCI8jTdTu0qR6bnLVpXgWupbg', use_context=True)

disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))

updater.start_polling()
updater.idle()
