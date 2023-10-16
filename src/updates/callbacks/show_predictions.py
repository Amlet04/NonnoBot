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
    
    u.path(f"/home/categories/{data}")

    category = utils.get_category(int(data))
    predictions = utils.get_prediction(parent_id=int(data))

    btns = botogram.Buttons()
    
    for prediction in predictions:
        btns[predictions.index(prediction) // 2].callback(
            prediction.name,
            "show_prediction",
            str(prediction.id)
        )
    
    btns[(len(predictions) + 2) // 2].callback("Back", "show_categories")
    btns[(len(predictions) + 2) // 2].url(
        "☎️ Parla con noi",
        "t.me/{admin_username}".format(
            admin_username = config.ADMIN_USERNAME
        )
    )

    if u.id in config.ADMINS:
        btns[(len(predictions) + 4) // 2].callback("➖", "remove_prediction", data)
        btns[(len(predictions) + 4) // 2].callback("➕", "create_prediction")
    
    if not predictions:
        text = "<b>Non ci sono pronostici attivi al momento</b>"
    else:
        text = (
            "{description}"
            .format(
                description = category.description if category.description else f"<b>Ecco i pronostici relativi alla categoria: {category.name}</b>",
            )
        )
    
    message.edit(text, syntax="HTML", attach=btns)
