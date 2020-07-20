from telethon.sync import TelegramClient, events
from tqdm import tqdm
import os

api_id = 1771007
api_hash = 'fcdefde9a8eb6f29c06e7b763a09da0c'

with TelegramClient('mayank',api_id,api_hash) as client:
    messages = client.get_messages('techalgo',limit=50)

    for msg in tqdm(messages):
        msg.download_media(file = os.path.join('media','algo'))
