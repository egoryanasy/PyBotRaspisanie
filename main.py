import asyncio
from contextlib import nullcontext

from telebot.async_telebot import AsyncTeleBot

from tokenFile import token

subscribed_IDS = list()

subscribed_IDSFile = open("subscribed_IDS.txt","r")
for line in subscribed_IDSFile:
    subscribed_IDS.append(line.strip())

async def SaveSubscribedIDs():
    with open("subscribed_IDS.txt","w") as f:
        for ID in subscribed_IDS:
            f.write(ID+"\n")
        print("Saved subscribedIDs.txt.")

bot = AsyncTeleBot(token)
@bot.message_handler(commands=['start'])
async def send_welcome_message(message):
    print("Start used.")
    if message == nullcontext:
        return
    if str(message.chat.id) not in subscribed_IDS:
        subscribed_IDS.append(str(message.chat.id))
        await SaveSubscribedIDs()

    text = ("Добро пожаловать, выберите группу!\n" +
            "Вы подписались на уведомление о обновлении расписания!\n"
            "Чтобы отписаться напишите /unsubscribe")
    await bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['unsubscribe'])
async def send_unsubscribe_message(message):
    print("Unsubscribed used")
    if message == nullcontext:
        return
    if str(message.chat.id) in subscribed_IDS:
        subscribed_IDS.remove(str(message.chat.id))
        await SaveSubscribedIDs()
        await bot.send_message(message.chat.id,"Вы успешно отписались. Чтобы подписаться\n"
                                               "напишите /subscribe")

@bot.message_handler(commands=['subscribe'])
async def send_subscribe_message(message):
    print("Subscribed used")
    if message == nullcontext:
        return
    if str(message.chat.id) not in subscribed_IDS:
        subscribed_IDS.append(str(message.chat.id))
        await SaveSubscribedIDs()
        await bot.send_message(message.chat.id, f"Вы успешно подписались, чтобы отписаться\n"+
                                                "напишите /unsubscribe")

asyncio.run(bot.polling())