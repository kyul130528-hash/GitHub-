import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'로그인 완료: {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!뽑기":
        await message.channel.send("🎴 카드 뽑기 성공!")

TOKEN = os.environ.get("DISCORD_TOKEN")

if TOKEN is None:
    print("토큰 없음! Environment 설정 확인")
else:
    client.run(e80dZ8ojjkzNV_9k2GpSK-sH-s_KeXb-)
