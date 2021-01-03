# -*- coding: utf-8 -*-

import sqlite3
import irc3
from irc3.plugins.command import command


@irc3.plugin
class Plugin:

    def __init__(self, bot):
        self.bot = bot
        self.bot.log.info('BotForceOne plugin loaded')

    @irc3.event(irc3.rfc.JOIN)
    def say_hi(self, mask, channel, **kw):
        """Say hi when someone join a channel"""
        if mask.nick != self.bot.nick:
            # FIXME: look up the correct quote - castlevania?
            self.bot.privmsg(channel, f'What a terrible night to have a curse {mask.nick}!')

    @command(permission='view')
    def ping(self, mask, target, args):
        """pong a ping

            %%ping
        """
        self.bot.privmsg(target=target, message=f'{mask.nick}: pong')

    @command(permission='view')
    def peng(self, mask, target, args):
        """peng a peng

            %%peng
        """
        yield 'peng'

    def connection_made(self):
        """triggered when connection is up"""

    def server_ready(self):
        """triggered after the server sent the MOTD (require core plugin)"""

    def connection_lost(self):
        """triggered when connection is lost"""

    @command(permission='view')
    def echo(self, mask, target, args):
        """Echo

            %%echo <message>...
        """
        yield ' '.join(args['<message>'])
