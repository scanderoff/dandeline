import IMask from "imask";


const maskOptions = {
    mask: "+{7} (000) 000 00-00",
    lazy: false,

    prepare: function (appended, masked) {
        if (appended === "8" && masked.value === "+7 (") {
            return "";
        }

        return appended;
    },
};

function onMaskComplete({target: field}) {
    const input = field.closest(".input");

    input.classList.remove("error");
}

export default function initPhoneFields(selector) {
    const $phoneFields = document.querySelectorAll(selector);

    for (const $field of $phoneFields) {
        const mask = IMask($field, maskOptions);
        mask.on("complete", onMaskComplete);
    }
}
