from ....objects.user import User
from ....objects.utils import Utils

utils = Utils()

def process_command(chat, message, args, bot):
    u = User(message.sender)

    if not args:
        text = (
            "<b>Devi passare uno o più username come parametro/i del comando per poter autorizzare un o più utenti.</b>"
        )
        chat.send(text, syntax="HTML")
        return

    real_username = []
    for username in args:
        username = username.replace("@", "")
        db_user = utils.get_user(username)
        if db_user:
            user = User(
                bot.chat(db_user.id).admins[0]
            )

            user.set_user({
                "pronostici": True
            })
            real_username.append(user.username)
        else:
            chat.send(f"<b>L'utente @{username} non è stato trovato.</b>")

    if len(real_username) > 1:
        text = (
            "<b>I seguenti utenti:</b>\n\n"
        )
        for username in real_username:
            username = username.replace("@", "")
            text += f"👤 @{username}\n"
        
        text += (
            "\n<b>Sono autorizzati a visualizzare i pronostici.</b> ✅"
        )
        chat.send(text, syntax="HTML")
        
    elif len(real_username) == 1:
        text = (
            "<b>Ora @{username} è autorizzato a visualizzare i pronostici.</b> ✅"
            .format(
                username=args[0].replace("@", "")
            )
        )
    
        chat.send(text, syntax = "HTML")
