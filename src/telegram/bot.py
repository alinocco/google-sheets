"""
Telegram-bot for notifications about delivery date expiration of an order.
http://t.me/lina_google_sheets_bot
"""


import environ

from notifiers import get_notifier

def notify(message):
    """
    Send notification with message.

    From lina_google_sheets_bot to user with CHAT_ID.
    """
    # Initialise environment variables
    env = environ.Env()
    environ.Env.read_env()

    # Notification
    message = '<pre>' + message + '</pre>'
    telegram = get_notifier('telegram')
    telegram.notify(token=env('TOKEN'), chat_id=env('CHAT_ID'), message=message, parse_mode='html')
