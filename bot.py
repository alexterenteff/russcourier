import logging
import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

# --- Настройка логирования ---
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# Токен бота берём из переменной окружения (задаётся в Railway),
# чтобы не хранить его в коде и в GitHub-репозитории.
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Ссылка, на которую ведёт кнопка "Связаться" — открывает личный чат в Telegram.
CONTACT_URL = "https://t.me/agterentev"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /start."""
    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("Связаться", url=CONTACT_URL)]]
    )
    await update.message.reply_text(
        "Привет, это проект Русский курьер",
        reply_markup=keyboard,
    )


def main() -> None:
    if not BOT_TOKEN:
        raise RuntimeError(
            "Не найдена переменная окружения BOT_TOKEN. "
            "Задайте её в настройках Railway (Variables)."
        )

    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    logger.info("Бот запущен и слушает обновления (polling)...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
