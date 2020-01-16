import discord


class StaticFunctions:
    @staticmethod
    def has_user_role(member: discord.Member, role: discord.Role):
        return role in member.roles

    @staticmethod
    async def temp_message(content: str, channel: discord.TextChannel, seconds: int):
        message: discord.Message = await channel.send(content)
        await message.delete(delay=seconds)

    @staticmethod
    async def contains_external_invite(content: str, guild: discord.Guild):
        content = content.lower()
        contains_no_external: bool = True
        pos: int

        invites: list = await guild.invites()

        guild_invites: list = []

        for invite in invites:
            guild_invites.append("discord.gg/" + invite.code)
            guild_invites.append("discordapp.com/invite/" + invite.code)

        #while (content.find("discord.gg") is not -1) and contains_no_external:
