#  Copyright (c) 2020.
#  All rights lies to "VukAnd12#4407" and "Gravity Assist#0852"
import time
import threading
import discord
import pymysql
import crayon

from secrets import token

client: discord.Client = discord.Client()

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='',
                     db='crayon_box')


def keep_db_synced():
    while True:
        crayon.DB.update(client)
        time.sleep(10)


@client.event
async def on_ready():
    print('==========')
    print(client.user.name + '#' + client.user.discriminator)
    print(client.user.id)
    print('https://discordapp.com/oauth2/authorize?client_id=' + str(client.user.id) + '&scope=bot')
    print('==========')

    threading.Thread(target=keep_db_synced).start()


@client.event
async def on_message(message: discord.Message):
    channel_actions: dict = {
        1: crayon.ModuleFunctions.verification
    }

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
                else:
                    action: int = int(crayon.DB.channel_use(channel))
                    if action != 0:
                        channel_actions[action](message, client)

    if content.lower() == 'creeper':
        if channel.id != 561997180638986242:
            await channel.send("this again? Just go to <#561997180638986242>...")


@client.event
async def on_message_edit(old_message: discord.Message, new_message: discord.Message):
    pass


@client.event
async def on_guild_channel_delete(channel):
    pass


@client.event
async def on_member_join(member: discord.Member):
    pass


@client.event
async def on_guild_join(guild: discord.Guild):
    pass


@client.event
async def on_guild_remove(guild: discord.Guild):
    pass


@client.event
async def on_guild_update(old_guild: discord.Guild, new_guild: discord.Guild):
    pass


client.run(token)
