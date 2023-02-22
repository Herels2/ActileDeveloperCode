import disnake

from disnake.ext import commands

bot = commands.Bot(command_prefix="*", intents=disnake.Intents.all())


@bot.slash_command()
async def test(interaction: disnake.AppCmdInter):
    await interaction.send("X3 khcto pisat")

bot.run("MTA3NzkyNjUxNzkyNzA2NzY4OA.GSqEXC.7tdTqsnOAhHgeIaDRGdsx1IWfm0-CMTP-Zxdic")