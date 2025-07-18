from .utils import sqlQuery

def setup_tables():
    sqlQuery("CREATE TABLE IF NOT EXISTS worlds (guild_id BIGINT PRIMARY KEY, world_name VARCHAR NOT NULL, world_description VARCHAR NOT NULL, world_genre VARCHAR NOT NULL, creator VARCHAR NOT NULL);")
