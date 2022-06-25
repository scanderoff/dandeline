
export default class CartRemoveForm {
    constructor($form) {
        this.$form = $form;

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
                "variation_id": fd.get("variation_id"),
            }),
        })
            .then(response => response.json())
            .then(this.onResponse.bind(this));
        ;
    }

    onResponse(result) {
        console.log(result);

        const {variationId} = result;

        const $items = document.querySelectorAll(`[data-variation-id="${variationId}"]`);

        $items.forEach($item => {
            $item.remove();
        });
    }
}
