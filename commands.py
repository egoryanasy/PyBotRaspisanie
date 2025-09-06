from telebot.async_telebot import AsyncTeleBot
from storage import IDStorage


class BotCommands:
    def __init__(self, bot: AsyncTeleBot):
        self.bot = bot
        self.storage = IDStorage()
        self.setup_handlers()

    def setup_handlers(self):
        @self.bot.message_handler(commands=['start'])
        async def send_welcome_message(message):
            print("Start used.")
            added = await self.storage.add_id(str(message.chat.id))

            text = "Добро пожаловать, выберите группу!\n"
            if added:
                text += "Вы подписались на уведомление о обновлении расписания!\n"
            else:
                text += "Вы уже подписаны на уведомления.\n"
            text += "Чтобы отписаться напишите /unsubscribe"

            await self.bot.send_message(message.chat.id, text)

        @self.bot.message_handler(commands=['unsubscribe'])
        async def send_unsubscribe_message(message):
            print("Unsubscribe used")
            removed = await self.storage.remove_id(str(message.chat.id))

            if removed:
                await self.bot.send_message(
                    message.chat.id,
                    "Вы успешно отписались. Чтобы подписаться напишите /subscribe"
                )
            else:
                await self.bot.send_message(
                    message.chat.id,
                    "Вы не были подписаны на уведомления."
                )

        @self.bot.message_handler(commands=['subscribe'])
        async def send_subscribe_message(message):
            print("Subscribe used")
            added = await self.storage.add_id(str(message.chat.id))

            if added:
                await self.bot.send_message(
                    message.chat.id,
                    "Вы успешно подписались! Чтобы отписаться напишите /unsubscribe"
                )
            else:
                await self.bot.send_message(
                    message.chat.id,
                    "Вы уже подписаны на уведомления."
                )

        @self.bot.message_handler(commands=['status'])
        async def send_status_message(message):
            is_subscribed = await self.storage.contains_id(str(message.chat.id))

            if is_subscribed:
                await self.bot.send_message(
                    message.chat.id,
                    "✅ Вы подписаны на уведомления"
                )
            else:
                await self.bot.send_message(
                    message.chat.id,
                    "❌ Вы не подписаны на уведомления"
                )
        @self.bot.message_handler(commands=['change'])
        async def send_change_message(message):
            print("Change used")
