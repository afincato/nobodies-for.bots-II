#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple Bot to reply to Telegram messages.
This is built on the API wrapper, see echobot2.py to see the same example built
on the telegram.ext bot framework.
This program is dedicated to the public domain under the CC0 license.
Code modified for the bot workshop http://todaysart.nl/2018/program/nobodies-for-bots/ .
"""
import random
import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep


update_id = None


def main():
    """Run the bot."""
    global update_id

    # Telegram Bot Authorization Token
    bot = telegram.Bot("token")

    # get the first pending update_id, this is so we can skip over it in case
    # we get an "Unauthorized" exception.
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    print('⚡️ working')

    while True:
        try:
            echo(bot, vocabulary)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1

vocabulary = {
    'ping': ['pong', 'wow', 'pow','boom'],
    'hello': ['hello','hey stranger', 'nice to see you around here'],
    'how was last night?': ['😈🤪😍', 'i watched a movie at the cinema']
}

def echo(bot, vocabulary):
    """Echo the message the user sent."""
    global update_id
    # Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1

        if update.message:  # your bot can receive updates without messages
            # Reply to the message
            # update.message.reply_text(update.message.text)
            print(update.message.text)
            for key, value in vocabulary.items():
                if not update.message.text == None:
                    words = update.message.text.split(' ')
                    if key in words or key in update.message.text:
                        update.message.reply_text(random.choice(value))
                        print('✨ ' + value)

if __name__ == '__main__':
    main()
