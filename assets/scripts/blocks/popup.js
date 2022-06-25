import Page from "../modules/page.js";

import Eventable from "./eventable.js";



class Popup extends Eventable(class {
    static active = null;

    constructor($element) {
        this.$container = $element;
        this.$triggers = document.querySelectorAll(`[data-popup=${$element.id}]`);
        this.$closer = $element.querySelector(".popup__closer");

        this.listenEvents();
    }

    listenEvents() {
        for (const trigger of this.$triggers) {
            trigger.addEventListener("click", this.onTriggerClick.bind(this));
        }

        this.$closer.addEventListener("click", this.hide.bind(this));
        this.$container.addEventListener("click", this.onContainerClick.bind(this));

        document.addEventListener("keydown", this.onKeyDown.bind(this));
    }

    show() {
        this.$container.classList.add("active");

        Popup.active = this;

        this._emit("show");
    }

    hide() {
        this.$container.classList.remove("active");

        Popup.active = null;

        this._emit("hide");
    }

    onTriggerClick({currentTarget}) {
        this.$trigger = currentTarget;

        this.show();
    }

    onContainerClick({target, currentTarget}) {
        if (target === currentTarget) {
            this.hide();
        }
    }

    onKeyDown({key}) {
        if (!Popup.active || key !== "Escape") {
            return;
        }

        Popup.active.hide();
    }
}) {}


export default Popup;
