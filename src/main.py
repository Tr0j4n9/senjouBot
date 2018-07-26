import discord      # pip3 install discord.py
import asyncio
from discord import Game, Embed, Color, Status, ChannelType
from discord.ext import commands
from os import path


# Default command prefix is set to '>', change it here if you want
PREFIX = ">"

# Creating selfbot instance
bot = commands.Bot(command_prefix=PREFIX, description='''Selfbot by zekro''', self_bot=True)


#####################
# L I S T E N E R S #
#####################

@bot.event
async def on_ready():
    """
    Printing username + discriminator and user ID
    when bot is finished logging in and ready
    """
    print(
            "\n +--------------------------------------------+"
            "\n |        senjouBot - discord self-bot        |"
            "\n | (c) 2017 Ringo Hoffman (zekro Development) |"
            "\n +--------------------------------------------+\n"
         )
    print("Logged in as %s#%s" % (bot.user.name, bot.user.discriminator))
    print("ID: " + bot.user.id)
    


   
@bot.command(pass_context = True)
async def dm(ctx, member : discord.Member = None, *, message):
    if not ctx.message.author.server_permissions.administrator:
        return
    if not member:
        return await client.say(ctx.message.author.mention + "Specify a user to DM!")
    if member == "@everyone":
        for server_member in ctx.message.server.members:
        await client.send_message(server_member, message)
    else:
        await client.send_message(member, message)


###################
# C O M M A N D S #
###################

@bot.command(pass_context=True)
async def test(ctx, *args):
    """
    Just a command for testing purposes and debugging
    """
    print(ctx.message.server.get_member(bot.user.id).game)
    

# Testing if file 'token.txt' exists. If it is so, then the token
# will be read out of this file. If not, the user will be asked
# for the token in the console to enter, wich will be saved in this
# file after and the bot will log in
if path.isfile("token.txt"):
    with open("token.txt") as f:
        token = f.readline()
    print("[INFO] Starting up and logging in...")
    bot.run(token, bot=False)
else:
    print("Please enter your discord account token (bot a bot account token!):")
    token = input()
    print("[INFO] Saving token...")
    with open("token.txt", "w") as f:
        f.write(token)
    print("[INFO] Starting up and logging in...")
    bot.run(token, bot=False)

