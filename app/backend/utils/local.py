# import
from pydantic_settings import BaseSettings
from pathlib import Path


# local env class
class Local_Env_Settings(BaseSettings):
    """
    Loads and stores environment variables from a .env file using Pydantic's BaseSettings.

    Class defines key configuration values required for the application,
    such as database credentials, token settings, and application secrets.

    Attributes:
        db_username (str): Database username.
        Db_password (str): Database password.
        Db_host (str): Database host address.
        Db_port (str): Database port number.
        Db_name (str): Database name.
        Pg_admin_user (str): Username for pgAdmin.
        Pg_admin_password (str): Password for pgAdmin.
        Tkn_key (str): Secret key used to sign tokens.
        Tkn_algo (str): Algorithm used for token encryption.
        Tkn_expire (int): Token expiration time (in minutes).
        App_key (str): App email secret key.
    """

    # define key vars for .env attrs
    db_username: str
    db_password: str
    db_host: str
    db_port: str
    db_name: str
    pg_admin_user: str
    pg_admin_password: str
    tkn_key: str
    tkn_algo: str
    tkn_expire: int
    app_key: str

    # load .env file
    class Config:
        env_file = Path(__file__).resolve().parents[3] / ".env"


# instance class
local: object = Local_Env_Settings()
