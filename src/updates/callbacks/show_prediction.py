import botogram, config
from ...objects.user import User
from ...objects.utils import Utils

utils = Utils()

def process_callback(message, query, data):
    u = User(query.sender)

    if not u.is_authorized():
        message.edit(
            "<b>Non sei autorizzato a vedere questo contenuto</b>\nDigita /start per ricominciare.",
            syntax="HTML"
        )
        return
    
    category_id = u.path().split("/")[-1]
    u.path(u.path() + f"/{data}")

    predictions = utils.get_prediction(parent_id=int(data))

    btns = botogram.Buttons()
    
    btns[0].callback("Back", "show_predictions", category_id)
    btns[0].url(
        "☎️ Parla con noi",
        "t.me/{admin_username}".format(
            admin_username = config.ADMIN_USERNAME
        )
    )

    text = (
        "{description}"
        .format(
            description = utils.get_prediction(prediction_id=int(data)).description
        )
    )
    
    message.edit(text, syntax="HTML", attach=btns)
