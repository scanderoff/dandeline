export default class CheckoutForm {
    constructor($element) {
        this.$element = $element;

        this.$element.addEventListener("submit", this._onSubmit.bind(this));
    }

    _onSubmit() {}
}
