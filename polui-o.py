import discord
from discord.ext import commands
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
"""
a = input('qual veículo você vai utilizar?')
km = input('quantos quilômetros serão rodados')
veiculodict= {'carro':120 , 'moto':50}"""

@bot.command()
async def explic(ctx):
    await ctx.send('use o comando $carbono e passe o veículo e a quilometragem')
    
@bot.command()
async def carbono(ctx, a, km):
    c = 0
    km = int(km)
    
    if a == 'carro':
        c = 120 * km
    elif a == 'moto':
        c = 50 * km
    elif a == 'ônibus':
        c = 1460 * km
    elif a == 'avião':
        c = 110 * km
    elif a == 'barco_pequeno':
        c = 300 * km
    elif a == 'barco_cruzeiro':
        c = 700 * km
    
    await ctx.send(str(c) + ' gramas de carbono seriam liberadas na astmosfera.')

bot.run('tolken')

