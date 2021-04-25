from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


# handlers
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Hello!\nYou can send me telegram channel links and I can send you news posts from these chanells.")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await bot.send_message(message.from_user.id, "*list of commands*")


@dp.message_handler()
async def echo_message(message: types.Message):
    await bot.send_message(message.from_user.id, "To use the bot, use the commands.\nTo get a list of commands, "
                                                 "use the command '/help'.")


#polling
if __name__ == '__main__':
    executor.start_polling(dp)