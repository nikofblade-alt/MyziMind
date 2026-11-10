import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🚀 Ouvrir MIZY MIND", web_app=WebAppInfo(url=WEBAPP_URL))],
    ]
    await update.message.reply_text(
        "👋 Bienvenue sur *MIZY MIND* 🔥\n\nRobot pour Pocket Option OTC.\nAppuie en bas pour ouvrir l'app.",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("MIZY MIND lance...")
    app.run_polling()
