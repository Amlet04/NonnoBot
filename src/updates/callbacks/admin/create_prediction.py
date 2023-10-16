import botogram, config
from ....objects.user import User
from ....objects.utils import Utils

utils = Utils()

def process_callback(message, query):
    u = User(query.sender)
    u.state("prediction_name")
    category_id = u.path().split("/")[-1]

    text = "<b>Inviami il nome del pronostico da creare: </b>"

    btns = botogram.Buttons()
    btns[0].callback("Back", "show_predictions", category_id)

    message.edit(text, syntax="HTML", attach=btns)
