import discord
import requests
import asyncio
import json
from Settings import *


# Extends the discord-py Client
class Client(discord.Client):
    def __init__(self, *args, **kwargs):
        super(Client, self).__init__(*args, **kwargs)
        # Sets up the task that refreshes our access token
        self.accessToken = ""
        self.loop.create_task(self.refreshAccessToken())

    async def refreshAccessToken(self):
        # Grab a new access token every 25 minutes
        url = CurseCopAPI + 'token'
        curseCopLogin = {'email': CurseCopUsername,
                         'password': CurseCopPassword}
        x = requests.post(url, data=json.dumps(curseCopLogin))
        print(x.text)
        self.accessToken = x.json()["access_token"]
        await asyncio.sleep(1500)
        self.loop.create_task(self.refreshAccessToken())

    def shouldFilterMessage(self, message):
        # Sends a request to the API to filter the message
        url = CurseCopAPI + '@me/filter'
        Message = {'text': message.content}
        headers = {'content-type': 'application/json',
                   'Authorization': "Bearer " + self.accessToken}
        x = requests.post(url, data=json.dumps(Message), headers=headers)
        # If the API says there were matches, return True
        return len(x.json()["matches"]) != 0

    async def on_message(self, message):
        # When the bot receives a message, send it to be filtered
        if self.shouldFilterMessage(message):
            await message.delete()


# run the bot
client = Client()
client.run(DiscordBotToken)
