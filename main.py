import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"로그인됨: {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!뽑기":
        await message.channel.send("🎴 카드 뽑기 성공!")

TOKEN = os.getenv("5yvQ-AZRcsi5fvMQ_0I3a1UV7apkuBGR")
client.run(5yvQ-AZRcsi5fvMQ_0I3a1UV7apkuBGR)
