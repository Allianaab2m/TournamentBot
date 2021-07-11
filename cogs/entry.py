from discord import Message
from discord.ext.commands import Bot, Cog, Context, command
from value import value


class Entry(Cog):
    __slots__ = "bot"

    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @command()
    async def entry(self, ctx: Context) -> None:
        value.teams.append(ctx.message.content)
        await ctx.send(f"Entried. Teamname:{ctx.message.content}, Teams:{value.teams}")


def setup(bot: Bot) -> None:
    bot.add_cog(Entry(bot))
