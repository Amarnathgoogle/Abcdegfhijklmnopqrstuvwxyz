import discord


# Replace YOUR_BOT_TOKEN with your actual bot token
client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello, I am a Discord self bot!')

client.run('MTIzMjAxNzAwNjIzMjg2Njg4OQ.GyjX5n.QtScR12cGjUc_QTcQKXGJ_H5a16PjBvXbRjQsg')
