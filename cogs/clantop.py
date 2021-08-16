""""
Copyright © Krypton 2021 - https://github.com/kkrypt0nn
Description:
This is a template to create your own discord bot in python.

Version: 2.7
"""
import asyncio
import json
import os
import sys
import httpx

from discord.ext import commands
from tenacity import *

# Only if you want to use variables that are in the config.json file.
if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)


async def ship_list(page):
    async with httpx.AsyncClient() as client:
        params = {"application_id": config["wgdev_id"], "fields": "name", "page_no": page}
        return await client.get("https://api.worldofwarships.com/wows/encyclopedia/ships/", params=params)


@retry(wait=wait_exponential(min=0.5))
async def member_query(member_id, ship_id):
    transport = httpx.AsyncHTTPTransport(retries=10)
    async with httpx.AsyncClient(transport=transport) as client:
        params = {"application_id": config["wgdev_id"], "fields": "pvp.battles, pvp.wins, pvp.damage_dealt, pvp.frags",
                  "account_id": member_id, "ship_id": ship_id}
        response = await client.get("https://api.worldofwarships.com/wows/ships/stats/", params=params)
        print(response.json()["data"])
        return response.json()


# Here we name the cog and create a new class for the cog.

class ClanTop(commands.Cog, name="clantop"):

    def __init__(self, bot):
        self.bot = bot

    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.
    @commands.command(name="clantop", aliases=["ct"])
    async def clantop(self, context):
        # update
        query = "bonks"
        ship_query = "4277090288"

        params = {"application_id": config["wgdev_id"], "search": query, "fields": "clan_id, name, tag"}
        response = httpx.get("https://api.worldofwarships.com/wows/clans/list/", params=params)
        clan_data = response.json()["data"][0]

        params = {"application_id": config["wgdev_id"], "clan_id": clan_data["clan_id"], "fields": "members_ids"}
        response = httpx.get("https://api.worldofwarships.com/wows/clans/info/", params=params)
        members_list = response.json()["data"][str(clan_data["clan_id"])]["members_ids"]
        print(members_list)

        responses = await asyncio.gather(*map(member_query, members_list, [ship_query] * len(members_list)))
        data = [resp["data"] for resp in responses]
        print(data)

    # async def clantop(self, context):
    #     pages = range(1, 7)
    #     resps = await asyncio.gather(*map(ship_list, pages))
    #     data = [resp.json() for resp in resps]
    #     print(data)


# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
def setup(bot):
    bot.add_cog(ClanTop(bot))
