import asyncio
from telebot.async_telebot import AsyncTeleBot
from tokenFile import token
from commands import BotCommands


async def main():
    bot = AsyncTeleBot(token) # Инициализация самого бота
    bot_commands = BotCommands(bot) # Подключение модуля команд

    print("Bot started...")
    await bot.polling() # Запуск бота

if __name__ == "__main__":
    asyncio.run(main())