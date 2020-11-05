
# import discord package
import discord
from discord.ext import commands

#Client
client = discord.client()

@client.event
async def on_ready():

    general_channel = client.get_channel(773777135931883570)  #Lähettää bottikomentoihin viestin.

    await general_channel.send('Kelatuki toimii!')
@client.event
async def on_message(message):
     if message.content == 'komento, kirjoita esim. !kelatuki':
        general_channel = client.get_channel(773777135931883570) #kanavan token
        await general_channel.send('viesti minkä se lähettää.')
     if message.content == 'komento, kirjoita esim. !kelatuki':
        general_channel = client.get_channel(773777135931883570) #kanavan token
        await general_channel.send('viesti minkä se lähettää.')

  

# run the client on the server
client.run('tässätoken')
