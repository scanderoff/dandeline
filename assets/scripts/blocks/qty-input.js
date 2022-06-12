class QtyInput {
    constructor($el) {
        this.$downBtn = $el.querySelector(".qty-input__btn--down");
        this.$upBtn = $el.querySelector(".qty-input__btn--up");
        this.$field = $el.querySelector(".qty-input__field");

        this.$downBtn.addEventListener("click", this.onDownBtnClick.bind(this));
        this.$upBtn.addEventListener("click", this.onUpBtnClick.bind(this));
    }

    onDownBtnClick(e) {
        this.$field.value = +this.$field.value - 1;
    }

    onUpBtnClick(e) {
        this.$field.value = +this.$field.value + 1;
    }
}

export default QtyInput;
