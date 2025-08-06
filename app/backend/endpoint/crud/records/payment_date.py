# import
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from typing import Annotated, Optional, Union

# local import
from app.backend.utils.constants import Constants as cns

# local router
payment_date_main: object = APIRouter(prefix=cns.URL_CRUD.value, tags=[cns.CRUD.value])


# GET -> Payment Date Main Page
@payment_date_main.get(cns.URL_CRUD_PAYMENT_DATES.value, response_class=HTMLResponse)
async def Getting_Crud_Payment_Date_Main_Endpoint(
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
        "crud/records/payments/index.html", context={
            "request": request, "params": {
                "fg": fg, "ops": cns.OPS_CRUD.value
            }
        }
    )


# GET -> Payment Date Create Page
@payment_date_main.get(cns.URL_CRUD_PAYMENT_DATES_REGISTER.value, response_class=HTMLResponse)
async def Getting_Crud_Payment_Date_Create_Endpoint(
        request: Request
) -> object:
    """
    Handles the Crud URL endpoint of the application.
    Renders the main index.html template located under the base frontend directory.
    Passes the current request template context
    Args:
        request (Request): The incoming HTTP request object.
    Returns:
        TemplateResponse: Rendered HTML response for the root page.
    """

    # return
    return cns.HTML_.value.TemplateResponse(
        "crud/records/payments/create.html", context={
            "request": request
        }
    )


# GET -> Payment Date Update Page
@payment_date_main.get(cns.URL_CRUD_PAYMENT_DATES_UPDATE.value, response_class=HTMLResponse)
async def Getting_Crud_Payment_Date_Update_Endpoint(
        request: Request,
        id: Annotated[Union[int, str], None]
) -> object:
    """
    Handles the Crud URL endpoint of the application.
    Renders the main index.html template located under the base frontend directory.
    Passes the current request template context
    Args:
        request (Request): The incoming HTTP request object.
    Returns:
        TemplateResponse: Rendered HTML response for the root page.
    """

    # return
    return cns.HTML_.value.TemplateResponse(
        "crud/records/payments/update.html", context={
            "request": request, "id": id
        }
    )
