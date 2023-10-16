from ....objects.user import User

def process_command(chat, message):
    u = User(message.sender)

    if u.state() == 'home':
        u.state('add_link')

        text = (
            "<b>Inviami il link di affiliazione da aggiungere.</b>"
        )
    
    else:
        text = (
            "<b>Devi concludere prima l'aggiunta del link precedente.</b>\n"
            "Se pensi di aver sbagliato qualcosa digita /cancel per cancellare questo processo ed aggiungere un nuovo link."
        )
    chat.send(text, syntax = 'HTML')
