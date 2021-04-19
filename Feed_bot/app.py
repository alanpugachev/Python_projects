from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN


def notifications_text_switcher(enable):
    if enable:
        return "disabled"
    if not enable:
        return "enabled"
# !COMING SOON! notification switcher


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


# handlers
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Hello!\nYou can send me telegram channel links and I can send you news posts from these chanells.",
                           disable_notification=False)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await bot.send_message(message.from_user.id, "*list of commands*", disable_notification=False)


@dp.message_handler(commands=['notifications'])
async def process_notifications_command(message: types.Message):
    await bot.send_message(message.from_user.id, f"Notifications {notifications_text_switcher(False)}", disable_notification=False)


@dp.message_handler()
# If you do not specify the library of the
# message being processed, then by default only processing text messages
async def echo_message(message: types.Message):
    await bot.send_message(message.from_user.id, "To use the bot, use the commands.\nTo get a list of commands, use the command '/help'.")


#polling
if __name__ == '__main__':
    executor.start_polling(dp)