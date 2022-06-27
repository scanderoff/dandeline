export default class FilterForm {
    constructor($el) {
        this.$form = $el;
        this.$resetBtn = $el.querySelector('.filter-form__btn[type="reset"]');

        // this.$form.addEventListener("submit", this.onSubmit.bind(this));
        this.$form.addEventListener("reset", this.onReset.bind(this));
    }

    // onSubmit(event) {
    //     // event.preventDefault();

    //     const $submitter = event.submitter;

    // }

    onReset() {
        location.search = "";
    }
}
