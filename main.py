from telethon.sync import TelegramClient, events
import time

api_id = 1200079
api_hash = 'e278d876a0cfdca2dc7705e1ec2f9d55'
client = TelegramClient('name', api_id, api_hash)


async def main():
    i = 0
    while i < 5:
        i += 1
        await client.send_message(-1001461743664, 'Test spam block chat')
        time.sleep(2)


with client:
    client.loop.run_until_complete(main())
