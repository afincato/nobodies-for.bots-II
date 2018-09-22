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
                 InlineKeyboardButton("Option 4", callback_data='4')],

                [InlineKeyboardButton("Option 5", callback_data='5')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    # update.message.reply_text('description:\nsomething someting choose your tech lalaal:\n1. tech bees\n2. tech peas\n3. tech miso\n4. tech holo\n')
    update.message.reply_text('Please choose:', reply_markup=reply_markup)

descr = [
    "Gravity shifter:\nclicker that permits seasonal shifts of gravitational pull (instead of down, sideways, or slightly off, etc.) known to alter migration of birds, seeds, helps for agricultural diversity and love matches. Pull can cause unforeseen effects other communities' order.",
    "Roving bubble:\nthis vehicle is the ultimate protection bubble that permits any entity to travel within its small parameters - it floats and cannot be penetrated and is completely clear so inside and outside you see through completely, no weapon can destruct it and despite any things that would keep an entity stuck it adapts to serve that need (ie underwater only creatures can travel in this).  other entites are able to see you and you cannot leave the bubble until you are back at your starting point. good for spying, greeting.",
    "Compigestian:\ndigest any waste product as food and/or energy.",
    "Supermaterial:\nincredibly thin nearly invisible material that can be used to cover any sized object or land and make it weightless and transportable for up to 2 hours.",
    "Velocimeter:\nallows the wearer to travel at the fastest speed known in the universe-the wearer can travel through the galaxy to find other tools or species to meet, dominate, befriend, multiply with, etc."
]

def button(bot, update):
    query = update.callback_query

    bot.edit_message_text(text="Selected option: {}\n\n".format(query.data) + descr[int(query.data) -1],
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)


def help(bot, update):
    update.message.reply_text("Use /tech to test this bot.")


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater('token')

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
