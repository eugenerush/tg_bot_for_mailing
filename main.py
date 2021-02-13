from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
import time

api_id = 3636832
api_hash = '775dbb2c1edce433a4dac365f78a7faa'
client = TelegramClient('user', api_id, api_hash)
t = open('text.txt', 'r', encoding='utf-8')
text = t.read()


'''async def main():
    f = open('chats.txt', 'r')
    i = 0
    while i <= 155:
        channel = f.readline()
        await client(JoinChannelRequest(channel))
        i += 1
        time.sleep(5)'''


async def spam():
    #  s = open('chats.txt', 'r')
    while True:
        f = open('output.txt', 'r')
        i = f.readline()
        #  channel = s.readline()
        if i == 'start_text_send':
            await client.send_message('maykovskiy', text)
            time.sleep(3)
        else:
            continue


with client:
    client.loop.run_until_complete(spam())
