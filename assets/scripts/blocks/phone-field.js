import IMask from "imask";


const maskOptions = {
    mask: "+{7} (000) 000 00-00",
    lazy: true,

    prepare: function (appended, masked) {
        if (appended === "8" && masked.value === "+7 (") {
            return "";
        }

        return appended;
    },
};

function onMaskComplete({target: $field}) {
    const input = $field.closest(".input");

    input.classList.remove("error");
}

function onFocus({target: $field}) {
    $field.mask.updateOptions({
        lazy: false,
    });
}

function onBlur({target: $field}) {
    $field.mask.updateOptions({
        lazy: true,
    });
}


export default function initPhoneFields(selector) {
    const $phoneFields = document.querySelectorAll(selector);

    for (const $field of $phoneFields) {
        const mask = IMask($field, maskOptions);
        mask.on("complete", onMaskComplete);

        $field.mask = mask;

        $field.addEventListener("focus", onFocus);
        $field.addEventListener("blur", onBlur);
    }
}
