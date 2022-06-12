export default class Cart {
    constructor(user) {
        this.user = user;

        const $actions = document.querySelectorAll("[data-product-id][data-action]");

        for (const $action of $actions) {
            $action.addEventListener("click", this._onActionClick.bind(this));
        }
    }

    update(action, productId) {
        const csrftoken = getCookie("csrftoken");

        fetch("/update_order_item", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken,
            },
            body: JSON.stringify({
                "product_id": productId,
                "action": action,
            }),
        })
            .then(response => response.json())
            .then(result => {
                console.log(result);
                location.reload();
            })
        ;
    }

    _onActionClick(e) {
        const $action = e.currentTarget;

        const productId = $action.dataset.productId;
        const action = $action.dataset.action;

        if (this.user === "AnonymousUser") {
            console.log("Anon");
        } else {
            this.update(action, productId);
        }
    }
}
