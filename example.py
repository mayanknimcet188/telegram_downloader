from telethon import TelegramClient
api_id = 1771007
api_hash = 'fcdefde9a8eb6f29c06e7b763a09da0c'
client = TelegramClient('mayank',api_id,api_hash)

async def main():
    #getting information about yourself
    me = await client.get_me()
    #print me user object by beautifying it using "stringify" method:
    print(me.stringify())

    username = me.username
    print(username)
    print(me.phone)

    async for dialog in client.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)

    await client.send_message('me',"hello")
    await client.send_message('+918473975406','Hello from Telethon!')

with client:
    client.loop.run_until_complete(main())

