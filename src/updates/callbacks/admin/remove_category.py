import botogram, config
from ....objects.user import User
from ....objects.utils import Utils

utils = Utils()

def process_callback(message, query, data):
    u = User(query.sender)
    btns = botogram.Buttons()

    if u.state() == "remove_category":
        u.state("home")

        category = utils.get_category(category_id=int(data))
        btns[0].callback("Back", "show_categories")

        text = (
            "<b>La categoria <code>{name}</code> è stata rimossa con successo! ✅</b>"
            .format(
                name = category.name
            )
        )
        utils.delete_category(int(data))

        message.edit(text, syntax="HTML", attach=btns)

    else:
        u.state("remove_category")

        categories = utils.get_category()
        
        for category in categories:
            btns[categories.index(category) // 2].callback(
                category.name,
                "remove_category",
                str(category.id)
            )

        text = (
            "<b>Scegli la categoria da eliminare: </b>\n\n"
            "<i>Tutti i pronostici presenti in quella categoria verranno eliminati</i>"
        )

        btns[(len(categories) + 2) // 2].callback("Back", "show_categories")

        message.edit(text, syntax="HTML", attach=btns)
