from telethon.sync import TelegramClient, events
import time

api_id = 1200079
api_hash = 'e278d876a0cfdca2dc7705e1ec2f9d55'
client = TelegramClient('anon', api_id, api_hash)


async def main():
    i = 15
    while i < 15:
        await client.send_message(-1001461743664, 'Test spam block chat')
        await client.send_file(-1001461743664, 'C:/Users/Роман/Desktop/tg/photo.jpg')
        time.sleep(2)


with client:
    client.loop.run_until_complete(main())
