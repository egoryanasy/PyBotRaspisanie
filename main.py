import asyncio
from telebot.async_telebot import AsyncTeleBot
from tokenFile import token
from commands import BotCommands


async def main():
    bot = AsyncTeleBot(token)
    bot_commands = BotCommands(bot)

    print("Bot started...")
    await bot.polling()


if __name__ == "__main__":
    asyncio.run(main())