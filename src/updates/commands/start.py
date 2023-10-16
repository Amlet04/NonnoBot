import botogram, config
from ...objects.user import User

def process_command(chat, message):
    u = User(message.sender)
    u.path("/home")

    text = (
        "Ciao {name}\n\n"
        "<i>Messaggio di benvenuto e spiegazione da inserire</i>"
        .format(
            name = message.sender.name,
        )
    )

    btns = botogram.Buttons()

    affiliazioni_list = u.get_affiliazione()
    
    idx = 0
    for affiliazione_index in range(len(affiliazioni_list)):
        btns[idx].callback(
            affiliazioni_list[affiliazione_index].service_name,
            "open_link",
            str(affiliazioni_list[affiliazione_index].id)
        )
        if affiliazione_index % 2 != 0:
            idx += 1
    
    if u.is_authorized():
        btns[idx + 1].callback("📊 Pronostici", "show_categories")
        
    btns[idx + 2].url(
        "☎️ Parla con noi",
        "t.me/{admin_username}".format(
            admin_username = config.ADMIN_USERNAME
        )
    )

    chat.send_photo(path=config.LOGO_PATH, caption=text, syntax="HTML", attach=btns)
