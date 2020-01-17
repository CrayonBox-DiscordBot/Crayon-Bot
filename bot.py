#  Copyright (c) 2020.
#  All rights lies to "VukAnd12#4407" and "Gravity Assist#0852"

import discord
import pymysql
import crayon

from secrets import token

client = discord.Client()


db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='',
                     db='crayon')



@client.event
async def on_message(message: discord.Message):
    prefix: str = 'c!'
    channel: discord.TextChannel = message.channel

    content: str = message.content
    guild: discord.Guild = message.guild

    if str(channel.type) != 'private':
        member: discord.Member = message.author
        user: discord.User = await client.fetch_user(member.id)
        if not user.bot:

            with db.cursor() as db_cursor:  # SQL Pointer
                db_cursor.execute('SELECT get_server_prefix({id}) AS prefix;'.format(id=str(guild.id)))
                for value in db_cursor:
                    prefix = value[0]

            if content.lower().startswith(prefix):
                args: list = content[len(prefix):].split(' ')
                command: str = args[0].lower()

                action: int = 0
                with db.cursor() as db_cursor:  # SQL Pointer
                    db_cursor.execute(
                        "SELECT get_server_command_action({id}, '{command}') AS action;".format(id=str(guild.id),
                                                                                                command=command))
                    for value in db_cursor:
                        action = int(value[0])

                # await crayon.StaticFunctions.contains_external_invite(content, guild)
                print(action)

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
