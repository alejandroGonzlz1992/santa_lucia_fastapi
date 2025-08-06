// import
import {Static} from "../../../tools/constants.js";
import {Shared} from "../../../tools/shared.js";


/* Payment Dates Validator Class */
export class PaymentDateValidator {

    /* constructor */
    constructor(idForm) {
        this.form = document.getElementById(idForm);
        this.valid = true;
        this.data = Static.PAYMENT_DATE_FORM_DICT;

        /* init event validators */
        this.initEventValidators();
    }

    /* event validators */
    initEventValidators() {

        /* on-time validators */

        /* form submission */
        this.form.addEventListener("submit", (e) => {

            /* prevent form autosubmission */
            e.preventDefault();

            /* validate blank fields and selections */
            if(!this.validateBlankFields()) {
                /* return to on-time validators */
                return;
            }

            if(this.valid){
                /* submit form */
                this.form.submit();
            }
        });
    }

    /* blank fields */
    validateBlankFields() {
        /* flag */
        let allValid = true;

        /* traverse list of blank field div names */
        Static.PAYMENT_DATE_BLANK_FIELDS.forEach((item) => {
            /* current div element */
            let fieldData = this.data[item];
            /* dropdown and input field validation */
            let inputField = this.form.elements.namedItem(item);
            /* validate input field type dropdown */
            if(inputField.tagName === "SELECT" && inputField.value === "not_select") {
                /* change flag */
                allValid = false;
                /* get error div element from current div element */
                let errorDiv = document.getElementById(fieldData.div_id.status);
                /* display error message */
                if(errorDiv){
                    Shared.displayErrorMessages(inputField, errorDiv, fieldData.text.status);
                }
            }
            /* validate input field type text or date */
            else if(!inputField || inputField.value.trim() === "") {
                /* change flag */
                allValid = false;
                /* get error div element from current div element */
                let errorDiv = document.getElementById(fieldData.div_id.blank);
                /* display error message */
                if(errorDiv){
                    Shared.displayErrorMessages(inputField, errorDiv, fieldData.text.blank);
                }
            }
        });

        /* validate flag status */
        if(this.valid) {
            this.valid = allValid;
        }

        return this.valid;
    }

}