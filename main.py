from telethon.sync import TelegramClient
import time
import random
from list import chat_id

api_id = id
api_hash = 'hash'
client = TelegramClient('user', api_id, api_hash)
t = open('text.txt', 'r', encoding='utf-8')
text = t.read()


async def spam():
    s = open('chats.txt', 'r')
    n = 0
    while True:
        f = open('output.txt', 'r')
        i = f.readline()
        if i == 'start_text_send':
            await client.send_message(chat_id[n], text)
            n += 1
            time.sleep(random.randrange(3, 5, 1))
            await client.send_message('user', 'send ' + str(n) + ' from 122')
            time.sleep(random.randrange(3, 8, 1))
            if chat_id[n] == chat_id:
                await client.send_message('user', 'stop sleep wait')
                time.sleep(13650)
            else:
                continue
        else:
            continue


with client:
    client.loop.run_until_complete(spam())
