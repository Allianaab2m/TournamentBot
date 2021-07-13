import random

from discord import Message
from discord.ext.commands import Bot, Cog, Context, command

from value import value


class Match(Cog):
    __slots__ = "bot"

    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @command()
    async def match(self, ctx: Context) -> None:
        for team in value.teams:
            unmatched = value.teams
            versus = random.sample(unmatched)
            value.match_list.append(versus)
            unmatched.remove(versus)


def setup(bot: Bot) -> None:
    bot.add_cog(Match(bot))
