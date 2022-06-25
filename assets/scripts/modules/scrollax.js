class Scrollax {
    constructor(element, options) {
        this.element = element;
        this.speed = options.speed;

        this.prevY = window.innerHeight;
        this.ty = 0;
        this.requestId = 0;

        new IntersectionObserver(this.onIntersect.bind(this), {}).observe(element);
    }

    scroll() {
        const curY = this.element.getBoundingClientRect().top;
        const dy = curY - this.prevY;
        const offsetY = (this.speed - 1)*dy;

        this.ty += offsetY;
        this.element.style.transform = `translateY(${this.ty}px)`;

        this.prevY = curY + offsetY;

        this.requestId = requestAnimationFrame(() => this.scroll());
    }

    onIntersect(entries, observer) {
        const entry = entries[0];

        if (entry.isIntersecting) {
            this.requestId = requestAnimationFrame(() => this.scroll());
        } else {
            cancelAnimationFrame(this.requestId);
        }
    }
}


export default Scrollax;
