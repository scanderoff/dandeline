// для корректной работы объект должен создаваться после события window.onload,
// чтобы применились все стили и шрифты. Т.о. offsetWidth вернет верное значение

class Marquee {
    constructor(element, options) {
        this.$container = element;
        this.$line = element.querySelector(".marquee__line");
        this.$lineClone = this.$line.cloneNode(true);

        element.appendChild(this.$lineClone);

        this.lineWidth = this.$line.getBoundingClientRect().width;

        this.duration = options.duration;

        if (options.rtl) {
            this.initTx = 0;
            this.direction = -1;
        } else {
            this.initTx = -this.lineWidth;
            this.direction = 1;
        }

        this.tick();
    }

    tick() {
        const animate = (now) => {
            let progress = (now - this.timestamp) / this.duration;

            if (progress > 1) {
                progress %= 1;
                this.timestamp = now;
            }

            const tx = this.direction * progress * this.lineWidth;

            this.$container.style.transform = `translateX(${this.initTx + tx}px)`;

            requestAnimationFrame(animate);
        };

        this.timestamp = performance.now();
        requestAnimationFrame(animate);
    }
}


export default Marquee;




// пример
// window.addEventListener("load", () => {
//     const marquee1 = new Marquee(document.getElementById("marquee"), {
//         duration: 30000,
//         rtl: true,
//     });
// });
