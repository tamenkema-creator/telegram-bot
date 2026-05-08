import json
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# 🔑 Put your bot token here
TOKEN = os.environ.get("BOT_TOKEN")

# 📂 Load your data file
with open("data.json", "r", encoding="utf-8") as file:
    database = json.load(file)

# 👋 Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send your full name and I will give you your ID.")

# 🔍 Search function
async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.message.text.strip()

    if name in database:
        await update.message.reply_text("Your ID is: " + database[name])
    else:
        await update.message.reply_text("Name not found.")

# 🚀 Start bot
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search))

app.run_polling()
