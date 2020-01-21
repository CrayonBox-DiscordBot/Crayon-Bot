#  Copyright (c) 2020.
#  All rights lies to "VukAnd12#4407" and "Gravity Assist#0852"
import pymysql
import discord

import crayon


class __Database:
    def __init__(self):
        self.__db = pymysql.connect(host='localhost',
                                    port=3306,
                                    user='root',
                                    password='',
                                    db='crayon_box')

    @staticmethod
    def update(client: discord.Client):
        changes: bool = False

        servers: list = client.guilds
        server_ids: list = []
        collected_servers: list = crayon.DB.execute_query("SELECT serverID FROM server;")
        collected_server_ids: list = []

        for entry in collected_servers:
            collected_server_ids.append(int(entry[0]))

        for server in servers:
            server_ids.append(server.id)
            if server.id not in collected_server_ids:
                changes = True
                crayon.DB.check_server_register(server)

        for entry in collected_server_ids:
            if entry not in server_ids:
                changes = True
                crayon.DB.execute_query(
                    "DELETE FROM server WHERE serverID = {serverid};".format(serverid=entry))

        channels = client.get_all_channels()
        channel_ids = []
        collected_channels: list = crayon.DB.execute_query("SELECT channelID FROM channel;")

        collected_channel_ids: list = []
        for entry in collected_channels:
            collected_channel_ids.append(int(entry[0]))

        for channel in channels:
            channel_ids.append(channel.id)
            if channel.id not in collected_channel_ids:
                changes = True
                crayon.DB.check_channel_register(channel)

        for entry in collected_channel_ids:
            if entry not in channel_ids:
                changes = True
                crayon.DB.execute_query(
                    "DELETE FROM channel WHERE channelID = {channelid};".format(channelid=entry))

        if changes:
            print("Database synced")

    def execute_query(self, query: str) -> tuple:
        cursor = self.__db.cursor()
        cursor.execute(query)
        self.__db.commit()
        rows = cursor.fetchall()
        cursor.close()
        self.__db.commit()
        return rows

    def check_server_register(self, server: discord.Guild):
        cursor = self.__db.cursor()
        cursor.execute("SELECT COUNT(serverID) FROM server WHERE serverID = {serverid};".format(serverid=server.id))
        self.__db.commit()
        rows = cursor.fetchall()

        if int(rows[0][0]) == 0:
            cursor.execute("INSERT INTO server (serverID) VALUES ({serverid});".format(serverid=server.id))
        cursor.close()
        self.__db.commit()

    def check_channel_register(self, channel: discord.TextChannel):
        cursor = self.__db.cursor()
        cursor.execute("SELECT COUNT(channelID) FROM channel WHERE channelID = {channelid};".format(
            channelid=channel.id))

        self.__db.commit()
        rows = cursor.fetchall()

        if int(rows[0][0]) == 0:
            cursor.execute("INSERT INTO channel (channelID, server_ID) VALUES ({channelid}, {serverid});".format(
                channelid=channel.id, serverid=channel.guild.id))
        cursor.close()
        self.__db.commit()

    def get_server_prefix(self, server: discord.Guild):
        cursor = self.__db.cursor()
        cursor.execute("SELECT prefix FROM server WHERE serverID = {serverid};".format(serverid=server.id))
        self.__db.commit()
        rows = cursor.fetchall()
        cursor.close()
        self.__db.commit()
        return rows[0][0]

    def is_special_channel_user(self, channel: discord.TextChannel, user: discord.User):
        cursor = self.__db.cursor()
        cursor.execute(
            "SELECT special_type FROM channel_special_users WHERE channel_ID = {channelid} AND user_ID = {userid};".format(
                channelid=channel.id, userid=user.id))
        self.__db.commit()
        rows = cursor.fetchall()
        cursor.close()
        self.__db.commit()
        if len(rows) == 0:
            return ""
        else:
            return rows[0][0]

    def is_verification_phrase_correct(self, channel: discord.TextChannel, content: str):
        cursor = self.__db.cursor()
        cursor.execute(
            "SELECT COUNT(channel_ID) FROM channel_verification WHERE channel_ID = {channelid} AND phrase_ID = (SELECT phraseID FROM phrase WHERE phrase = '{phrase}');".format(
                channelid=channel.id, phrase=content))
        self.__db.commit()
        rows = cursor.fetchall()
        cursor.close()
        self.__db.commit()
        return rows[0][0]

    def verification_roles(self, channel: discord.TextChannel):
        cursor = self.__db.cursor()
        cursor.execute("SELECT role_action, role_ID FROM channel_verification WHERE channel_ID = {channelid};".format(
            channelid=channel.id))
        self.__db.commit()
        rows = cursor.fetchall()
        cursor.close()
        self.__db.commit()

        roles = {"add": [], "remove": []}
        for entry in rows:
            roles[entry[0]].append(entry[1])

        return roles

    def get_verification_log_channel(self, server: discord.Guild):
        cursor = self.__db.cursor()
        cursor.execute("SELECT verification_log_channel_ID FROM server_log WHERE server_ID = {serverid};".format(
            serverid=server.id))
        self.__db.commit()
        rows = cursor.fetchall()
        cursor.close()
        self.__db.commit()

        if len(rows) == 0:
            return 0
        else:
            return rows[0][0]

    def channel_use(self, channel: discord.TextChannel):
        cursor = self.__db.cursor()

        cursor.execute("SELECT used FROM channel WHERE channelID = {channelid};".format(channelid=channel.id))
        self.__db.commit()
        rows = cursor.fetchall()
        cursor.close()
        self.__db.commit()
        return rows[0][0]
