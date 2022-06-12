import Animation from "./animation.js";


class Page {
    constructor() {
        this.$element = document.documentElement;
        const scrollbarWidth = window.innerWidth - this.$element.offsetWidth;
        this.$element.style.setProperty("--scrollbar-width", `${scrollbarWidth}px`);

        this.isLocked = false;
    }

    toggleScroll(force) {
        if (!this.isLocked || force) {
            this.lockScroll();
        } else {
            this.unlockScroll();
        }
    }

    unlockScroll() {
        this.$element.classList.remove("locked");

        this.isLocked = false;
    }

    lockScroll() {
        this.$element.classList.add("locked");

        this.isLocked = true;
    }

    // speed, offset
    goto($target, options) {
        if (typeof $target === "string") {
            $target = document.querySelector($target);
        }

        const distance = $target.getBoundingClientRect().top - options.offset;
        const time = Math.abs(distance/options.speed * 1000);

        if (time === 0) {
            return;
        }

        const y = window.scrollY;

        new Animation(this.$element, {
            duration: time,
            easing: "easeInOutSine",

            update($element, progress) {
                $element.scrollTop = y + progress*distance;
            },
        }).play();
    }
}


export default Page;
