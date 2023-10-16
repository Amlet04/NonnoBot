from model import Affiliazioni, Telegram_user
from datetime import datetime as dt
from pony.orm import *

class User:

    @db_session
    def __init__(self, sender):
        '''
        Create a new User Object
        :param sender: Telegram's User Object
        '''
        self.id = sender.id
        self.username = sender.username
        self.first_name = sender.first_name

        u = self.get()

        if not u:
            user = Telegram_user(
                id = self.id,
                username = self.username,
                first_name = self.first_name,
                state='home',
                path="/home",
                pronostici = False
            )
        elif u.username != self.username:
            self.set_user({"username" : self.username})
        elif u.first_name != self.first_name:
            self.set_user({"first_name" : self.first_name})
    
    @db_session
    def get(self):
        '''
        Getting Database's User Object (row)
        :return: user
        '''
        user = Telegram_user.get(id = self.id)
        return user

    @db_session
    def set_user(self, values):
        self.get().set(**values)

    @db_session
    def state(self, new_state= None):
        '''
        Getting or Setting User's state
        :param new_state: new state to set
        :return: state
        '''
        user = self.get()
        if new_state:
            user.state = new_state
        return user.state
    
    @db_session
    def path(self, new_path= None):
        '''
        Getting or Setting User's path
        :param new_state: new path to set
        :return: path
        '''
        user = self.get()
        if new_path:
            user.path = new_path
        return user.path

    @db_session
    def create_affiliazione(self, link):
        a = Affiliazioni(
            link=link,
            service_name=None,
            description=None,
            active=False,
            added_at=dt.now()
        )
    
    @db_session
    def get_affiliazione(self, last=False, delete=False):
        if last:
            newest_a = None
            for a in Affiliazioni.select():
                if not newest_a:
                    newest_a = a
                elif newest_a.added_at < a.added_at:
                    newest_a = a
            
            if delete:
                newest_a.delete()
            else:
                return newest_a
        else:
            affiliazioni_list = select(a for a in Affiliazioni if a.active)[:]
            return affiliazioni_list
    
    @db_session
    def set_affiliazione(self, values):
        a = self.get_affiliazione(last=True)
        if a:
            a.set(**values)

    def is_authorized(self):
        return self.get().pronostici
