#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Simple oracle bot for the workshop http://todaysart.nl/2018/program/nobodies-for-bots/ .
This program is dedicated to the public domain under the CC0 license.
"""

import random
from telegram.ext import Updater, CommandHandler
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

prophecy=["It is beyond your control.","Yes.","You may proceed.", "No.", "Try again.","Go ahead.","Follow your intuition.","Trust your fellow with your decision.", "You will suffer, but it will be for the good of your community. Continue.","It is best to ponder again.","Not all that shines is gold. Do not pursue this."]

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def oracle(bot, update):
    update.message.reply_text('You have summoned the great oracle. The answer to your question is: %s'%(random.choice(prophecy)))



def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """Run bot."""
    updater = Updater("TOKEN")
    print('⚡️ working')

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("oracle", oracle))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
