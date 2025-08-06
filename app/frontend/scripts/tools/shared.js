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

    /* formatting birthday date */
    static birthdayInputFormatting(field){
        /* convert input to date object and current date */
        let birthdayDate = new Date(field.value);
        let currentDate = new Date();

        currentDate.setHours(0, 0, 0, 0);

        /* underage and overage male, overage female */
        let underAge = new Date(currentDate);
        underAge.setFullYear(underAge.getFullYear() - Static.UNDERAGE);

        let overAgeMan = new Date(currentDate);
        overAgeMan.setFullYear(overAgeMan.getFullYear() - Static.RETIRE_AGE_MAN);

        let overAgeWoman = new Date(currentDate);
        overAgeWoman.setFullYear(overAgeWoman.getFullYear() - Static.RETIRE_AGE_WOMAN);

        /* return */
        return {"birth": birthdayDate, "under": underAge, "man": overAgeMan, "woman": overAgeWoman}
    }

    /* enable and disable password field values */
    static enableAndDisablePasswordField(passwordFields, buttonFields){
        /* define password and button lists */
        let passwords = [];
        let buttons = [];

        /* traverse passwords input fields and append element to list */
        passwordFields.forEach((passw) => {
            /* get element */
            let field = document.querySelector(passw);
            /* append */
            passwords.push(field);
        });

        /* traverse button fields and append element to list */
        buttonFields.forEach((button) => {
            /* get element */
            let bttn = document.querySelector(button);
            /* append */
            buttons.push(bttn);
        });

        /* combine both lists */
        let combine = passwords.map((field, index) => [field, buttons[index]]);

        /* event listener on combine list */
        combine.forEach(([passw, toggle]) => {
            if(passw && toggle) {
                /* event listener */
                toggle.addEventListener("click", function() {
                    /* change input attribute if button is click (hide or unhide) */
                    let type = passw.getAttribute("type") === "password" ? "text" : "password";
                    passw.setAttribute("type", type);

                    /* update eye-slash icon base on type change of input */
                    let icon = toggle.querySelector("i");
                    if(icon){
                        icon.classList.toggle("fa-eye");
                        icon.classList.toggle("fa-eye-slash");
                    }
                });
            }
        });
    }

}