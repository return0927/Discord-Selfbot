import discord
import json
import asyncio
from random import choice

class Setting:
    def __init__(self):
        self.setting = None

        self.command_prefix = None
        self.commands = {}
        self.keywords = {}

        self.token = ""

        self.load()

    def load(self):
        self.setting = json.loads(open("commands.json", "r", encoding='UTF-8').read())

        self.command_prefix = self.setting['command']['prefix']
        self.commands = self.setting['command']['content']
        self.keywords = self.setting['keyword']

        self.token = self.setting['token']

Settings = Setting()
client = discord.Client()


@client.event
async def on_ready(**kwargs):
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(msg):
    print("서버: {:10}\t채널:{:10}({:5})\t작성자:{:10}\t메세지: {}"
          .format(
        msg.server.name, msg.channel.name, msg.channel.id, msg.author.name, msg.content
    ))

    prefix = msg.content.split(" ")[0]

    # Command Detection:
    for command in Settings.commands.keys():
        if prefix == Settings.command_prefix + command:
            _temp = Settings.commands[command]
            react = _temp if type(_temp) is type("") else choice(_temp)
            react_message = await client.send_message(msg.channel, react)
            await asyncio.sleep(10)
            await client.delete_message(react_message)

            return

    # Keyword Detection
    for keyword in Settings.keywords.keys():
        if keyword in msg.content:
            _temp = Settings.keywords[keyword]
            react = _temp if type(_temp) is type("") else choice(_temp)
            react_message = await client.send_message(msg.channel, react)
            await asyncio.sleep(10)
            await client.delete_message(react_message)

            return # Ends when one keyword reacted



client.run(Settings.token, bot=False)