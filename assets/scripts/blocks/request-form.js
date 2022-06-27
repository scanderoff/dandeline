import Cookies from "js-cookie";


export default class RequestForm {
    constructor($el) {
        this.$form = $el;
        this.$stepDefault = $el.querySelector(".form__step--default");
        this.$stepSuccess = $el.querySelector(".form__step--success");

        this.$form.addEventListener("submit", this.onSubmit.bind(this));
    }

    onSubmit(event) {
        event.preventDefault();

        const fd = new FormData(this.$form);


        fetch(this.$form.action, {
            method: "POST",
            mode: "same-origin",

            headers: {
                "X-CSRFToken": Cookies.get("csrftoken"),
            },

            body: JSON.stringify({
                "name": fd.get("name"),
                "phone": fd.get("phone"),
            }),
        })
            .then(response => response.json())
            .then(this.onResponse.bind(this))
        ;
    }

    onResponse(result) {
        if (!result["success"]) {
            alert("Ошибка");
        }

        this.$form.reset();
        this.$stepDefault.classList.remove("active");
        this.$stepSuccess.classList.add("active");

        setTimeout(() => {
            this.$stepDefault.classList.add("active");
            this.$stepSuccess.classList.remove("active");
        }, 5000);
    }
}
