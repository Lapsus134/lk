import requests
import random
import string
import time
import discord
from discord.ext import commands

num = 1000000

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"Generated {num} codes | Time taken: {time.time() - start}\n")
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$',intents=intents)
client = discord.Client(intents=intents, command_prefix="$")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('nitro2'):
        with open("Nitro Codes.txt") as file:
            for line in file.readlines():
                nitro = line.strip("\n")

                url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

                r = requests.get(url)

                if r.status_code == 200:
                    print(f" Valid | {nitro} ")
                    await message.channel.send(f" Valid | {nitro} ")
                    break
                else:
                    print(f" Invalid | {nitro} ")
client.run('to')