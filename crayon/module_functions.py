#  Copyright (c) 2020.
#  All rights lies to "VukAnd12#4407" and "Gravity Assist#0852"

import discord
import crayon


class ModuleFunctions:
    @staticmethod
    async def verification(message: discord.Message, client: discord.Client):
        user: discord.User = message.author
        content: str = message.content
        guild: discord.Guild = message.guild
        channel: discord.TextChannel = message.channel
