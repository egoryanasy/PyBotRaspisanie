from telebot import types
from storage import IDStorage


class CallbackHandlers:
    def __init__(self, bot, storage):
        self.bot = bot
        self.storage = storage

    async def handle_callback(self, call):
        """Основной обработчик колбэков"""
        if call.data == "course1":
            await self.handle_course1(call)
        elif call.data == "course2":
            await self.handle_course2(call)
        elif call.data == "course3":
            await self.handle_course3(call)
        elif call.data == "course4":
            await self.handle_course4(call)
        elif call.data == "teacher":
            await self.handle_teacher(call)
        elif call.data == "gr404":
            await self.handle_group404(call)
        elif call.data == "gr405":
            await self.handle_group405(call)
        elif call.data == "gr406":
            await self.handle_group406(call)

    async def handle_course1(self, call):
        await self.bot.send_message(call.message.chat.id, "первый курс")

    async def handle_course2(self, call):
        await self.bot.send_message(call.message.chat.id, "второй курс")

    async def handle_course3(self, call):
        await self.bot.send_message(call.message.chat.id, "третий курс")

    async def handle_course4(self, call):
        fourth = types.InlineKeyboardMarkup()
        group404 = types.InlineKeyboardButton(text="ИСП-404", callback_data="gr404")
        group405 = types.InlineKeyboardButton(text="ИСП-405", callback_data="gr405")
        group406 = types.InlineKeyboardButton(text="ИСП-406", callback_data="gr406")

        fourth.add(group404, group405, group406)

        await self.bot.send_message(call.message.chat.id,
                                    "Выберите группу 4 курса",
                                    reply_markup=fourth)

    async def handle_teacher(self, call):
        await self.bot.send_message(call.message.chat.id, "Преподаватель")

    async def handle_group404(self, call):
        await self.bot.send_message(call.message.chat.id,
                                    "Вы успешно выбрали группу ИСП-404")

    async def handle_group405(self, call):
        await self.bot.send_message(call.message.chat.id,
                                    "Вы успешно выбрали группу ИСП-405")

    async def handle_group406(self, call):
        await self.bot.send_message(call.message.chat.id,
                                    "Вы успешно выбрали группу ИСП-406")