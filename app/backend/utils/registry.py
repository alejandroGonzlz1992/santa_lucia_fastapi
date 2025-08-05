# local import
from app.backend.endpoint.crud.base import crud_main
from app.backend.endpoint.crud.entities.roles import roles_main
from app.backend.endpoint.crud.entities.users import users_main

# route list
Routes_API_List: list[object] = [crud_main, roles_main, users_main]