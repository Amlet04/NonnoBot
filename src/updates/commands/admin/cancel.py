from ....objects.user import User
from pony.orm import db_session, delete

@db_session
def process_command(chat, message):
    u = User(message.sender)

    if u.state() == "home":
        text = (
            "<b>Non c'è nessuna sessione da cancellare</b>"
        )
    
    else:
        if u.state() != "add_link":
            u.get_affiliazione(last=True, delete=True)

        u.state("home")

        text = (
            "<b>Sessione cancellata.</b>\n\n"
            "<i>Puoi aggiungere un nuovo link digitando</i> /addlink"
        )
    
    chat.send(text, syntax="HTML")

