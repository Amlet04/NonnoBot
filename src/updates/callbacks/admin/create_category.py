import botogram, config
from ....objects.user import User
from ....objects.utils import Utils

utils = Utils()

def process_callback(message, query):
    u = User(query.sender)
    u.state("category_name")

    text = "<b>Inviami il nome della categoria da creare: </b>"

    btns = botogram.Buttons()
    btns[0].callback("Back", "show_categories")

    message.edit(text, syntax="HTML", attach=btns)
