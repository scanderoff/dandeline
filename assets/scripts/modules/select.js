class Select {
    constructor(element) {
        this.container = element;
        this.btn = element.querySelector(".select > .select__value");
        this.options = element.querySelectorAll(".dropdown__btn");
        this.hidden = element.querySelector(".select__hidden");

        this.listenEvents();
    }

    listenEvents() {
        this.btn.addEventListener("click", this.onBtnClick.bind(this));

        for (const option of this.options) {
            option.addEventListener("click", this.onSelect.bind(this));
        }

        document.addEventListener("mouseup", this.onMouseUp.bind(this));
    }

    unlistenEvents() {

    }

    onSelect({target: option}) {
        const selected = option.textContent.trim();

        this.hidden.value = selected;

        const prevActive = this.container.querySelector(".dropdown__btn.active");
        prevActive?.classList.remove("active");
        option.classList.add("active");

        this.btn.querySelector("span").textContent = selected;

        this.hidden.dispatchEvent(new Event("change"));
    };

    onBtnClick() {
        this.container.classList.toggle("active");
    };

    onMouseUp(event) {
        if (this.container.classList.contains("active") && event.target !== this.btn) {
            this.onBtnClick(event);
        }
    };
}


export default Select;
