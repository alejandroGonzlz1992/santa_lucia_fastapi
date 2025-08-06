# import
from fastapi.templating import Jinja2Templates
from enum import Enum
from zoneinfo import ZoneInfo
from datetime import datetime
from pathlib import Path

# local import
from app.backend.utils.local import local


# constant values
class Constants(Enum):
   """

   """
    # db connection string
   CONN_STRING = (f"postgresql://{local.db_username}:{local.db_password}"
                  f"@{local.db_host}:{local.db_port}/{local.db_name}")

   # time zone banner
   TIMEZONE = datetime.now(ZoneInfo('America/Costa_Rica')).strftime("%d-%m-%Y | %-I:%M %p")

   # jinja2 engine
   TEMPLATES = Path(__file__).resolve().parent.parent.parent
   TEMPLATES_DIR = f"{TEMPLATES}/frontend/templates"
   HTML_ = Jinja2Templates(directory=TEMPLATES_DIR)

   # static folder path
   STATIC_DIR, STATIC_PATH, STATIC_NAME = "/frontend", "app/frontend", "static"

   # calendar
   CALENDAR = {
       "months": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
                  "Noviembre", "Diciembre"],
       "days": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                29, 30, 31]
   }

   # root endpoint
   VRS = "v1_"
   URL_ROOT = f"/api/{VRS}"
   URL_ID = "{id}"
   URL_BASE = "/"

   # endpoint tags
   ROOT, CRUD = "BASE", "CRUD"

   """route names for endpoints"""

   # auth

   # crud
   URL_CRUD = f"{URL_ROOT}/mantenimientos"

   URL_CRUD_USERS = "/usuarios"
   URL_CRUD_USERS_REGISTER = f"{URL_CRUD_USERS}/registrar"
   URL_CRUD_USERS_UPDATE = f"{URL_CRUD_USERS}/actualizar/{URL_ID}"

   URL_CRUD_ROLES = "/roles"
   URL_CRUD_ROLES_REGISTER = f"{URL_CRUD_ROLES}/registrar"
   URL_CRUD_ROLES_UPDATE = f"{URL_CRUD_ROLES}/actualizar/{URL_ID}"

   URL_CRUD_DEPARTMENT = "/departamentos"
   URL_CRUD_DEPARTMENT_REGISTER = f"{URL_CRUD_DEPARTMENT}/registrar"
   URL_CRUD_DEPARTMENT_UPDATE = f"{URL_CRUD_DEPARTMENT}/actualizar/{URL_ID}"

   URL_CRUD_SCHEDULES = "/jornadas"
   URL_CRUD_SCHEDULES_REGISTER = f"{URL_CRUD_SCHEDULES}/registrar"
   URL_CRUD_SCHEDULES_UPDATE = f"{URL_CRUD_SCHEDULES}/actualizar/{URL_ID}"

   URL_CRUD_DEDUCTIONS = "/deducciones"
   URL_CRUD_DEDUCTIONS_REGISTER = f"{URL_CRUD_DEDUCTIONS}/registrar"
   URL_CRUD_DEDUCTIONS_UPDATE = f"{URL_CRUD_DEDUCTIONS}/actualizar/{URL_ID}"

   URL_CRUD_PAYMENT_DATES = "/fechas_pago"
   URL_CRUD_PAYMENT_DATES_REGISTER = f"{URL_CRUD_PAYMENT_DATES}/registrar"
   URL_CRUD_PAYMENT_DATES_UPDATE = f"{URL_CRUD_PAYMENT_DATES}/actualizar/{URL_ID}"

   URL_CRUD_QUESTION = "/preguntas_evaluativas"
   URL_CRUD_QUESTION_REGISTER = f"{URL_CRUD_QUESTION}/registrar"
   URL_CRUD_QUESTION_UPDATE = f"{URL_CRUD_QUESTION}/actualizar/{URL_ID}"

   # services

   # profile

   """operations message banners"""

   # crud
   OPS_CRUD = {
      'user': {
         '_create': 'El registro de usuario fue creado de forma exitosa.',
         '_update': 'El registro de usuario fue actualizado de forma exitosa.',
         '_fail': 'Existen errores en la información ingresada.',
         '_except': {
            'identification': 'El número de identificación ingresado, ya se encuentra registrado en la base de datos.',
            'email': 'El correo electrónico ingresado, ya se encuentra registrado en la base de datos.',
            'phone': 'El número de teléfono ingresado, ya se encuentra registrado en la base de datos.',
            'update_date': 'La fecha de actualización no puede estar antes de la fecha de creación en los registros.',
         }
      },
      'role': {
         '_create': 'El registro de rol de usuario fue creado de forma exitosa.',
         '_fail': 'Existen errores en la información ingresada.',
         '_update': {
            "_update": 'El registro de rol de usuario fue actualizado de forma exitosa.',
            "_except": 'La fecha de actualización no puede estar antes de la fecha de creación en los registros.'
         }
      },
      'department': {
         '_create': 'El registro departamento fue creado de forma exitosa.',
         '_update': 'El registro departamento fue actualizado de forma exitosa.',
      },
      'schedule': {
         '_create': 'El registro de jornada laboral fue creado de forma exitosa.',
         '_update': 'El registro de jornada laboral fue actualizado de forma exitosa.',
      },
      'deduction': {
         '_create': 'El registro de deducción fue creado de forma exitosa.',
         '_update': 'El registro de deducción fue actualizado de forma exitosa.',
      },
      'pay_date': {
         '_create': 'El registro de fecha de pago fue creado de forma exitosa.',
         '_update': 'El registro de fecha de pago fue actualizado de forma exitosa.',
      },
      'evaluation': {
         '_create': 'El registro de pregunta de evaluación fue creado de forma exitosa.',
         '_update': 'El registro de pregunta de evaluación fue actualizado de forma exitosa.',
      },
   }

   # general

   # exceptions
