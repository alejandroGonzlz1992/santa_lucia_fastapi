# local import
from app.backend.endpoint.crud.base import crud_main
from app.backend.endpoint.crud.entities.roles import roles_main
from app.backend.endpoint.crud.entities.users import users_main
from app.backend.endpoint.crud.records.deductions import deductions_main
from app.backend.endpoint.crud.records.department import department_main
from app.backend.endpoint.crud.records.questions import question_main
from app.backend.endpoint.crud.records.schedule import schedule_main
from app.backend.endpoint.crud.records.payment_date import payment_date_main

# route list
Routes_API_List: list[object] = [
    crud_main, roles_main, users_main, deductions_main, department_main, question_main,
    schedule_main, payment_date_main]
