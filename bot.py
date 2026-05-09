import json
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

import os
TOKEN = os.environ.get("BOT_TOKEN")

with open("data.json", "r", encoding="utf-8") as file:
    database = json.load(file)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send your full name and I will give you your ID.")

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.message.text.strip()

    if name in database:
        await update.message.reply_text(f"Your ID is: {database[name]}")
    else:
        await update.message.reply_text("Name not found.")

print("Bot is starting...")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search))

import asyncio

async def main():
    print("Bot starting...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
