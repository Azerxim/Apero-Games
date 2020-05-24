import discord
from discord.ext import commands
from discord.ext.commands import bot
from game import gameFonctions as GF
import random as r


class ByPierrot(commands.Cog):

    def __init__(self, ctx):
        return(None)

    @commands.command(pass_context=True)
    async def game(self, ctx):
        """Jouer au jeu"""
        data = GF.read("game/rules.json")
        rules = data["rules"]
        for one in data["new"]:
            rules.append(one)
        rules.append(data["special"])
        drules = list()
        i = 0
        while i < len(rules):
            drule = rules[r.randint(0, len(rules)-1)]
            if not drule in drules:
                drules.append(drule)
                i += 1
        rule = drules[r.randint(0, len(drules)-1)]
        await ctx.channel.send(rule)

    @commands.command(pass_context=True)
    async def rules(self, ctx):
        """Affiche toutes les règles"""
        data = GF.read("game/rules.json")
        rules = data["rules"]
        for one in data["new"]:
            rules.append(one)
        rules.append(data["special"])
        regles = ""
        for rule in rules:
            regles += "• {0}\n".format(rule)

        msg = discord.Embed(
            title = "Règles",
            color= 13752280,
            description = regles)
        msg.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed = msg)

    @commands.command(pass_context=True)
    async def new(self, ctx, *args):
        """Ajoute une nouvelle règle"""
        data = GF.read("game/rules.json")
        new = data["new"]
        nr = ""
        i = 1
        for one in args:
            nr += "{0}".format(one)
            if i < len(args):
                nr += " "
            i += 1
        new.append(nr)
        GF.dump("game/rules.json", data)
        await ctx.channel.send("Règle ajoutée")

    @commands.command(pass_context=True)
    async def supp(self, ctx, *args):
        """Supprime une règles"""
        data = GF.read("game/rules.json")
        new = data["new"]
        n = list()
        nr = ""
        msg = ""
        i = 1
        for one in args:
            nr += "{0}".format(one)
            if i < len(args):
                nr += " "
            i += 1
        for one in new:
            if one == nr:
                msg = "Règle supprimée"
            else:
                n.append(one)
        if msg != "":
            data["new"] = n
        else:
            msg = "Suppréssion impossible"
        GF.dump("game/rules.json", data)
        await ctx.channel.send(msg)

    @commands.command(pass_context=True)
    async def reload(self, ctx, *args):
        """Supprime toutes les nouvelles règles"""
        data = GF.read("game/rules.json")
        data["new"] = []
        GF.dump("game/rules.json", data)
        await ctx.channel.send("Règles réinitialisée")


def setup(bot):
    bot.add_cog(ByPierrot(bot))
    open("help/cogs.txt", "a").write("ByPierrot\n")
