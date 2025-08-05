// import
import {Static} from "./constants.js";


/* Utilities functions, to be used in validators' classes */
export class Shared {

    /* display error message */
    static displayErrorMessages(input, div, text) {
        /* modify inner attributes */
        input.style.border = "1px solid rgba(231, 76, 60, 0.6)";
        input.style.boxShadow = "0 0 8px rgba(231, 76, 60, 0.4)";
        div.style.display = "block";
        div.textContent = text;
    }

    /* clear error message */
    static clearErrorMessages(input, div, text) {
        /* modify inner attributes */
        input.style.border = "";
        input.style.boxShadow = "";
        div.forEach((field) => {
            field.style.display = "none";
        });
    }

    /* validate input blank fields */
    static validateInputBlankFields(input, div, text, form) {
        /* while clicking on input, display style and error message */
        input.addEventListener("click", () => {
            if(input.value.trim() === ""){
                Shared.displayErrorMessages(input, div, text);
                form.valid = false;
            }
        });
        /* clear out style and error message after info is inputed */
        input.addEventListener("input", () => {
            if(input.value.trim() !== ""){
                Shared.clearErrorMessages(input, [div]);
                form.valid = true;
            }
        });
    }

    /* validate current date vs input date */
    static inputDateAndCurrentDateFormat(field){
        /* convert input to date object and format it */
        let createDate = new Date(field.value);
        let currentDate = new Date();

        createDate.setHours(0, 0, 0, 0);
        currentDate.setHours(0, 0, 0, 0);

        /* adjust create date to one day */
        createDate.setDate(createDate.getDate() + 1);

        return {"create": createDate, "current": currentDate};
    }

}