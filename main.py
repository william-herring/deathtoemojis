import discord
import os
import random
import emoji

token = os.getenv('TOKEN')
banned_msgs = ['rip', 'RIP', 'L', 'oui', 'OUI', 'oui oui', 'ouioui', 'OUIOUI', 'OUI OUI', 'unluggy', 'tru', 'TRU', 'choggers']


class Client(discord.Client):
    async def on_ready(self):
        print('Logged on as ' + str(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content in banned_msgs:
            await message.channel.send(random.choice(banned_msgs))
            await message.author.kick(reason='rip')

        for i in message.content:
            if i in emoji.UNICODE_EMOJI['en']:
                await message.channel.send(random.choice(banned_msgs))
                await message.author.ban(reason='we dont like that lol')


client = Client()
client.run(token)
