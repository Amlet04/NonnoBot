import botogram
import config
from .updates import commands, process_messages, callbacks

#BotFather per bot_token

bot = botogram.create(config.BOT_TOKEN) 
bot.lang = 'it'
bot.process_backlog = True

@bot.command("start")
def process_start_command(chat, message):
    commands.start.process_command(chat, message)

@bot.callback("open_link")
def process_open_link_callback(message, data, query):
    callbacks.open_link.process_callback(message, data, query)

@bot.callback("home")
def process_home_callback(message, query):
    callbacks.home.process_callback(message, query)

@bot.callback("show_categories")
def process_show_categories_callback(message, query):
    callbacks.show_categories.process_callback(message, query)

@bot.callback("show_predictions")
def process_show_predictions_callback(message, query, data):
    callbacks.show_predictions.process_callback(message, query, data)

@bot.callback("show_prediction")
def process_show_prediction_callback(message, query, data):
    callbacks.show_prediction.process_callback(message, query, data)

#! ADMIN

# Links affiliazione
@bot.command("add_link", hidden=True)
@bot.command("addlink", hidden=True)
@bot.command("addLink", hidden=True)
def process_add_link_command(chat, message):
    if message.sender.id in config.ADMINS:
        commands.admin.add_link.process_command(chat, message)

@bot.command("cancel", hidden=True)
def process_cancel_command(chat, message):
    if message.sender.id in config.ADMINS:
        commands.admin.cancel.process_command(chat, message)

@bot.process_message
def process_message(chat, message):
    if message.sender.id in config.ADMINS:
        process_messages.process_message(chat, message)

@bot.callback("confirm_link")
def process_confirm_link_callback(message, data, query):
    if query.sender.id in config.ADMINS:
        callbacks.admin.confirm_link.process_callback(message, data, query)

# Pronostici
@bot.command('autorizza_utente', hidden=True)
@bot.command('autorizzaUtente', hidden=True)
@bot.command('autorizzautente', hidden=True)
def process_authorize_user_command(chat, message, args, bot):
    if message.sender.id in config.ADMINS:
        commands.admin.authorize_user.process_command(chat, message, args, bot)

@bot.command('togli_autorizzazione', hidden=True)
@bot.command('togliautorizzazione', hidden=True)
@bot.command('togliAutorizzazione', hidden=True)
def process_unauthorize_user_command(chat, message, args, bot):
    if message.sender.id in config.ADMINS:
        commands.admin.unauthorize_user.process_command(chat, message, args, bot)

@bot.callback("create_category")
def process_create_category_callback(message, query):
    callbacks.admin.create_category.process_callback(message, query)

@bot.callback("remove_category")
def process_remove_category_callback(message, query, data):
    callbacks.admin.remove_category.process_callback(message, query, data)

@bot.callback("create_prediction")
def process_create_prediction_callback(message, query):
    callbacks.admin.create_prediction.process_callback(message, query)

@bot.callback("remove_prediction")
def process_remove_prediction_callback(message, query, data):
    callbacks.admin.remove_prediction.process_callback(message, query, data)
