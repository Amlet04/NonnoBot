import botogram, config
from ....objects.user import User
from ....objects.utils import Utils

utils = Utils()

def process_callback(message, query, data):
    u = User(query.sender)
    btns = botogram.Buttons()

    if u.state() == "remove_prediction":
        u.state("home")

        prediction = utils.get_prediction(prediction_id=int(data))
        category_id = u.path().split("/")[-1]
        btns[0].callback("Back", "show_predictions", category_id)

        text = (
            "<b>Il pronostico <code>{name}</code> è stato rimosso con successo! ✅</b>"
            .format(
                name = prediction.name
            )
        )
        utils.delete_prediction(int(data))

        message.edit(text, syntax="HTML", attach=btns)

    else:
        u.state("remove_prediction")

        category = utils.get_category(int(data))
        predictions = utils.get_prediction(parent_id=int(data))

        btns = botogram.Buttons()
        
        for prediction in predictions:
            btns[predictions.index(prediction) // 2].callback(
                prediction.name,
                "remove_prediction",
                str(prediction.id)
            )

        text = (
            "<b>Scegli il pronostico da eliminare: </b>\n\n"
        )

        btns[(len(predictions) + 2) // 2].callback("Back", "show_predictions", data)

        message.edit(text, syntax="HTML", attach=btns)
