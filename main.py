import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Bật logging để debug
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Lệnh /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Xin chào! Bot Telegram của bạn đã hoạt động ✅")

# Lệnh /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Các lệnh có sẵn: /start, /help")

def main():
    # 🔑 Thay TOKEN của bạn vào đây
    application = Application.builder().token("YOUR_TELEGRAM_BOT_TOKEN").build()

    # Thêm các lệnh
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Chạy bot
    application.run_polling()

if __name__ == "__main__":
    main()
