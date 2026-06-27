from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = “8502310716:AAFf3qltc727re0ztB2CTnLWlQd8flFii3A
”

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text(
“🎉 Welcome to Ubayy Creative Studio!\n\n”
“We offer:\n”
“• Logo Design\n”
“• Flyers & Posters\n”
“• Business Cards\n”
“• Social Media Designs\n”
“• Certificates\n”
“• Branding\n\n”
“Send us a message to get started.”
)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler(“start”, start))

print(“Bot running…”)
app.run_polling()
