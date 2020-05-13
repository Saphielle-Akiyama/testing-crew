"""
MIT License

Copyright (c) 2020 - Sudosnok, AbstractUmbra, Saphielle-Akiyama

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from typing import Union, Optional

from discord import Member, Object
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

        self.DEF_DAYS = 7
        self.DEF_REASON = "No reason given"

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, ctx: commands.Context, target: Union[Member, Object], days: Optional[int], *, reason: Optional[str]) -> None:
        """Bans the given <target> for [reason], deleting [days] of messages"""  # that good?
        days = days or self.DEF_DAYS
        reason = reason or self.DEF_REASON
        await ctx.guild.ban(target, delete_message_days=days, reason=reason)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def kick(self, ctx: commands.Context, target: Member, *, reason: Optional[str]) -> None:
        """Kicks the given target for a reason"""
        reason = reason or self.DEF_REASON
        await target.kick(reason=reason)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def unban(self, ctx: commands.Context, target: int, *, reason: Optional[str]) -> None:
        """Unbans the given target"""
        reason = reason or self.DEF_REASON
        await ctx.guild.unban(Object(id=target), reason=reason)

    @commands.command()
    @commands.has_guild_permissions(mute_members=True)
    @commands.bot_has_guild_permissions(mute_members=True)
    async def mute(self, ctx: commands.Context, target: Member, *, reason: Optional[str]) -> None:
        """Mutes the given target with a reason"""
        reason = reason or self.DEF_REASON
        await target.edit(mute=True, reason=reason)

    @commands.command()
    @commands.has_guild_permissions(mute_members=True)
    @commands.bot_has_guild_permissions(mute_members=True)
    async def unmute(self, ctx: commands.Context, target: Member, *, reason: Optional[str]) -> None:
        reason = reason or self.DEF_REASON
        await target.edit(mute=False, reason=reason)


def setup(bot):
    """ Cog entrypoint. """
    bot.add_cog(Moderation(bot))
