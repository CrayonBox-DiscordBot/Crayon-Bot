#  Copyright (c) 2020.
#  All rights lies to "VukAnd12#4407" and "Gravity Assist#0852"

import discord


class StaticFunctions:
    @staticmethod
    async def temp_message(content: str, channel: discord.TextChannel, seconds: int):
        message: discord.Message = await channel.send(content)
        await message.delete(delay=seconds)

    @staticmethod
    async def contains_external_invite(content: str, guild: discord.Guild) -> bool:
        """
        Check if message contains invite to guild which is not the message.guild
        :param content:
        Message content
        :param guild:
        Message guild
        :return bool:
        Contains no invite to different guild
        """
        content = content.lower()

        contains_no_external: bool = True
        pos: int
        message_invite: str

        invites: list = await guild.invites()

        guild_invites: list = []

        invite_types: list = [
            "discord.gg/",
            "discordapp.com/invite/"
        ]

        for invite in invites:
            for invite_type in invite_types:
                guild_invites.append(invite_type + invite.code)

        for invite_type in invite_types:
            search_text: str = content
            while (content.find(invite_type) != -1) and contains_no_external:
                pos = search_text.find(invite_type)

                if search_text[pos:].find(" ") == -1:
                    message_invite = search_text[pos:]
                else:
                    message_invite = search_text[pos:search_text[pos:].find(" ")]
                if message_invite not in guild_invites:
                    contains_no_external = False
                search_text = search_text[pos + len(message_invite):]

        return contains_no_external
