from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message
from pyrogram import filters
import os
from dotenv import load_dotenv

load_dotenv()
api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')

client = Client(name = 'refresh', api_id = api_id, api_hash = api_hash)#Создаем экземпляр класса Client

@client.on_message(filters.bot)#Фильтруем сообщения - берем только сообщения ботов
def all_message(client: Client, message: Message):#Получаем сообщение и конструктор классов автоматически создает экземпляр класса Message
    message_text = message.text.split()#Режем наше сообщение на список
    if message_text[0] == 'Неизвестная' and message_text[1] == 'команда':#Проверяем первые две первые позиции списка на соответствие фразе 'Неизвестная команда'
        message.delete()#Если условие верно удаляем сообщение

client.run()#Обращаемся к методу run экземпрляра класса client, чтобы все запустить










