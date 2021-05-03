import discord

TOKEN = 'ODM0Mzc0NzExNjc2NjMzMDg5.YH_-AQ.S1hQ2y8FP45tiZ6D9EoHvRk1274'

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/neko':
        await message.channel.send('にゃーん')

client.run(TOKEN)
