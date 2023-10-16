from pony.orm import db_session
from model import Affiliazioni
import config, botogram

def process_callback(message, data, query):
    with db_session:
        affiliazione = Affiliazioni.get(id=int(data))
    
    if affiliazione:
        text = affiliazione.description
        image_id = affiliazione.image_id

        btns = botogram.Buttons()
        btns[0].url("Vai all'offerta!", affiliazione.link)
        btns[1].callback("Back", "home")
        btns[1].url(
            "☎️ Parla con noi",
            "t.me/{admin_username}".format(
                admin_username = config.ADMIN_USERNAME
            )
        )
        chat = message.chat
        message.delete()
        chat.send_photo(file_id= image_id, caption=text, syntax="HTML", attach=btns)
    
    else:
        message.delete()
