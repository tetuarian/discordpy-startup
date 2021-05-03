from discord.ext import commands
import os
import traceback
from datetime import datetime 

bot = commands.Bot(command_prefix='!')
token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = 829494676477181955


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong'):
async def loop():
    now = datetime.now().strftime('%H:%M')
    if now == '04:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('おはよう')  

loop.start()


bot.run(token)
