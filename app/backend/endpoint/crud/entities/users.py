# import
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from typing import Annotated, Optional, Union

# local import
from app.backend.utils.constants import Constants as cns

# local router
users_main: object = APIRouter(prefix=cns.URL_CRUD.value, tags=[cns.CRUD.value])


# GET -> Users Main Page
@users_main.get(cns.URL_CRUD_USERS.value, response_class=HTMLResponse)
async def Getting_Crud_Users_Main_Endpoint(
        request: Request,
        fg: Annotated[str, None] = None
) -> object:
    """
    Handles the Crud URL endpoint of the application.
    Renders the main index.html template located under the base frontend directory.
    Passes the current request template context and fg flag for determine message for output operations.

    Args:
        request (Request): The incoming HTTP request object.
        fg (Optional): Optional flag for determine message for output operations.

    Returns:
        TemplateResponse: Rendered HTML response for the root page.
    """

    # return
    return cns.HTML_.value.TemplateResponse(
        "crud/entities/users/index.html", context={
            "request": request, "params": {
                "fg": fg, "ops": cns.OPS_CRUD.value
            }
        }
    )


# GET -> Users Create Page
@users_main.get(cns.URL_CRUD_USERS_REGISTER.value, response_class=HTMLResponse)
async def Getting_Crud_Users_Create_Endpoint(
        request: Request,
        fg: Annotated[str, None] = None,
        excpt: Annotated[str, None] = None
) -> object:
    """
    Handles the Crud URL endpoint of the application.
    Renders the main index.html template located under the base frontend directory.
    Passes the current request template context, the url path id related to the selected table record,  fg flag for
    determine message for output operations and excpt to displaying error message when db queries are met.

    Args:
        request (Request): The incoming HTTP request object.
        id (Integer): Id number for selected table record.
        fg (String): for determine message for output operations.
        excpt (String): for determine message for output query operations.
    Returns:
        TemplateResponse: Rendered HTML response for the root page.
    """

    # return
    return cns.HTML_.value.TemplateResponse(
        "crud/entities/users/create.html", context={
            "request": request, "params": {
                "fg": fg, "excpt": excpt, "ops": cns.OPS_CRUD.value
            }
        }
    )


# GET -> Users Update Page
@users_main.get(cns.URL_CRUD_USERS_UPDATE.value, response_class=HTMLResponse)
async def Getting_Crud_Users_Update_Endpoint(
        request: Request,
        id: Annotated[Union[int, str], None],
        fg: Annotated[str, None] = None,
        excpt: Annotated[str, None] = None
) -> object:
    """
    Handles the Crud URL endpoint of the application.
    Renders the main index.html template located under the base frontend directory.
    Passes the current request template context, the url path id related to the selected table record,  fg flag for
    determine message for output operations and excpt to displaying error message when db queries are met.

    Args:
        request (Request): The incoming HTTP request object.
        id (Integer): Id number for selected table record.
        fg (String): for determine message for output operations.
        excpt (String): for determine message for output query operations.
    Returns:
        TemplateResponse: Rendered HTML response for the root page.
    """

    # return
    return cns.HTML_.value.TemplateResponse(
        "crud/entities/users/update.html", context={
            "request": request, "id": id, 'params': {
                'fg': fg, 'excpt': excpt, 'ops': cns.OPS_CRUD.value
            }
        }
    )
