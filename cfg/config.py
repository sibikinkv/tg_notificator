
DATABASE_CONNECTION = ''

GENERAL_CHANNEL_ID = ''  # channnel for non-personal notifications

BOT_TOKEN = ''  # Your bot token

REQUEST_KWARGS = {
    'proxy_url': 'socks5://stats-tg.ru:7777',
    # Optional, if you need authentication:
    'urllib3_proxy_kwargs': {
        'username': '',
        'password': '',
    }
}

CHANNELS = {
    # My notifications
    '-1001167122843': {
        'log_scanner': ('WARNING', 'ERROR'),
        'zcm_log_analyser': ('WARNING', 'ERROR')
    }
    # Other channels with app names and levels
}
