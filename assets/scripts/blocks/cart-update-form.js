// import Cookies from "js-cookie";


export default class CartUpdateForm {
    constructor($form) {
        this.$form = $form;

        this.$form.addEventListener("change", this.onChange.bind(this));
        // this.$form.addEventListener("submit", this.onSubmit.bind(this));
    }

    onChange() {
        const fd = new FormData(this.$form);
        const product_id = fd.get("product_id");
        const size_id = fd.get("size_id");
        const color_id = fd.get("color_id");

        if (![product_id, size_id, color_id].every(value => !!value)) {
            return;
        }

        const url = new URL("/catalog/variation", location.origin);

        url.searchParams.append("product_id", product_id);
        url.searchParams.append("size_id", size_id);
        url.searchParams.append("color_id", color_id);

        fetch(url)
            .then(response => response.json())
            .then(result => {
                console.log(result);

                if (!result["success"]) {
                    this.$form["do"].disabled = true;
                    this.$form["do"].title = "Нет в наличии";

                    this.$form["variation_id"].value = "";
                    return;
                }

                this.$form["do"].disabled = false;
                this.$form["do"].title = "";

                this.$form["variation_id"].value = result["variation_id"];
            })
        ;
    }

    // onSubmit(event) {
    //     event.preventDefault();

    //     const fd = new FormData(this.$form);
    //     fd.append("do", event.submitter.value);


    //     fetch(this.$form.action, {
    //         method: "POST",
    //         mode: "same-origin",

    //         headers: {
    //             "X-CSRFToken": Cookies.get("csrftoken"),
    //         },

    //         body: JSON.stringify({
    //             "do": fd.get("do"),
    //             "variation_id": fd.get("variation_id"),
    //         }),
    //     })
    //         .then(response => response.json())
    //         .then(this.onResponse.bind(this))
    //     ;
    // }

    // onResponse(result) {
    //     console.log(result);

    //     const {html, variationId, newQty} = result;

    //     if (html) {
    //         const $itemsList = document.querySelector(".cart-items__list");
    //         $itemsList.classList.remove("empty");
    //         $itemsList.insertAdjacentHTML("afterbegin", html);
    //     }

    //     const $items = document.querySelectorAll(`[data-variation-id="${variationId}"]`);

    //     $items.forEach($item => {
    //         const $qty = $item.querySelector(".cart-item-qty");

    //         if ($qty.matches("input")) {
    //             $qty.value = newQty;
    //         } else {
    //             $qty.textContent = newQty;
    //         }

    //         const $itemPrice = $item.querySelector(".cart-item-price");

    //         if ($itemPrice) {
    //             $itemPrice.textContent = result["itemPrice"];
    //         }
    //     });

    //     const $counters = document.querySelectorAll(".cart-counter");
    //     $counters.forEach($counter => $counter.textContent = result["totalItems"]);

    //     const $totalPrices = document.querySelectorAll(".cart-total-price");
    //     $totalPrices.forEach($price => $price.textContent = result["totalPrice"]);
    // }
}
