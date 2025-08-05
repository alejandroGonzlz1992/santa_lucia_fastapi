# import
from logging import getLogger, CRITICAL
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# local import
from app.backend.utils.constants import Constants as cns
from app.backend.utils.registry import Routes_API_List


# suppressing bcrypt version warning
getLogger('passlib.handlers.bcrypt').setLevel(CRITICAL)


# app init config
def Init_App_Config() -> object:
    """
    Initializes and configures the FastAPI application.

    This includes:
    - Loading database models.
    - Creating the FastAPI app instance.
    - Mounting static file paths.
    - Including API route handlers.

    Returns:
        FastAPI: The configured FastAPI application instance.
    """

    # load db models

    # app instance
    app: object = FastAPI()

    # mount a static path to serve static assets
    app.mount(cns.STATIC_DIR.value, StaticFiles(directory=cns.STATIC_PATH.value), name=cns.STATIC_NAME.value)

    # include api routes
    for route in Routes_API_List:
        app.include_router(router=route)

    # return app
    return app
