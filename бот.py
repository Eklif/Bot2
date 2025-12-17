import os
import twitchio
from twitchio.ext import commands
import logging
from twitchio.utils import setup_logging
from dotenv import load_dotenv

load_dotenv()
setup_logging(level=logging.INFO)



# Все ваши параметры
TWITCH_TOKEN = os.getenv('TWITCH_TOKEN')
TWITCH_CLIENT_ID = 'oyqwkklbdq1mnsunde77a5y1d8y5kt'
TWITCH_CLIENT_SECRET = os.getenv('TWITCH_CLIENT_SECRET')
BOT_ID = '104844002'  # Ваш числовой ID
TWITCH_CHANNEL = '104844002'
name='EklifBot'

class Bot(commands.Bot):
    def __init__(self):
        # Передаем ВСЕ обязательные параметры
        super().__init__(
            token=TWITCH_TOKEN,
            client_id=TWITCH_CLIENT_ID,
            client_secret=TWITCH_CLIENT_SECRET,
            initial_channels=[TWITCH_CHANNEL],
            bot_id=BOT_ID,
            prefix="!",
            #name=BOT_NICK,
        )
        
    async def event_ready(self):
        #Called when the bot is connected to Twitch.
        #print(f' Бот {bot.name} подключен')
        print(f'Urer ID | {self.bot_id}')
        await self.fetch_channel(TWITCH_CHANNEL)#.send(f'{bot.name} is online')

    async def event_message(self, message):
        #Called every time a message is sent in an observed channel.
        if message.author.name.lower()==self.name.lower():
            return
        print(f'[{message.channel.name}] {message.author.name}: {message.content}')
        await self.handle_commands(message)

    @commands.command(name='hello')
    async def hello(self, ctx:commands.Context):
        await ctx.send(f'Hello {ctx.author.name}!Я есть ТвичИО 3.1.0 бот')

if __name__== "__main__":
    bot=Bot()
    bot.run()
        
        


