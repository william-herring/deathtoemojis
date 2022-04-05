import discord
import dotenv

token = dotenv.get_key('.env', 'TOKEN')


class Client(discord.Client):
    async def on_ready(self):
        print('Logged on as ' + str(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return
        print(message.content)


client = Client()
client.run(token)
