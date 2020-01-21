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
        member: discord.Member = guild.get_member(user.id)
        channel: discord.TextChannel = message.channel

        if crayon.DB.is_special_channel_user(channel, user) != "ignore":
            verification_log_channel_id: int = crayon.DB.get_verification_log_channel(guild)
            if verification_log_channel_id != 0:
                verification_log_channel: discord.TextChannel = await client.fetch_channel(
                    verification_log_channel_id)
            if int(crayon.DB.is_verification_phrase_correct(channel, content)) == 1:
                verification_roles: dict = crayon.DB.verification_roles(channel)

                for role_id in verification_roles["add"]:
                    await member.add_roles(guild.get_role(role_id),
                                           reason="Verified role added (success verification)")

                for role_id in verification_roles["remove"]:
                    await member.remove_roles(guild.get_role(role_id),
                                              reason="Unverified role removed (success verification)")

                verification_log_channel_id: int = crayon.DB.get_verification_log_channel(guild)
                if verification_log_channel_id != 0:
                    verification_log_channel: discord.TextChannel = await client.fetch_channel(
                        verification_log_channel_id)
                    await verification_log_channel.send(
                        "[cba verification] <@!{userid}> has verified ✨✨".format(userid=user.id))
            else:
                await (await channel.send(embed=crayon.StaticEmbeds.wrong_verify_message(user, guild))).delete(delay=7)
                if verification_log_channel_id != 0:
                    verification_log_channel: discord.TextChannel = await client.fetch_channel(
                        verification_log_channel_id)
                    await verification_log_channel.send(
                        "[cba verification] <@!{userid}> failed, they sent:\n{content}".format(userid=user.id,
                                                                                               content=content))
