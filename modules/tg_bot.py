from telegram.ext import Updater
import telegram.error

from cfg import config


class Bot:
    def __init__(self):
        self.updater = Updater(token=config.BOT_TOKEN,
                               request_kwargs=config.REQUEST_KWARGS,
                               use_context=True)
        self.channels = config.CHANNELS

    def send_msg(self, msg):
        found = False

        for ch_id, apps in self.channels.items():
            for app, levels in apps.items():
                if msg['service'] == app and msg['level'] in levels:
                    self._send(msg, ch_id)
                    found = True
                    break

        if not found:
            self._send(msg, config.GENERAL_CHANNEL_ID)

    def _send(self, msg, channel_id):
        try:
            self.updater.bot.send_message(channel_id, text=Bot._format_msg(msg), timeout=20)
        except telegram.error.TimedOut:
            print('Couldn\'t connect to telegram.')

    @staticmethod
    def _format_msg(msg):
        res = []
        for k, v in msg.items():
            s = '{0}:   {1} \n'.format(k, v)
            res.append(s)

        return '\n'.join(res)

