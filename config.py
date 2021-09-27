import yaml

with open("config.yaml") as file:
    _config = yaml.load(file, Loader=yaml.FullLoader)

DATABASE_NAME = _config.get("database", {}).get("name")
DATABASE_USER = _config.get("database", {}).get("username")
DATABASE_PASSWORD = _config.get("database", {}).get("password")
DATABASE_HOST = _config.get("database", {}).get("host", "localhost")
DATABASE_PORT = _config.get("database", {}).get("port", 3306)
