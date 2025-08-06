// import

/* global static dict class for static values */
export const Static = {

    /* general */
    MIN_ROLE_NAME_LENGTH: 5,
    IDENTIFICATION_LENGTH: 9,
    NAME_LASTNAME_LASTNAME2_LENGTH: 4,
    UNDERAGE: 18,
    RETIRE_AGE_MAN: 65,
    RETIRE_AGE_WOMAN: 63,
    MAX_CHILDREN: 12,
    PASSWORD_MIN_LENGTH: 9,
    PHONE_LENGTH: 8,
    GROSS_INCOME_MIN: 250000,
    GROSS_INCOME_MAX: 3000000,

    ENABLE_USER_CREATE_PASSWORD: [
        ["#id_user_password", "#id_user_password_confirm"],
        ["#id_user_password_bttn", "#id_user_confirm_password_bttn"]
    ],

    /* regex Dictionary */
    REGEX: {
        "only_numbers": /^\d+$/,
        "only_letters": /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$/,
        "email_format": /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
        "address": /^(?!\d+$)[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s.,]+$/,
        "percentage": /^\d+(\.\d{1,3})?$/,
        "question": /^[a-zA-Z0-9\s¿?.]+$/,
        "numbers_decimals": /^\d+(\.\d+)?$/,
        "password": /^(?=.*[a-zA-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>])[A-Za-z\d!@#$%^&*(),.?":{}|<>]+$/,
        "evaluation": /^(?=.*[a-zA-Z])[a-zA-Z0-9¿?,.\s]+$/,
    },

    /* Form Fields -> Contains a dict of form field div names, errors, and messages */

    // USER ROLES
    USER_ROLE_FORM_DICT: {
        "role_name": {
            "div_id": {
                "blank": "id_role_name_blank_field_error",
                "chars": "id_role_name_chars_field_error",
                "length": "id_role_name_length_field_error"
            },
            "text": {
                "blank": "Campo Obligatorio.",
                "chars": "Ingresar letras únicamente.",
                "length": "Nombre de rol debe tener mínimo cinco caracteres."
            }
        },
        "role_type": {
            "div_id": {
                "status": "id_role_type_status_field_error",
            },
            "text": {
                "status": "Debe seleccionar una de las opciones del menú.",
            }
        },
        "role_department": {
            "div_id": {
                "status": "id_role_department_status_field_error",
            },
            "text": {
                "status": "Debe seleccionar una de las opciones del menú.",
            }
        },
        "role_schedule": {
            "div_id": {
                "status": "id_role_schedule_status_field_error",
            },
            "text": {
                "status": "Debe seleccionar una de las opciones del menú.",
            }
        },
        "role_create_date": {
            "div_id": {
                "blank": "id_role_create_date_blank_field_error",
                "before": "id_role_create_date_before_field_error",
            },
            "text": {
                "blank": "Campo Obligatorio.",
                "before": "La fecha de registro no puede estar antes de la fecha actual.",
            }
        },
        "role_status": {
            "div_id": {
                "status": "id_role_status_field_error",
            },
            "text": {
                "status": "Debe seleccionar una de las opciones del menú.",
            }
        },
    },

    USER_ROLE_BLANK_FIELDS: [
        "role_name", "role_type", "role_department",
        "role_schedule", "role_create_date", "role_status"
    ],

    // USER
    USER_FORM_DICT: {
        "user_identification": {
            "div_id": {
                "blank": "id_identification_blank_field_error",
                "chars": "id_identification_chars_field_error",
                "length": "id_identification_length_field_error"
            },
            "text": {
                "blank": "Campo obligatorio.",
                "length": "El número de identificación debe contener nueve dígitos.",
                "chars": "El número de identificación solamente pueden ser números.",
            }
        },
        "user_name": {
            "div_id": {
                "blank": "id_name_blank_field_error",
                "chars": "id_name_chars_field_error",
                "length": "id_name_length_field_error",
            },
            "text": {
                "blank": "Campo obligatorio.",
                "length": "El nombre de usuario debe tener mínimo cuatro caracteres.",
                "chars": "El nombre de usuario solamente pueden ser letras.",
            }
        },
        "user_lastname": {
            "div_id": {
                "blank": "id_lastname_blank_field_error",
                "chars": "id_lastname_chars_field_error",
                "length": "id_lastname_length_field_error",
            },
            "text": {
                "blank": "Campo obligatorio.",
                "length": "El apellido de usuario debe tener mínimo cuatro caracteres.",
                "chars": "El apellido de usuario solamente pueden ser letras.",
            }
        },
        "user_lastname2": {
            "div_id": {
                "blank": "id_lastname2_blank_field_error",
                "chars": "id_lastname2_chars_field_error",
                "length": "id_lastname2_length_field_error",
            },
            "text": {
                "blank": "Campo obligatorio.",
                "length": "El segundo apellido de usuario debe tener mínimo cuatro caracteres.",
                "chars": "El segundo apellido de usuario solamente pueden ser letras.",
            }
        },
        "user_birthday": {
            "div_id": {
                "blank": "id_birthday_date_blank_field_error",
                "under": "id_birthday_date_underage_field_error",
                "man": "id_birthday_date_overage_man_field_error",
                "woman": "id_birthday_date_overage_woman_field_error",
            },
            "text": {
                "blank": "Campo obligatorio.",
                "under": "No se permite el registro de menores de edad.",
                "man": "La edad máxima de registro es de 65 años para hombres.",
                "woman": "La edad máxima de registro es de 63 años para mujeres.",
            }
        },
        "user_gender": {
            "div_id": {
                "status": "id_user_gender_status_field_error",
            },
            "text": {
                "status": "Debe seleccionar una de las opciones del menú.",
            }
        },
        "user_marital_status": {
            "div_id": {
                "status": "id_user_marital_status_field_error",
            },
            "text": {
                "status": "Debe seleccionar una de las opciones del menú.",
            }
        },
        "user_children": {
            "div_id": {
                "blank": "id_user_children_blank_field_error",
                "chars": "id_user_children_chars_field_error",
                "max": "id_user_children_max_field_error",
            },
            "text": {
                "blank": "Campo obligatorio.",
                "chars": "Ingresar números únicamente.",
                "max": "La cantidad máxima de hijos es de doce.",
            }
        },
        "user_password": {
            "div_id": {
                "blank": "id_user_password_blank_field_error",
                "format": "id_user_password_format_field_error",
                "length": "id_user_password_length_field_error",
            },
            "text": {
                "blank": "Campo obligatorio.",
                "format": "Formato incorrecto de contraseña.",
                "length": "La contraseña debe contener mínimo nueve caracteres.",
            }
        },
        "user_password_confirm": {
            "div_id": {
                "blank": "id_user_confirm_password_blank_field_error",
                "mismatch": "id_user_confirm_password_mistmatch_field_error"
            },
            "text": {
                "blank": "Campo obligatorio.",
                "mismatch": "Las contraseñas ingresadas no coinciden.",
            }
        },
        "user_email": {
            "div_id": {
                "blank": "id_email_blank_field_error",
                "format": "id_email_format_field_error"
            },
            "text": {
                "blank": "Campo obligatorio.",
                "format": "Formato incorrecto de correo electrónico.",
            }
        },
        "user_phone": {
            "div_id": {
                "blank": "id_phone_blank_field_error",
                "chars": "id_phone_chars_field_error",
                "length": "id_phone_length_field_error"
            },
            "text": {
                "blank": "Campo obligatorio.",
                "chars": "Ingresar números únicamente.",
                "length": "El número telefónico debe tener nueve dígitos únicamente."
            }
        },
        "user_gross_income": {
            "div_id": {
                "blank": "id_gross_income_blank_field_error",
                "chars": "id_gross_income_chars_field_error",
                "min": "id_gross_income_min_field_error",
                "max": "id_gross_income_max_field_error",
            },
            "text": {
                "blank": "Campo obligatorio.",
                "chars": "Ingresar números únicamente.",
                "min": "El ingreso bruto mínimo es de 250.000 CRC.",
                "max": "El ingreso bruto máximo es de 3.000.000 CRC.",
            }
        },
        "user_create_date": {
            "div_id": {
                "blank": "id_user_create_date_blank_field_error",
                "before": "id_user_create_date_before_field_error",
            },
            "text": {
                "blank": "Campo obligatorio.",
                "before": "La fecha de registro no puede estar antes de la fecha actual.",
            }
        },
    },

    USER_BLANK_FIELDS: [
        "user_identification", "user_name", "user_lastname", "user_lastname2", "user_birthday", "user_gender",
        "user_marital_status", "user_children", "user_password", "user_password_confirm", "user_email", "user_phone",
        "user_gross_income", "user_create_date"
    ],

    // DEDUCTIONS
    DEDUCTIONS_FORM_DICT: {

    },

    DEDUCTIONS_BLANK_FIELDS: [

    ],

    // DEPARTMENTS
    DEPARTMENTS_FORM_DICT: {

    },

    DEPARTMENTS_BLANK_FIELDS: [

    ],

    // PAYMENT DATE
    PAYMENT_DATE_FORM_DICT: {

    },

    PAYMENT_DATE_BLANK_FIELDS: [

    ],

    // QUESTIONS
    QUESTIONS_FORM_DICT: {

    },

    QUESTIONS_BLANK_FIELDS: [

    ],

    // SCHEDULE
    SCHEDULE_FORM_DICT: {

    },

    SCHEDULE_BLANK_FIELDS: [

    ],

}