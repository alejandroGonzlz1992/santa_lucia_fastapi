# import
from fastapi import Request
from fastapi.responses import HTMLResponse

# local import
from app import Init_App_Config
from app.backend.utils.constants import Constants as cns


# instance app
app: object = Init_App_Config()


# app root endpoint
@app.get(cns.URL_ROOT.value, response_class=HTMLResponse)
async def Getting_Root_Endpoint(
        request: Request

) -> object:
    """
    Handles the root URL endpoint of the application.
    Renders the main index.html template located under the base frontend directory.
    Passes the current request and a timezone parameter to the template context.

    Args:
        request (Request): The incoming HTTP request object.

    Returns:
        TemplateResponse: Rendered HTML response for the root page.
    """

    # return
    return cns.HTML_.value.TemplateResponse(
        "base/index.html", context={
            "request": request, "params": {
                "time_zone": cns.TIMEZONE.value,
            }
        }
    )
