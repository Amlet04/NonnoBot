from ..objects.user import User
from ..objects.utils import Utils
import botogram, config

utils = Utils()

def process_message(chat, message):
    u = User(message.sender)

    if u.state() == "add_link":
        u.state("add_description")
        u.create_affiliazione(message.text)

        text = (
            "<b>Ora inviami la descrizione del servizio/sito. Puoi usare la formattazione HTML se desideri personalizzare il testo</b>"
        )
        chat.send(text, syntax="HTML")

    elif u.state() == "add_description":
        u.state("add_service_name")
        text = (
            "<b>Adesso inviami il nome del servizio/sito.</b>\n\n"
            "<i>Questo messaggio verrà usato come label del Button nella schermata Home.</i>"
        )

        u.set_affiliazione({
            "description" : message.text
        })

        chat.send(text, syntax="HTML")

    elif u.state() == "add_service_name":
        u.state("add_image")

        u.set_affiliazione({
            "service_name" : message.text
        })

        text = (
            "<b>Inviami l'immagine della promozione.</b>\n"
        )
        chat.send(text, syntax="HTML")

    elif u.state() == "add_image":

        if not message.photo:
            text = (
                "<i>Il messaggio ricevuto non è una foto, riprova.</i>"
            )
            chat.send(text, syntax="HTML")
            return

        image = message.photo
        u.set_affiliazione({
            "image_id" : image.file_id
        })

        text = (
            "<b>La nuova affiliazione è pronta per essere aggiunta, procedere per pubblicarla?</b>\n\n"
            "<b>N.B.</b>\n"
            "<i>Cliccando su \"No\" l'attuale processo verrà eliminato e sarà necessario ripartire da capo per aggiungere questa affiliazione.</i>"
        )

        btns = botogram.Buttons()
        btns[0].callback("Sì", "confirm_link", "Sì")
        btns[0].callback("No", "confirm_link")

        chat.send(text, syntax="HTML", attach=btns)
    
    elif u.state() == "category_name":
        u.state("category_description")
        category_name = message.text
        utils.create_category(category_name)

        btns = botogram.Buttons()
        btns[0].callback("Skip", "show_categories")

        text = (
            "<b>Inviami una breve descrizione della categoria. Puoi usare la formattazione HTML se desideri personalizzare il testo</b>\n\n"
            "<i>Puoi saltare questo passaggio cliccando sul button <b>\"Skip\"</b> qua sotto</i>"
        )

        chat.send(text, syntax="HTML", attach=btns)
    
    elif u.state() == "category_description":
        u.state("home")

        utils.set_last_category({
            "description" : message.text
        })

        text = (
            "<b>Nuova categoria creata con successo!</b> ✅"
        )

        btns = botogram.Buttons()
        btns[0].callback("Back", "show_categories")

        chat.send(text, syntax="HTML", attach=btns)
    
    elif u.state() == "prediction_name":
        u.state("prediction_description")

        prediction_name = message.text
        category_id = u.path().split("/")[-1]

        utils.create_prediction(prediction_name, category_id=int(category_id))

        btns = botogram.Buttons()

        text = (
            "<b>Inviami una breve descrizione della categoria. Puoi usare la formattazione HTML se desideri personalizzare il testo</b>\n\n"
            "Questo messaggio deve contenere uno o più pronostici che verranno visualizzati all'utente."
        )

        chat.send(text, syntax="HTML", attach=btns)

    elif u.state() == "prediction_description":
        u.state("home")
        category_id = u.path().split("/")[-1]

        utils.set_last_prediction({
            "description" : message.text
        })

        text = (
            "<b>Nuovo pronostico creato con successo!</b> ✅"
        )

        btns = botogram.Buttons()
        btns[0].callback("Back", "show_predictions", category_id)

        chat.send(text, syntax="HTML", attach=btns)
