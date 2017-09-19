#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Padbot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Job
import logging
import random

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(bot, update):
    update.message.reply_text('Hi!')

def help(bot, update):
    update.message.reply_text('Help!')

def reply(bot, update):
    if random.random() > 0.10:
        return

    name = "{} {}".format(update.message.from_user.first_name if update.message.from_user.first_name else "",
                          update.message.from_user.last_name if update.message.from_user.last_name else "")
    name = name.lower()
    message = update.message.text
    resp = list()

    # By Message
    if "plaquinha" in message:
        update.message.reply_text("Alguem disse plaquinha?")
        return
    if "http" in message:
        resp = ["Mas que lixo", "muitooooo booom"]
        update.message.reply_text(random.choice(resp))
        return
    if "almoço" in message:
        update.message.reply_text("Villani?")
        return
    if "projeto" in message:
        update.message.reply_text("Ta pronto?")
        return
    if "parabens" in message or "parabéns" in message:
        update.message.reply_text("Parabéns @raoniff!")
        return

    # By Name
    if "raoni" in name:
        resp = ["Rrrrrrrraoniii", "Raonildo", "Parabéns raoni!"]
    if "luiz" in name:
        resp = ["Luizerararara", "DEU..... zig zeira", "Zigzerarara"]
    if "max" in name:
        resp = ["Well well well", "Well well well maxwell", "Tudo well?"]
    if "trevizan" in name:
        resp = ["Trrrrrrrrrevizan", "Trevizolis", "Trevizão", "Não gosto de você..."]
    if "pagano" in name:
        resp = ["Paganera", "Ta pagano ou ta deveno?", "Tom Cruise? O.O"]
    if "atila" in name or "átila" in name:
        resp = ["Run forest, runnnn"]
    if "gabriel" in name or "átila" in name:
        resp = ["Gayyybriel"]
    if "gustavo" in name or "gustavo" in message:
        if random.choice([1,2]) == 1:
            update.message.reply_text("druuuuuuuuu")
        else:
            update.message.reply_voice(voice="AwADAQADCAADxtJQRXAxs64dn1RzAg")
    if "leandro" in name:
        resp = ["Leandroviski", "Drrrrrrrroviski", "!", "lixo", "Isso ai é bucha"]
    if "fabrício" in name:
        resp = ["Poloniiii"]
    if "curvello" in name:
        resp = ["Teacherrr", "Plaquinha?"]
    if "felix" in name:
        resp = ["Tem que ver isso ai...", "Vinicius Felix bateu seu record"]

    # Reply to message
    update.message.reply_text(random.choice(resp))


# Command timeout
def timeout_message(bot, job):
    bot.send_message(chat_id=job.context, text='Timeout, partindo.')

def timeout(bot, update, job_queue, args):
    if len(args) != 2:
        update.message.reply_text("Sintaxe errada! /timeout 1 min ou /timeout 30 seg")
        return

    try:
        float(args[0])
    except ValueError:
        update.message.reply_text("Tempo inválido")
        return

    if args[1] not in ["min", "seg"]:
        update.message.reply_text("Unidade de tempo inválida. Unidades validas: min, seg")
        return

    time = float(args[0])
    if "min" in args:
        time = time * 60

    bot.send_message(chat_id=update.message.chat_id,
                     text='Timeout em {} {}!'.format(time if args[1] == "seg" else time/60, args[1]))
    job_alarm = Job(timeout_message,
                    time,
                    repeat=False,
                    context=update.message.chat_id)
    job_queue.put(job_alarm)

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("BOT_TOKEN")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("timeout", timeout, pass_job_queue=True, pass_args=True))
    dp.add_handler(MessageHandler(Filters.text, reply))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
