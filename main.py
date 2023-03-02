import asyncio
import discord
import sys

intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)

async def run_script(script_name):
    print(f"{script_name} is running...")
    # Add your script execution code here

async def embed_menu():
    embed = discord.Embed(title="Script Runner", description="React with a number to run a script", color=0x00ff00)
    embed.add_field(name="1️⃣ Script 1", value="Runs script 1", inline=False)
    embed.add_field(name="2️⃣ Script 2", value="Runs script 2", inline=False)
    embed.add_field(name="3️⃣ Script 3", value="Runs script 3", inline=False)

    msg = await client.get_channel(1076133239476998246).send(embed=embed)

    reactions = ["1️⃣", "2️⃣", "3️⃣"]
    for reaction in reactions:
        await msg.add_reaction(reaction)

    try:
        reaction, user = await client.wait_for('reaction_add', timeout=20.0, check=lambda reaction, user: user != client.user and str(reaction.emoji) in reactions)
        if str(reaction.emoji) == "1️⃣":
            await run_script("Script 1")
        elif str(reaction.emoji) == "2️⃣":
            await run_script("Script 2")
        elif str(reaction.emoji) == "3️⃣":
            await run_script("Script 3")
    except asyncio.TimeoutError:
        print("Timeout occurred")
        await client.get_channel(1076133239476998246).send('Time out!')
    finally:
        await msg.delete()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content == "!menu":
        # role = discord.utils.get(message.guild.roles, name='Runner',id="1079666888533086228")
        role = discord.utils.get(message.guild.roles, name='Runner')
        if role in message.author.roles:
            await message.delete() # Delete the user's message
            await embed_menu()
        else:
            await message.channel.send('Sorry, you do not have permission to use this command.')

client.run('NzIzOTUwOTc4ODM1MTUyOTY2.G_udop.OMnyLv4IKrbvNQ_etQr68l6HoTDsExykKuNPyY')
