#  Copyright (c) 2020.
#  All rights lies to "VukAnd12#4407" and "Gravity Assist#0852"
import time

import discord
import pymysql
import crayon

from secrets import token

client = discord.Client()

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='',
                     db='crayon_box')


@client.event
async def on_ready():
    print('==========')
    print(client.user.name + '#' + client.user.discriminator)
    print(client.user.id)
    print('https://discordapp.com/oauth2/authorize?client_id=' + str(client.user.id) + '&scope=bot')
    print('==========')

    """while True:
        crayon.DB.update(client)
        time.sleep(10)"""


@client.event
async def on_message(message: discord.Message):
    prefix: str = 'c!'
    channel: discord.TextChannel = message.channel

    content: str = message.content
    guild: discord.Guild = message.guild


    if str(channel.type) != 'private':
        member: discord.Member = message.author
        user: discord.User = await client.fetch_user(member.id)

        crayon.DB.check_server_register(guild)
        crayon.DB.check_channel_register(channel)

        if not user.bot:
            prefix = crayon.DB.get_server_prefix(guild)

            result = crayon.DB.is_special_channel_user(channel, user)

            # await crayon.ModuleFunctions.verification(message, client)

            if result == "ignore":
                pass
            elif str(result) == "forbidden":
                await message.delete()
            else:
                if int(crayon.DB.channel_use(channel)) == 0:
                    await crayon.ModuleFunctions.verification(message, client)

                if content.lower().startswith(prefix):
                    args: list = content[len(prefix):].split(' ')
                    command: str = args[0].lower()
                    action: int = 0
                    # await crayon.StaticFunctions.contains_external_invite(content, guild)

    if content.lower() == 'creeper':
        if channel.id != 561997180638986242:
            await channel.send("this again? Just go to <#561997180638986242>...")


@client.event
async def on_message_edit(oldMessage, newMessage):
    pass


@client.event
async def on_guild_channel_delete(channel):
    # db update
    pass


@client.event
async def on_member_join(member):
    pass


@client.event
async def on_guild_join(guild):
    pass


@client.event
async def on_guild_remove(guild):
    # no db update so if he connects again all configs will stay
    pass


@client.event
async def on_guild_update(oldGuild, newGuild):
    pass


client.run(token)
