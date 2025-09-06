from math import acosh

from telebot.async_telebot import AsyncTeleBot
from storage import IDStorage
from telebot import types


class BotCommands:
    def __init__(self, bot: AsyncTeleBot): # Модуль инициализации
        self.bot = bot
        self.storage = IDStorage()
        self.setup_handlers()

    def setup_handlers(self):
        @self.bot.message_handler(commands=['start'])
        # Переход в начало или начало работы с ботом
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
        # Отписка от уведомлений об изменении расписания
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
        # Подписка на уведомление об изменении расписания
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
        # Проверка подписки на увдеомление об изменении расписания
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
        # Поменять привязку к группе с inline кнопками
        async def send_change_message(message):
            print("Change used")
            keyboard = types.InlineKeyboardMarkup()
            course1 = types.InlineKeyboardButton(text="1 курс", callback_data="course1")
            course2 = types.InlineKeyboardButton(text="2 курс", callback_data="course2")
            course3 = types.InlineKeyboardButton(text="3 курс", callback_data="course3")
            course4 = types.InlineKeyboardButton(text="4 курс", callback_data="course4")

            keyboard.add(course1, course2)
            keyboard.add(course3, course4)

            await self.bot.send_message(message.chat.id,
                                    "Выберите курс Ваш курс:",
                                    reply_markup=keyboard)

        @self.bot.callback_query_handler(func=lambda call: True)
        # Обработка inline кнопок
        async def callback(call):
            if call.data == "course1":
                await self.bot.send_message(call.message.chat.id, "первый курс")
            if call.data == "course2":
                await self.bot.send_message(call.message.chat.id, "второй курс")
            if call.data == "course3":
                await self.bot.send_message(call.message.chat.id, "третий курс")
            if call.data == "course4":
                await self.bot.send_message(call.message.chat.id, "четвертый курс")
