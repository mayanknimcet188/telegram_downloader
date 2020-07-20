from telethon import TelegramClient

#api_id
api_id = 1771007
api_hash = 'fcdefde9a8eb6f29c06e7b763a09da0c'

#first parameter is the seesion file name 
with TelegramClient('anon',api_id,api_hash) as client:
    client.loop.run_until_complete(client.send_message('me','Hello, myself!'))
