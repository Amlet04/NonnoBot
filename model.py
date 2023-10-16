from pony.orm import Database, PrimaryKey, Required, Optional, Set, Json
import config
from datetime import datetime

# ! SETUP DATABASE
db = Database()

db.bind(
    provider=config.DB_PROVIDER,
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    host=config.DB_HOST,
    database=config.DB_NAME
)

class Telegram_user(db.Entity):
    id = PrimaryKey(int)
    username = Optional(str, nullable = True)
    first_name = Optional(str, nullable = True)
    state = Required(str)
    path = Required(str)
    pronostici = Required(bool)

class Affiliazioni(db.Entity):
    id=PrimaryKey(int, auto=True)
    link=Required(str)
    service_name = Optional(str, nullable=True)
    description = Optional(str, nullable=True)
    active = Required(bool)
    image_id = Optional(str, nullable=True)
    added_at = Required(datetime)

class Categoria(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    description = Optional(str, nullable=True)
    pronostici = Set("Pronostici")

class Pronostici(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    description = Optional(str, nullable=True)
    parent_category = Required(Categoria)

    
db.generate_mapping(create_tables=True)
# ? END SETUP DATABASE