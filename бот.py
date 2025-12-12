import os
#from dotenv import load_dotenv
from twitchio.ext import commands
import ssl
import asyncio
import aiohttp
import ssl
# Настройка SSL для Windows




#load_dotenv()

TWITCH_TOKEN='oauth:6n6vi71dtwwcry7x981rgn158wghhv'
TWITCH_CLIENT_ID='oyqwkklbdq1mnsunde77a5y1d8y5kt'
TWITCH_CLIENT_SECRET='9c69fyv6jcpk6vdpxzck5hz7zzayqs'
BOT_ID='ekl1f'
TWITCH_BOT_NAME='Eklifbot1'
TWITCH_CHANNEL='ekl1f'


import aiohttp
from aiohttp import ClientSession, TCPConnector

class CustomTCPConnector(TCPConnector):
    def __init__(self, *args, **kwargs):
        kwargs['ssl'] = ssl_context
        super().__init__(*args, **kwargs)

# Подменяем стандартный TCPConnector
aiohttp.TCPConnector = CustomTCPConnector

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            token=TWITCH_TOKEN,
            client_id=TWITCH_CLIENT_ID,
            client_secret=TWITCH_CLIENT_SECRET,
            bot_id=BOT_ID,
            nick=TWITCH_BOT_NAME,
            prefix='!',
            initial_channels=[TWITCH_CHANNEL],
        )
    
    
    async def event_ready(self):
        print (f'Бот {self.nick} успешно подключен')
        print ('Ожидание сообщений в чате...')

    async def event_message(self, message):
        if message.echo:
            return

        print (f'{message.author.name}:{message.content}')
        await self.handle_commands(message)

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f'Привет, {ctx.author.name}!')



if __name__ == "__main__":
    bot=Bot()
    bot.run()
    
        

    
            
            
    

