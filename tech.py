#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Basic example for a bot that uses inline keyboards.

# This program is dedicated to the public domain under the CC0 license.
"""
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def tech(bot, update):
    keyboard = [[InlineKeyboardButton("Option 1", callback_data='1'),
                 InlineKeyboardButton("Option 2", callback_data='2')],

                [InlineKeyboardButton("Option 3", callback_data='3'),
                 InlineKeyboardButton("Option 4", callback_data='4')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    # update.message.reply_text('description:\nsomething someting choose your tech lalaal:\n1. tech bees\n2. tech peas\n3. tech miso\n4. tech holo\n')
    update.message.reply_text('Please choose:', reply_markup=reply_markup)

descr = [
    '1. tech bees 🐝\nthis technology is built upon x-y-z, and can be used for these occasions — etc etc',
    '2. tech peas 🥜\nthis technology is built upon x-y-z, and can be used for these occasions — etc etc',
    '3. tech miso 🍜\nthis technology is built upon x-y-z, and can be used for these occasions — etc etc',
    '4. tech holo 🕳\nthis technology is built upon x-y-z, and can be used for these occasions — etc etc',
]

def button(bot, update):
    query = update.callback_query

    bot.edit_message_text(text="Selected option: {}\n".format(query.data) + descr[int(query.data) -1],
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)


def help(bot, update):
    update.message.reply_text("Use /tech to test this bot.")


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater("TOKEN")

    updater.dispatcher.add_handler(CommandHandler('tech', tech))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    print('⚡️ working')

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
