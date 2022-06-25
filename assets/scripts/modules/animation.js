import utils from "./utils.js";
import rafQueue from "./rafQueue.js";


class Animation {
    static _easings = {
        linear: x => x,
        easeOutSine: x => Math.sin(x * Math.PI/2),
        easeInOutSine: x => -(Math.cos(Math.PI * x) - 1) / 2,
    };

    isActive = false;
    time = 0;
    progress = 0.0;
    _direction = 1;
    _timestamp = 0;
    _requestId = 0;

    constructor($element, options) {
        this.$element = $element;

        this.duration = options.duration;
        this.easing = Animation._easings[options.easing];
        this.update = options.update;

        // this.eventListeners = {};
    }

    play() {
        this._run(1);

        return this;
    }

    reverse() {
        this._run(-1);

        return this;
    }

    pause() {
        cancelAnimationFrame(this._requestId);

        this.isActive = false;

        return this;
    }

    _run(dir) {
        this._direction = dir;

        if (this.isActive) {
            return;
        }

        this.isActive = true;

        this._timestamp = performance.now();
        setTimeout(() => {
            this._requestId = requestAnimationFrame(() => this._loop());
        }, 1);
    }

    _loop() {
        const now = performance.now();

        this.time += this._direction * (now - this._timestamp);
        this.time = utils.clamp(this.time, 0, this.duration);
        this._timestamp = now;

        const timeFraction = utils.clamp(this.time/this.duration, 0, 1);

        this.progress = this.easing(timeFraction);
        this.update(this.$element, this.progress);

        if (0 < timeFraction && timeFraction < 1) {
            this._requestId = requestAnimationFrame(() => this._loop());
        } else {
            this.isActive = false;
        }
    }
}


export default Animation;
