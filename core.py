import discord
from discord.ext import commands
from discord.ext.commands import Bot

# initialisation des variables.
VERSION = open("core/version.txt").read().replace("\n", "")
TOKEN = open("token/token.txt", "r").read().replace("\n", "")
PREFIX = open("core/prefix.txt", "r").read().replace("\n", "")
client = commands.Bot(command_prefix="{0}".format(PREFIX))
NONE = open("help/cogs.txt", "w")
NONE = open("help/help.txt", "w")

client.remove_command("help")

# Au démarrage du Bot.
@client.event
async def on_ready():
    global GGconnect
    print('Connecté avec le nom : {0.user}'.format(client))
    print('PREFIX = '+str(PREFIX))
    print('\nApero Games '+VERSION)
    print('------\n')
    activity = discord.Activity(type=discord.ActivityType.playing, name="{0}game".format(PREFIX))
    await client.change_presence(status=discord.Status.online, activity=activity)

####################### Commande help #######################

client.load_extension('help.help')


####################### Commande game #######################

client.load_extension('game.bypierrot')


####################### Welcome ####################################

@client.event
async def on_guild_join(guild):
    if guild.system_channel != None:
        systemchannel = guild.system_channel
    else:
        systemchannel = 0
    await systemchannel.send('Bonjour **{0}**!'.format(guild.name))

####################### Lancemement du bot ######################

try:
    client.run(TOKEN)
except (KeyboardInterrupt, SystemExit):
    pass
