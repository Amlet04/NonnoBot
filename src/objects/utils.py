from model import Telegram_user, Categoria, Pronostici
from pony.orm import db_session

class Utils:

    def __init__(self):
        pass
    
    @staticmethod
    @db_session
    def get_user(username):
        for user in Telegram_user.select():
            if user.username.lower() == username.lower():
                return user
        return None
    
    # Category
    @staticmethod
    @db_session
    def get_category(category_id=None):
        if not category_id:
            return Categoria.select()[:]
        return Categoria.get(id=category_id)
    
    @staticmethod
    @db_session
    def create_category(name):
        c = Categoria(name=name)

    @staticmethod
    @db_session
    def get_last_category():
        c = None
        for category in Categoria.select():
            if not c:
                c = category
            elif c.id < category.id:
                c = category
        return c
    
    @staticmethod
    @db_session
    def set_last_category(values):
        c = Utils.get_last_category()
        c.set(**values)
    
    @staticmethod
    @db_session
    def delete_category(category_id):
        predictions = Utils.get_prediction(parent_id=category_id)
        for p in predictions:
            p.delete()
        c = Utils.get_category(category_id)
        c.delete()
    

    # Predictions
    @staticmethod
    @db_session
    def get_prediction(prediction_id=None, parent_id=None):
        if parent_id and not prediction_id:
            return Pronostici.select(parent_category=parent_id)[:]
        return Pronostici.get(id=prediction_id)
           
    @staticmethod
    @db_session
    def create_prediction(name, category_id):
        p = Pronostici(name=name, parent_category=category_id)


    @staticmethod
    @db_session
    def get_last_prediction():
        p = None
        for prediction in Pronostici.select():
            if not p:
                p = prediction
            elif p.id < prediction.id:
                p = prediction

        return p
    
    @staticmethod
    @db_session
    def set_last_prediction(values):
        p = Utils.get_last_prediction()
        p.set(**values)
    
        
    @staticmethod
    @db_session
    def delete_prediction(prediction_id):
        p = Utils.get_prediction(prediction_id=prediction_id)
        p.delete()
