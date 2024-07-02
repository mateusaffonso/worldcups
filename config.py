import yaml

with open("config.yaml") as file:
    _config = yaml.load(file, Loader=yaml.FullLoader)

_database_conf = _config.get("database", {})

DATABASE_NAME = _database_conf.get("name")
DATABASE_USER = _database_conf.get("username")
DATABASE_PASSWORD = _database_conf.get("password")
DATABASE_HOST = _database_conf.get("host", "127.0.0.1")
#host=localhost, mas usa-se '127.0.0.1' para poder dar certo usando o WSL (https://superuser.com/questions/1354350/how-to-connect-to-mysql-running-on-xampp-through-wsl-terminal)
DATABASE_PORT = _database_conf.get("port", 3306)

DEGUB = _config.get("debug", False)
