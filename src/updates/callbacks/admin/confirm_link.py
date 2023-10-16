from ....objects.user import User
from pony.orm import db_session, delete

def process_callback(message, data, query):
    u = User(query.sender)
    u.state("home")
    
    if data:
        u.set_affiliazione({
            "active": True
        })
    
        text = (
            "<b>Nuova affiliazione aggiunta con successo ✅</b>"
        )

    else:
        u.get_affiliazione(last=True, delete=True)
        
        text = (
            "<b>Affiliazione Eliminata.</b>\n"
            "Digita /addlink per aggiungerne una nuova."
        )
    
    message.edit(text, syntax="HTML")
