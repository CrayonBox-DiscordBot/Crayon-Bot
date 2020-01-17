#  Copyright (c) 2020.
#  All rights lies to "VukAnd12#4407" and "Gravity Assist#0852"

import discord
import datetime


class StaticEmbeds:
    __trial_mod_color: str = "#C8D5EE"
    __wrong_verify_color: str = "#FF0000"
    __not_allowed_character_color: str = "#FF0000"
    __no_discord_invite_color: str = "#FF0000"
    __welcome_message_color: str = "#00FF00"
    __vote_color: str = "#0000FF"

    __feature_colors = {
        "Requested": "#707070",
        "Accepted": "#00FFBB",
        "Rejected": "#B30000",
        "Closed": "#44FF00"

    }

    __giveaway_drop_colors = {
        "dropped": "#D0A33E",
        "claimed": "#D000BC",
        "closed": "#8EA5D0"
    }

    @staticmethod
    def trial_mod_accept(mod: discord.User, new_trial_mod: discord.User, guild: discord.Guild) -> discord.Embed:
        """

        :param mod:
        :param new_trial_mod:
        :param guild:
        :return:
        """
        embed: discord.Embed = discord.Embed(
            title="Hi, your mod application in {guild_name} has been accepted".format(
                guild_name=guild.name
            )
        )
        embed.colour = StaticEmbeds.__trial_mod_color
        embed.set_author(
            name=mod.name,
            icon_url=mod.avatar_url
        )
        embed.timestamp = datetime.datetime.timestamp(datetime.datetime.now())
        embed.set_footer(
            text="For {trial_name}, made by Gravity Assist#0852".format(
                trial_name=new_trial_mod.name
            )
        )

        return embed

    @staticmethod
    def trial_mod_info(trial_mod: discord.User) -> discord.Embed:
        """

        :param trial_mod:
        :return:
        """
        embed: discord.Embed = discord.Embed(
            title="{trial_mod_name} has beed givem Trial Mod!".format(
                trial_mod_name=trial_mod.name
            )
        )
        embed.colour = StaticEmbeds.__trial_mod_color
        embed.timestamp = datetime.datetime.timestamp(datetime.datetime.now())
        embed.set_footer(text="Made by Gravity Assist#0852")

        return embed

    @staticmethod
    def wrong_verify_message(user: discord.User, guild: discord.Guild) -> discord.Embed:
        """

        :param guild:
        :param user:
        :return:
        """
        embed: discord.Embed = discord.Embed(
            title="You do not have permission to access to the *{guild_name}* server".format(
                guild_name=guild.name
            ),
            description="That's the wrong password. Please try again."
        )
        embed.colour = StaticEmbeds.__wrong_verify_color
        embed.set_author(
            name="Verification System",
            icon_url="https://b.thumbs.redditmedia.com/OIDktcKCqI8n4CnTj2SNZAQtXjBWxo9Qah6ku96YsME.png"
        )
        embed.timestamp = datetime.datetime.timestamp(datetime.datetime.now())
        embed.set_footer(
            text="For {user_name}, made by Gravity Assist#0852".format(
                user_name=user.name
            )
        )
        embed.set_image(
            url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/160/facebook/11/cross-mark_274c.png")

        return embed

    @staticmethod
    def not_allowed_character(user: discord.User, character: str) -> discord.Embed:
        """

        :param user:
        :param character:
        :return:
        """
        embed: discord.Embed = discord.Embed(
            title="Really funny",
            description="{character} is not allowed here, for obvious reasons.".format(
                character=character)
        )
        embed.colour = StaticEmbeds.__not_allowed_character_color
        embed.set_image(
            url="https://media.tenor.com/images/002ad9767dabb97d0dfcc0300ad95da7/tenor.gif"
        )
        embed.timestamp = datetime.datetime.timestamp(datetime.datetime.now())
        embed.set_footer(
            text="For {user_name}, made by Gravity Assist#0853".format(
                user_name=user.name
            )
        )

        return embed

    @staticmethod
    def no_discord_invite(user: discord.User) -> discord.Embed:
        """

        :param user:
        :return:
        """
        embed: discord.Embed = discord.Embed(
            title='Rule: No invites to other Discord Servers',
            description="Per Rules, its not allowed to send invites to other Discord Servers"
        )
        embed.colour = StaticEmbeds.__no_discord_invite_color
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/649636894807949352/667656108659179520/animated_discord_logo.gif"
        )
        embed.timestamp = datetime.datetime.timestamp(datetime.datetime.now())
        embed.set_footer(
            text="For {user_name}, made by Gravity Assist#0853".format(
                user_name=user.name
            )
        )

        return embed

    @staticmethod
    def welcome_message() -> discord.Embed:
        """

        :return:
        """
        embed: discord.Embed = discord.Embed(
            title="Welcome to the Server!",
            description="Please read the rules and thanks for joining!"
        )
        embed.colour = StaticEmbeds.__welcome_message_color
        embed.set_author(
            name="Join Message",
            icon_url="https://b.thumbs.redditmedia.com/OIDktcKCqI8n4CnTj2SNZAQtXjBWxo9Qah6ku96YsME.png"
        )
        embed.timestamp = datetime.datetime.timestamp(datetime.datetime.now())
        embed.set_footer(text="Made by Gravity Assist#0853")

        return embed

    @staticmethod
    def feature_request(requester: discord.User, feature: str, feature_id: int, request_id: int, channel_id: int,
                        status: str) -> discord.Embed:
        """

        :param requester:
        :param feature:
        :param feature_id:
        :param request_id:
        :param channel_id:
        :param status:
        :return:
        """
        embed: discord.Embed = discord.Embed(title="Feature {status}".format(status=status))
        embed.colour = StaticEmbeds.__feature_colors[status]
        embed.set_author(
            name=str(requester.name + "#" + requester.discriminator),
            icon_url=requester.avatar_url
        )
        embed.timestamp = datetime.datetime.timestamp(datetime.datetime.now())
        embed.set_footer(text="Made by Gravity Assist#0853")

        embed.add_field(name="Requested Feature", value=feature, inline=False)
        embed.add_field(name="Feature ID", value=str(feature_id), inline=False)
        embed.add_field(name="Request ID", value=str(request_id), inline=False)
        embed.add_field(name="Request channel ID", value=str(channel_id), inline=False)
        embed.add_field(name="Requester ID", value=requester.id, inline=False)

        return embed

    @staticmethod
    def feature_request_response(requester: discord.User, feature: str, feature_id: int, developer: discord.User,
                                 status: str) -> discord.Embed:
        """

        :param requester:
        :param feature:
        :param feature_id:
        :param developer:
        :param status:
        :return:
        """
        embed: discord.Embed = discord.Embed(title="Feature {status}".format(status=status))
        embed.colour = StaticEmbeds.__feature_colors[status]
        embed.set_author(
            name=str(requester.name + "#" + requester.discriminator),
            icon_url=requester.avatar_url
        )
        embed.timestamp = datetime.datetime.timestamp(datetime.datetime.now())
        embed.set_footer(text="Made by Gravity Assist#0853")

        embed.add_field(name="Requested Feature", value=feature, inline=False)
        embed.add_field(name="Feature ID", value=str(feature_id), inline=False)
        embed.add_field(name="{status} by", value=str(developer.name + "#" + developer.discriminator), inline=False)

        return embed

    @staticmethod
    def giveaway_drop(prize: str, dropped_by: discord.User) -> discord.Embed:
        """


        :param prize:
        :param dropped_by:
        :return:
        """
        embed: discord.Embed = discord.Embed(title="Giveaway Dropped")
        embed.colour = StaticEmbeds.__giveaway_drop_colors["dropped"]
        embed.set_author(
            name=str(dropped_by.name + "#" + dropped_by.discriminator),
            icon_url=dropped_by.avatar_url
        )
        embed.timestamp = datetime.datetime.timestamp(datetime.datetime.now())
        embed.set_footer(text="Made by Gravity Assist#0853")

        embed.add_field(name="Prize", value=prize, inline=False)
        embed.add_field(name="Winner", value="I haven't noticed a winner yet.", inline=False)
        embed.add_field(
            name="How to win!",
            value="Be the first who reacts with <a:dropreact:665990890438918174>",
            inline=False
        )

        return embed

    @staticmethod
    def giveaway_drop_winner(prize: str, dropped_by: discord.User, winner: discord.User) -> discord.Embed:
        """

        :param prize:
        :param dropped_by:
        :param winner:
        :return:
        """
        embed: discord.Embed = discord.Embed(title="Giveaway Claimed")
        embed.colour = StaticEmbeds.__giveaway_drop_colors["claimed"]
        embed.set_author(
            name=str(dropped_by.name + "#" + dropped_by.discriminator),
            icon_url=dropped_by.avatar_url
        )
        embed.timestamp = datetime.datetime.timestamp(datetime.datetime.now())
        embed.set_footer(text="Made by Gravity Assist#0853")

        embed.add_field(name="Prize", value=prize, inline=False)
        embed.add_field(name="Winner", value="<@!{winner_id}>".format(winner_id=winner.id), inline=False)
        embed.add_field(
            name="How to win!",
            value="Be the first who reacts with <a:dropreact:665990890438918174>",
            inline=False
        )

        return embed

    @staticmethod
    def giveaway_drop_invalid(prize: str, dropped_by: discord.User) -> discord.Embed:
        """

        :param prize:
        :param dropped_by:
        :return:
        """
        embed: discord.Embed = discord.Embed(title="Giveaway Expired")
        embed.colour = StaticEmbeds.__giveaway_drop_colors["closed"]
        embed.set_author(
            name=str(dropped_by.name + "#" + dropped_by.discriminator),
            icon_url=dropped_by.avatar_url
        )
        embed.timestamp = datetime.datetime.timestamp(datetime.datetime.now())
        embed.set_footer(text="Made by Gravity Assist#0853")

        embed.add_field(name="Prize", value=prize, inline=False)
        embed.add_field(name="Winner", value="The prize is no longer valid.", inline=False)
        embed.add_field(
            name="How to win!",
            value="Be the first who reacts with <a:dropreact:665990890438918174>",
            inline=False
        )

        return embed

    @staticmethod
    def vote(creator: discord.User, vote_question: str) -> discord.Embed:
        """

        :param creator:
        :param vote_question:
        :return:
        """
        embed: discord.Embed = discord.Embed(title="Vote")
        embed.colour = StaticEmbeds.__vote_color
        embed.set_author(name=str(creator.name + "#" + creator.discriminator), icon_url=creator.avatar_url)
        embed.timestamp = datetime.datetime.timestamp(datetime.datetime.now())
        embed.set_footer(text="Made by Gravity Assist#0853")

        embed.add_field(name="Question", value=vote_question, inline=False)

        return embed
