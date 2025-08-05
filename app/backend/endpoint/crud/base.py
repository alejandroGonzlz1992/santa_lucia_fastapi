# import
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

# local import
from app.backend.utils.constants import Constants as cns

# local router
crud_main: object = APIRouter(prefix=cns.URL_CRUD.value, tags=[cns.CRUD.value])


# GET -> Crud Main Page
@crud_main.get(cns.URL_BASE.value, response_class=HTMLResponse)
async def Getting_Crud_Main_Menu_Endpoint(
        request: Request

) -> object:
    """
    Handles the Crud URL endpoint of the application.
    Renders the main index.html template located under the base frontend directory.
    Passes the current request template context.

    Args:
        request (Request): The incoming HTTP request object.

    Returns:
        TemplateResponse: Rendered HTML response for the root page.
    """

    # return
    return cns.HTML_.value.TemplateResponse(
        "crud/index.html", context={
            "request": request
        }
    )
