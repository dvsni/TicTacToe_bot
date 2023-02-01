from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}, Lets play TicTacToe. /step номер позиции (от 1 до 9)')

async def step(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Step {update.effective_user.first_name}')


app = ApplicationBuilder().token("6126061849:AAHFZx1krnj7VvcpzfC2De9LChPAvBN1j3Q").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("step", step))
print('Telegram bot run')
app.run_polling()

