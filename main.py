import os
import discord
from flask import Flask
import threading

# 웹서버 설정 (UptimeRobot 핑 방지용)
app = Flask(__name__)

@app.route('/')
def home():
    return "봇 살아있음!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    thread = threading.Thread(target=run)
    thread.start()

# 디스코드 봇 설정
intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ 봇 로그인됨: {client.user}")

# 실행
keep_alive()
client.run(os.environ['DISCORD_BOT_TOKEN'])
