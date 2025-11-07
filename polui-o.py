import discord
from discord.ext import commands
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
#a = input('qual veículo você vai utilizar?')
#km = input('quantos quilômetros serão rodados')
#veiculodict= {'carro':120 , 'moto':50}
#if a == 'carro':
#   return 120 * b
#elif a == 'moto':
#  50 * b
@bot.command()
async def pokemon(ctx, ):
    await ctx.send(f'{pokemon_image}')
    view = discord.ui.View()
    botao = discord.ui.Button(label='capturar', style=discord.ButtonStyle.green)
    botao.callback = resposta_botao
    botao2 = discord.ui.Button(label='fugir', style=discord.ButtonStyle.green)
    botao2.callback = resposta_botao2

    view.add_item(botao2)
    view.add_item(botao)
    await ctx.reply(view=view)

bot.run('TOLKEN')
