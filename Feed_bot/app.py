from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


#handlers
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Hello\nWrite something to me")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Write something to me and I forward your message to you")

@dp.message_handler()
#If you do not specify the library of the
# message being processed, then by default only processing text messages
async def echo_message(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


#polling
if __name__ == '__main__':
    executor.start_polling(dp)