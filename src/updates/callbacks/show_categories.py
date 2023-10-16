import botogram, config
from ...objects.user import User
from ...objects.utils import Utils

utils = Utils()

def process_callback(message, query):
    u = User(query.sender)
    u.path("/home/categories")

    if not u.is_authorized():
        message.edit(
            "<b>Non sei autorizzato a vedere questo contenuto</b>\nDigita /start per ricominciare.",
            syntax="HTML"
        )
        return

    categories = utils.get_category()
    btns = botogram.Buttons()
    
    for category in categories:
        btns[categories.index(category) // 2].callback(
            category.name,
            "show_predictions",
            str(category.id)
        )
    
    btns[(len(categories) + 2) // 2].callback("Back", "home")
    btns[(len(categories) + 2) // 2].url(
        "☎️ Parla con noi",
        "t.me/{admin_username}".format(
            admin_username = config.ADMIN_USERNAME
        )
    )

    if u.id in config.ADMINS:
        btns[(len(categories) + 4) // 2].callback("➖", "remove_category")
        btns[(len(categories) + 4) // 2].callback("➕", "create_category")
    
    if not categories:
        text = "<b>Non ci sono categorie attive per i pronostici al momento</b>"
    else:
        text = (
            "<b>Seleziona una delle seguenti categorie per vedere i relativi pronostici:</b>"
        )
    
    message.edit(text, syntax="HTML", attach=btns)
    
    
